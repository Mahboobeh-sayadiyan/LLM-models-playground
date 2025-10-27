#!/bin/bash

# LLM Playground Runner
# This script makes it easy to run the Gradio app

echo "🚀 Starting LLM Playground..."
echo ""

# Check if UV is installed
if command -v uv &> /dev/null; then
    echo "✅ Using UV to run the app..."
    uv run python app.py
elif command -v python3 &> /dev/null; then
    echo "✅ Using Python to run the app..."
    python3 app.py
else
    echo "❌ Python not found. Please install Python or UV."
    exit 1
fi

