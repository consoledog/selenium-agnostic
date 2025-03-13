from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    #Handles dynamic multi-step registration forms.

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        #Opens the registration page.
        self.driver.get(url)

    def get_visible_fields(self):
        #Finds and returns all input fields currently visible on the page
        return self.driver.find_elements(By.TAG_NAME, "input")

    def fill_fields(self, field_data):
        #Fills out available fields based on provided field data.
        visible_fields = self.get_visible_fields()
        
        for field in visible_fields:
            name = field.get_attribute("name")
            if name in field_data:
                field.clear()
                field.send_keys(field_data[name])

    def click_next_or_submit(self):
        #Clicks 'Next' if available, otherwise clicks 'Submit'.
        next_buttons = self.driver.find_elements(By.NAME, "next")
        submit_buttons = self.driver.find_elements(By.NAME, "submit")

        if next_buttons:
            next_buttons[0].click()
            return True  # Indicates more steps remain
        elif submit_buttons:
            submit_buttons[0].click()
            return False  # Last step, no more pages
        else:
            raise Exception("No 'Next' or 'Submit' button found!")

    def complete_registration(self, form_data):
        #Handles the registration process dynamically.
        while True:
            self.fill_fields(form_data)
            more_steps = self.click_next_or_submit()
            if not more_steps:
                break
