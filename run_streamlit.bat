REM Activate the virtual environment and run the Streamlit app
@echo off
if not exist ".venv\Scripts\activate" (
    echo MsgBox "Virtual environment not found. Please create it first.", 16, "Error" > temp.vbs
    cscript //nologo temp.vbs
    del temp.vbs
    exit /b 1
)
call .venv\Scripts\activate
streamlit run main.py