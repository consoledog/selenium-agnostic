from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        #Go to url
        self.driver.get(url)

    def enter_username(self, username):
        #Handle entering username if the field is available.
        username_fields = self.driver.find_elements(By.ID, "username")
        if username_fields:
            username_fields[0].send_keys(username)
            return True
        return False

    def enter_password(self, password):
        #Handle entering password if the field is available.
        password_fields = self.driver.find_elements(By.ID, "password")
        if password_fields:
            password_fields[0].send_keys(password)
            return True
        return False

    def click_next(self):
        #Click the 'Next' button if present.
        next_buttons = self.driver.find_elements(By.ID, "next")
        if next_buttons:
            next_buttons[0].click()
            return True
        return False

    def click_login(self):
        #Clicks the 'Login' button.
        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, "login")))
        login_button.click()

    def login(self, username, password):
        #Handles all three login cases dynamically.
        
        username_found = self.enter_username(username)
        password_found = self.enter_password(password)

        if username_found and password_found:
            # Case 1: Both fields are present (standard login form)
            self.click_login()
        
        elif username_found:
            # Case 2: Username first, then password
            self.click_next()
            self.wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
            self.click_login()
        
        elif password_found:
            # Case 3: Password first, then username
            self.click_next()
            self.wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
            self.click_login()
