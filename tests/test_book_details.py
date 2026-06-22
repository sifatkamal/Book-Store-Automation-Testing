from selenium import webdriver
from pages.book_store_page import BookStorePage
from pages.book_details_page import BookDetailsPage
from pages.login_page import LoginPage
from pages.profilePage import ProfilePage

def test_book_details():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        book_store = BookStorePage(driver)
        details = BookDetailsPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        login_page.open()
        login_page.login("user321", "User@321#")
        login_page.go_to_book_store()

        book_store.search_book("Git Pocket Guide")

        assert book_store.get_row_count() == 1

        title = book_store.get_book_title()

        assert title == "Git Pocket Guide"

        book_store.open_book()

        assert details.get_isbn() != ""
        assert details.get_title() == title
        assert details.get_subtitle() != ""
        assert details.get_author() != ""
        assert details.get_publisher() != ""
        assert details.get_pages() != ""
        assert details.get_description() != ""
        assert details.get_website() != ""

        details.add_to_collection()
        details.go_to_profile()
        assert profile_page.is_book_present("Git Pocket Guide")

    finally:
        driver.quit()