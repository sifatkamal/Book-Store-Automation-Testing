from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_book_present(self, book_name):
        book_locator = (By.LINK_TEXT, book_name)
        return self.wait.until(EC.visibility_of_element_located(book_locator)).is_displayed()