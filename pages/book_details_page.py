from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BookDetailsPage:

    ISBN = (By.CSS_SELECTOR, "#ISBN-wrapper #userName-value")
    TITLE = (By.CSS_SELECTOR, "#title-wrapper #userName-value")
    SUBTITLE = (By.CSS_SELECTOR, "#subtitle-wrapper #userName-value")
    AUTHOR = (By.CSS_SELECTOR, "#author-wrapper #userName-value")
    PUBLISHER = (By.CSS_SELECTOR, "#publisher-wrapper #userName-value")
    PAGES = (By.CSS_SELECTOR, "#pages-wrapper #userName-value")
    DESCRIPTION = (By.CSS_SELECTOR, "#description-wrapper #userName-value")
    WEBSITE = (By.CSS_SELECTOR, "#website-wrapper #userName-value")
    ADD_TO_COLLECTION = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    PROFILE = (By.LINK_TEXT, "Profile")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_isbn(self):
        ISBN_value = self.wait.until(EC.visibility_of_element_located(self.ISBN)).text
        return ISBN_value

    def get_title(self):

        title_value = self.driver.find_element(*self.TITLE).text
        return title_value

    def get_subtitle(self):

        subtitle_value = self.driver.find_element(*self.SUBTITLE).text
        return subtitle_value

    def get_author(self):

        author_value = self.driver.find_element(*self.AUTHOR).text
        return author_value

    def get_publisher(self):

        publisher_value = self.driver.find_element(*self.PUBLISHER).text
        return publisher_value

    def get_pages(self):

        page_value = self.driver.find_element(*self.PAGES).text
        return page_value

    def get_description(self):

        description_value = self.driver.find_element(*self.DESCRIPTION).text
        return description_value

    def get_website(self):

        website_value = self.driver.find_element(*self.WEBSITE).text
        return website_value

    def add_to_collection(self):

        buttons = self.wait.until(EC.presence_of_all_elements_located((self.ADD_TO_COLLECTION)))
        add_button = buttons[1]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_button)
        self.driver.execute_script("arguments[0].click();",add_button)
        alert = self.wait.until(EC.alert_is_present())
        assert "Book added" in alert.text or "already present" in alert.text
        alert.accept()

    def go_to_profile(self):
        # self.wait.until(EC.element_to_be_clickable(self.PROFILE)).click()

        self.driver.get("https://demoqa.com/profile")