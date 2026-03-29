#!/bin/bash

echo "=========================================="
echo "  OrangeHRM Automation Test Execution"
echo "=========================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt --quiet

echo ""
echo "🚀 Starting test execution..."
echo ""

# Run tests
pytest tests/test_orangehrm_workflow.py -v --html=reports/report.html --self-contained-html

echo ""
echo "=========================================="
echo "  Test Execution Completed!"
echo "=========================================="
echo ""
echo "📊 View HTML Report: reports/report.html"
echo "📝 Check Logs: reports/logs/"
echo "📸 Screenshots: reports/screenshots/"
echo ""
