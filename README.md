# 🧪 QA-Brazil Python Automation Project – TripleTen Bootcamp

This repository contains automated test projects developed during **Sprint 7** and **Sprint 8** of the **TripleTen QA Engineering Bootcamp**.

It showcases:
- Basic Pytest structures with assert-based tests  
- Advanced automated UI testing using **Selenium** with the **Page Object Model (POM)** pattern  
- Clear separation between legacy/manual scripts and modern automation layers  
- Real-world QA architecture with scalable test components  

---

## 📁 Project Structure

QA-Brazil_Python_Automation/
├── legacy/                     # Sprint 7 – manual or base tests
│   └── main_sprint7.py
├── tests/                      # Automated Pytest scripts
│   └── test_main.py
├── urban_routes_project/       # POM pages, data, and helpers
│   ├── urban_routes_main_page.py
│   ├── helpers.py
│   └── data.py
├── .venv/                      # Python virtual environment (optional)
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation (this file)


---

## 🚀 How to Run the Tests

### 1. Activate the Virtual Environment (Windows)

```bash
.\.venv\Scripts\activate

Or create a new one:
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt

2. Run All Tests (Selenium + Pytest)

pytest tests/test_main.py --disable-warnings -s
Flags:

--disable-warnings → Suppresses warning messages

-s → Shows print statements in console

📦 Dependencies
To install all dependencies:
pip install -r requirements.txt

📚 Learning Outcomes
✅ Fundamentals of Python test automation

✅ Writing scalable test scripts with Pytest

✅ Applying Page Object Model (POM) with Selenium

✅ Modular architecture for test maintenance and scalability

✅ Integration of helper functions and test data separation

✅ CLI-based test execution and debugging

👤 Author
Thiago Gibran T. Nunes
QA Automation Engineer
International Experience (Canada, USA, Brazil)

Python, Pytest, Selenium

Web & API Testing

ERP / Supply Chain Systems

Git, Jira, CI-ready

📎 GitHub Profile
🔗 LinkedIn; www.linkedin.com/in/thiago-gibran-a01489b5

📌 Notes
This repository is public and structured to be reviewed by recruiters or hiring managers.

Each part was developed as part of a real QA Bootcamp, following industry-level methodologies.

---- Portuguese; 

# 🧪 Projeto Sprint 8 – Testes Automatizados com Selenium + Pytest

Este projeto contém a automação de testes da aplicação **Urban Routes**, desenvolvida durante a Sprint 8 do curso de QA da TripleTen. Os testes são baseados no padrão Page Object Model (POM) com uso de `Selenium`, `Pytest` e `asserts`.

---

## 📁 Estrutura do Projeto

```
project_sprint_8_QA_7_8/
├── legacy/                          # Arquivos da Sprint 7 (testes manuais)
│   └── main_sprint7.py
├── tests/                           # Testes automatizados com Pytest
│   └── test_main.py
├── urban_routes_project/           # Página POM e utilitários
│   ├── urban_routes_main_page.py
│   ├── helpers.py
│   └── data.py
├── .venv/                           # Ambiente virtual Python
└── requirements.txt                # Dependências do projeto
```

---

## ▶️ Como executar os testes

### 1. Ativar o ambiente virtual (Windows)

```bash
.\.venv\Scriptsctivate
```

### 2. Rodar todos os testes

```bash
pytest tests/test_main.py --disable-warnings -s
```

- `--disable-warnings`: oculta avisos.
- `-s`: exibe prints no console.

---

## 🧰 Executar fluxo completo da Sprint 7 (opcional)

```bash
python legacy/main_sprint7.py
```

> Esse script executa o fluxo completo de forma sequencial e visual, sem usar `pytest`. Serve como referência histórica.

---

## 📦 Dependências

Instale todas as dependências com:

```bash
pip install -r requirements.txt
```

---

## ✍️ Autor

**Thiago Gibran T. Nunes**  
QA Tester | Automação de Testes | Sprint 8 – TripleTen

---
