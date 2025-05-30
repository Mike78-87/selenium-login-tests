from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://berpress.github.io/selenium-login-demo/"

    def open(self):
        self.driver.get(self.url)

    def set_username(self, username):
        self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "username").send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, "login-btn").click()

    def get_message(self):
        wait = WebDriverWait(self.driver, 10)
        message_element = wait.until(EC.visibility_of_element_located((By.ID, "result")))
        return message_element.text
