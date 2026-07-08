import io
import pdfplumber
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

def extract_question_data(pdf_file):
    """
    Extracts question ID and chosen option data from the UGC PDF.
    """
    question_data = []
    # pdfplumber works perfectly with Streamlit's uploaded file objects
    with pdfplumber.open(pdf_file) as pdf:
        for page_num, page in enumerate(pdf.pages):
            text = page.extract_text()
            if not text:
                continue
            lines = text.split("\n")

            question_ids = []
            chosen_options = []
            correct_option = []

            for line in lines:
                if "Question ID :" in line:
                    question_ids.append(line.split(":")[1].strip())
                elif "Chosen Option :" in line:
                    chosen_options.append(line.split(":")[1].strip())
                elif "Correct Option :" in line:
                    correct_option.append(line.split(":")[1].strip())
                    correct_option = []

            for i in range(len(question_ids)):
                # Added a safety check in case options are blank/missing
                chosen_opt = chosen_options[i] if i < len(chosen_options) else "Not Attempted"
                question_data.append({
                    "Question ID": question_ids[i],
                    "Chosen Option": chosen_opt
                })

    sorted_question_data = sorted(question_data, key=lambda x: int(x['Question ID']))
    return sorted_question_data

def extract_correct_option_data(pdf_file):
    """
    Extracts question IDs and correct options from the answer key PDF.
    """
    question_data = []
    
    with pdfplumber.open(pdf_file) as pdf:
        for page_num, page in enumerate(pdf.pages):
            text = page.extract_text()
            if not text:
                continue
            lines = text.split("\n")

            collecting = False
            question_ids = []
            correct_options = []

            for line in lines:
                if "Question ID" in line and "Correct Option" in line:
                    collecting = True
                    continue

                if collecting:
                    if line.strip() and not any(x in line for x in ["Page", "https://"]):
                        columns = line.split()
                        
                        if len(columns) >= 3:
                            try:
                                question_id = columns[1].strip()
                                correct_option = columns[2].strip()

                                question_ids.append(question_id)
                                correct_options.append(correct_option)
                            except IndexError:
                                continue

            for i in range(len(question_ids)):
                question_data.append({
                    "Question ID": question_ids[i],
                    "Correct Option": correct_options[i],
                })

    return question_data

def calculate_score(response_file, answer_key_file):
    """
    Master function to process files and return an Excel file in memory.
    """
    # Extract data from both PDFs
    question_data_ugc = extract_question_data(response_file)
    question_data_ans = extract_correct_option_data(answer_key_file)

    # Convert the extracted data to DataFrames
    df1 = pd.DataFrame(question_data_ugc, columns=['Question ID', 'Chosen Option'])
    df2 = pd.DataFrame(question_data_ans, columns=['Question ID', 'Correct Option'])

    # Merge the DataFrames on 'Question ID'
    combined_df = pd.merge(df1, df2, on='Question ID', how='outer')

    # Determine if the chosen option is correct
    combined_df['Mark'] = combined_df.apply(
        lambda row: 'Correct' if row['Chosen Option'] == row['Correct Option'] else 'Incorrect',
        axis=1
    )

    # Calculate counts and marks
    correct_count = combined_df['Mark'].value_counts().get('Correct', 0)
    incorrect_count = combined_df['Mark'].value_counts().get('Incorrect', 0)
    
    marks_gained = correct_count * 2
    marks_lost = incorrect_count * 2

    # Create a new Workbook and add the extracted data
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = 'Combined Data'

    # Write the DataFrame to the sheet
    for r in dataframe_to_rows(combined_df, index=False, header=True):
        worksheet.append(r)

    # Write summary data directly below the existing data
    row_offset = len(combined_df) + 3
    worksheet.cell(row=row_offset, column=1, value='Marks Gained')
    worksheet.cell(row=row_offset, column=2, value=marks_gained)
    worksheet.cell(row=row_offset + 1, column=1, value='Marks Lost')
    worksheet.cell(row=row_offset + 1, column=2, value=marks_lost)

    # --- THE MAGIC HAPPENS HERE ---
    # Instead of saving to disk, we save to an in-memory buffer
    excel_buffer = io.BytesIO()
    workbook.save(excel_buffer)
    excel_buffer.seek(0) # Reset the pointer so Streamlit can read it from the beginning

    return excel_buffer
