@echo off
REM LLM Playground Runner for Windows
REM This script makes it easy to run the Gradio app on Windows

echo Starting LLM Playground...
echo.

REM Check if UV is installed
where uv >nul 2>&1
if %ERRORLEVEL% == 0 (
    echo Using UV to run the app...
    uv run python app.py
) else if exist "app.py" (
    echo Using Python to run the app...
    python app.py
) else (
    echo Python or app.py not found. Please install Python or UV.
    pause
    exit /b 1
)

