from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    USERNAME_FIELD = (By.ID, "userName")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    GO_TO_STORE_BUTTON = (By.ID, "gotoStore")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://demoqa.com/login")

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def go_to_book_store(self):
        self.wait.until(EC.element_to_be_clickable(self.GO_TO_STORE_BUTTON)).click()