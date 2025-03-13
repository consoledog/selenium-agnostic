1. Clone the repository
2. Create virtual environment
   ```bash
   python3 -m venv venv
   ```
3. Activate virtual environment
   ```bash
   source venv/bin/activate  
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the tests:
   ```bash
   pytest -v tests/test_login.py
   pytest -v tests/test_register.py
   ```
Note: Websites, Webelement locators (Like ID or NAME), and credentials are just placeholders
you need to put your own data.