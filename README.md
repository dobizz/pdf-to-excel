# pdf-to-excel

## Installation

Download and install `python3` and `pip` package manager
https://www.python.org/downloads/

Install dependencies
```bash
pip install -r requirements.txt .
```

Install developer dependencies (optional)
```bash
pip install -r requirements-dev.txt
```

## Building Executable for Windows (optional)
Requires developer dependencies installed, specifically `pyinstaller`

```bash
pyinstaller app.spec
```

This will generate `pdf2excel_v0.1.0.exe` inside the `dist` directory which will be created automatically
```bash
├── README.md
├── app.py
├── app.spec
├── dist
│   └── pdf2excel_v0.1.0.exe
├── pyproject.toml
├── requirements-dev.txt
├── requirements.txt
├── setup.py
├── src
│   ├── pdf2excel
│   │   ├── __init__.py
│   │   ├── regexes.py
│   │   └── tasks.py
└── tests
    ├── conftest.py
    └── pdf2excel_tests
        ├── __init__.py
        ├── regexes_test.py
        └── tasks_test.py
```

## Running
After installing the required dependencies, run the script
```bash
python3 app.py
```
or
```bash
python app.py
```