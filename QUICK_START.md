# 🚀 Quick Start Guide - OrangeHRM Automation

## ⚡ Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Tests
```bash
# Linux/Mac
bash run_tests.sh

# Windows
run_tests.bat

# Or directly with pytest
pytest tests/test_orangehrm_workflow.py -v
```

### Step 3: View Results
```bash
# Open HTML report
open reports/report.html  # Mac
xdg-open reports/report.html  # Linux
start reports/report.html  # Windows
```

---

## 🎯 Common Commands

### Run Specific Tests:
```bash
# Smoke test only (quick login check)
pytest -m smoke

# Complete E2E workflow
pytest -m e2e

# Single test
pytest tests/test_orangehrm_workflow.py::TestOrangeHRMWorkflow::test_01_login
```

### Run with Options:
```bash
# Verbose output
pytest -v

# Show print statements  
pytest -s

# Stop on first failure
pytest -x

# Run in parallel (install pytest-xdist first)
pytest -n 2
```

---

## 📋 Test Execution Order

1. Login ✅
2. Navigate to PIM ✅
3. Add Employee ✅
4. Search Employee (ID) ✅
5. Search Employee (Name) ✅
6. Edit Employee ✅
7. Data Import ✅
8. Navigate to Leave ✅
9. Apply Leave ✅
10. View Leave List ✅
11. Check My Leave ✅
12. Assign Leave ✅
13. Manage Entitlements ✅
14. Delete Employee ✅
15. Logout ✅

---

## 🔧 Configuration

Edit `config/config.py`:

```python
# Change browser
BROWSER = "firefox"  # Default: chrome

# Run in headless mode
HEADLESS = True  # Default: False

# Adjust timeouts
EXPLICIT_WAIT = 30  # Default: 20
```

---

## 📊 Reports & Logs

After running tests, check:

- **HTML Report**: `reports/report.html`
- **Logs**: `reports/logs/test_log_*.log`
- **Screenshots**: `reports/screenshots/` (on failures)

---

## 🐛 Troubleshooting

### Tests failing?
1. Check internet connection
2. Verify OrangeHRM demo site is accessible
3. Increase wait times in config.py
4. Check logs in `reports/logs/`

### Import errors?
```bash
# Make sure you're in project root
cd orangehrm_automation
pytest tests/
```

### WebDriver issues?
```bash
# Framework uses webdriver-manager
# It auto-downloads drivers
# Just ensure internet connection
```

---

## 📈 Next Steps

1. ✅ Run the smoke test first: `pytest -m smoke`
2. ✅ Run complete workflow: `pytest -m e2e`
3. ✅ Review HTML report
4. ✅ Check logs and screenshots
5. ✅ Customize config if needed

---

## 💡 Tips

- Run smoke test first to verify setup
- Check logs for detailed execution info
- Screenshots are auto-captured on failures
- Each test is independent and can run standalone
- Tests are numbered for sequential execution

---

**Happy Testing! 🎉**

For detailed documentation, see `README.md`
