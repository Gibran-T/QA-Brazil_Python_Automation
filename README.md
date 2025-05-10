
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
