import pytest
from selenium import webdriver

#Fixture for handling driver before and after a test
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
