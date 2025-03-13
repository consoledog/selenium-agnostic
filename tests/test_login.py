import pytest
from pages.login_page import LoginPage

# List of test cases with different websites, usernames, and passwords
TEST_DATA = [
    ("https://example1.com/login", "user1", "password1"),
    ("https://example2.com/login", "user1", "password1"),
    ("https://example3.com/login", "user1", "password1"),
]

@pytest.mark.parametrize("url, username, password", TEST_DATA)
def test_login(driver, url, username, password):
    #Tests login functionality across multiple websites dynamically.
    login_page = LoginPage(driver)
    login_page.open(url)
    login_page.login(username, password)

    #Note: Here can put some assertions after the login is done
