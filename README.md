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

Note: There are 2 ways to approach N - step registration process:
1. (Implemented) to fill empty fields and catch the "Next" and "Submit" button
2. To fill empty fields, and track what fields are filled in the code (Have a boolean value for each of the fields). On this way, code is agnostic also on the "Next" and "Submit" button. In other words, does not depend on what is the name of the button for the next step.
