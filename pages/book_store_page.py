from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BookStorePage:

    SEARCH_BOX = (By.ID, "searchBox")
    BOOK_TITLE = (By.LINK_TEXT, "Git Pocket Guide")
    BOOK_ROWS = (By.CSS_SELECTOR, "tbody > tr")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://demoqa.com/books")

    def search_book(self, book_name):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_BOX)).send_keys(book_name)

    def get_row_count(self):
        return len(self.driver.find_elements(*self.BOOK_ROWS))

    def get_book_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.BOOK_TITLE)).text

    def open_book(self):
        self.wait.until(EC.element_to_be_clickable(self.BOOK_TITLE)).click()