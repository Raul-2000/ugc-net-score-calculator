# 📝 UGC NET Score Calculator

A clean, fast, and automated tool designed to help UGC NET aspirants instantly evaluate their performance without hours of manual cross-checking.

**[👉 Click here to use the live calculator!](https://ugcnetcalc.streamlit.app/)**

---

## 📥 How to Get Your Required PDFs

To use the calculator with your own results, you need two specific PDF files:

### 1. Your Question Paper (Response Sheet)
* Log in to the official NTA UGC NET candidate portal.
* View your attempted question paper.
* Use your browser's print options (or click download if available) to save the entire page as a **PDF** directly to your device.

### 2. The Official Answer Key
* Open the official answer key page on the NTA website.
* Since NTA often displays this as a webpage table rather than a file download, use your browser's native **"Print to PDF"** feature (Ctrl+P / Cmd+P) or a browser extension (such as *Print Friendly & PDF*) to save that specific webpage layout as a **PDF**.

---

## 🚀 How to Use the Web App

1. Open the live web application link: [https://ugcnetcalc.streamlit.app/](https://ugcnetcalc.streamlit.app/)
2. Drag and drop your **Response Sheet PDF** into Box 1.
3. Drag and drop your **Answer Key PDF** into Box 2.
4. Click the **Calculate My Score** button.
5. View your immediate score breakdown on screen and download your detailed spreadsheet!

---

## 📊 Understanding Your Output (`Result.xlsx`)

The app provides a downloadable Excel file containing a clear matrix of your exam data:
* **Question ID:** The unique tracking number for each specific question.
* **Chosen Option:** The option ID you picked during the exam.
* **Correct Option:** The official answer key designation.
* **Mark:** Explicitly flags whether a question is `Correct`, `Incorrect`, or `Unattempted`.
* **Summary Blocks:** Located at the bottom of the worksheet, detailing total **Marks Gained** (+2 per correct answer) and **Marks Missed**.

---

## 💻 Running it Locally (For Developers)

### 🪟 For Windows Users

**1. Install Python:**
* Download and install the latest version of Python from the [Official Python Website](https://www.python.org/downloads/). 
* *Crucial:* During installation, check the box that says **"Add Python.exe to PATH"** before clicking install.

**2. Clone or Download the Code:**
* Open **Command Prompt (cmd)** or **PowerShell** and navigate to your project folder:
```cmd
cd path\to\your\ugc-net-calculator
```

**3. Set Up a Virtual Environment & Install Dependencies:**
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**4. Run the Application:**
```cmd
streamlit run app.py
```

---

### 🐧 For Linux Users (Fedora / Arch / Ubuntu)

**1. Clone the repository:**
```bash
git clone [https://github.com/your-username/ugc-net-calculator.git](https://github.com/your-username/ugc-net-calculator.git)
cd ugc-net-calculator
```

**2. Setup environment and install requirements:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**3. Run the application:**
```bash
streamlit run app.py
```

---

## 📁 Project Structure
* `app.py` - Streamlit frontend script handling theme-aware layout.
* `nta.py` - Core parsing algorithms utilizing `pdfplumber` and `pandas`.
* `requirements.txt` - Tracking external package versions.
