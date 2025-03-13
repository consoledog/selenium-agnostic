import pytest
from pages.registration_page import RegistrationPage

# Test data for different websites
# Brief explanation: For example "first_name": "Alice". In here, first_name is the name of the field on website (got by ID or NAME locator)
TEST_DATA = [
    ("https://example1.com/register", {"first_name": "Alice", "last_name": "Smith", "email": "alice@example.com", "password": "Secure123!"}),
    ("https://example2/register", {"username": "testuser", "email": "test@example.com", "password": "Pass1234!", "phone": "1234567890"}),
    ("https://example3/register", {"name": "Charlie", "dob": "1990-01-01", "city": "New York", "phone": "9876543210", "password": "SecurePass!"}),
]

@pytest.mark.parametrize("url, form_data", TEST_DATA)
def test_registration(driver, url, form_data):
    """Tests registration on multiple websites with different field structures."""
    registration_page = RegistrationPage(driver)
    registration_page.open(url)
    registration_page.complete_registration(form_data)

    #Note: Add appropriate assert