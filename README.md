# 🧪 Project: QA-Brazil_Python_Automation

This repository was developed during **Sprint 7 and Sprint 8** of the **TripleTen QA Engineering Bootcamp**. It includes automated tests for the **Urban Routes** application using **Python**, **Pytest**, and **Selenium**, following professional QA architecture standards.

---

## 🚀 Overview

This project contains:

- 🧱 **Sprint 7** – Foundational structure using Pytest and helper/data separation  
- 🧪 **Sprint 8** – Selenium-based UI testing using the Page Object Model (POM)

It showcases:

- ✅ Basic Pytest structures with assert-based tests  
- 🧠 Advanced automated UI testing using **Selenium** with the **Page Object Model (POM)** pattern  
- 🧹 Clear separation between legacy/manual scripts and modern automation layers  
- 🏗️ Real-world QA architecture with scalable test components  

---

## 📁 Project Structure

```text
QA-Brazil_Python_Automation/
├── legacy/                   # Sprint 7 – manual or base tests
│   └── main_sprint7.py
├── tests/                    # Automated Pytest scripts
│   └── test_main.py
├── urban_routes_project/     # POM pages, data, and helpers
│   ├── urban_routes_main_page.py
│   ├── helpers.py
│   └── data.py
├── .venv/                    # Python virtual environment (optional)
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation (this file)
```

---

## 🧪 How to Run the Tests

### 1. Activate the Virtual Environment (Windows)

```bash
.\.venv\Scriptsctivate
```

### 2. Install the Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run All Tests

```bash
pytest tests/test_main.py --disable-warnings -s
```

- `--disable-warnings`: suppress warning messages  
- `-s`: allow print output in console  

---

## 🧰 Legacy Test Execution (Optional)

You can run the Sprint 7 logic-based simulation script manually:

```bash
python legacy/main_sprint7.py
```

This script runs through the full workflow without `pytest`, acting as a visual or interview-style reference.

---

## 🧠 Learning Outcomes

- Organized QA automation projects with Pytest and Selenium  
- Implemented Page Object Model (POM) structure  
- Executed manual vs. automated validation flows  
- Experience setting up and running Python test suites  
- Modular code separation using `data.py` and `helpers.py`  

---

## 👨‍💻 Author

**Thiago Gibran T. Nunes**  
QA Automation Engineer | Python | Web & API Testing | ERP | International Experience

- GitHub: [Gibran-T](https://github.com/Gibran-T)  
- LinkedIn: [Thiago Gibran](https://www.linkedin.com/in/thiago-gibran-a01489b5)
