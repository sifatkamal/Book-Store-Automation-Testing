# Book-Store-Automation-Testing

## Project Overview
This project contains Selenium WebDriver automation tests for the DemoQA Book Store application using Python and Selenium WebDriver.

## Tech Stack
- *[Python](https://www.python.org/)* as the Programming Language
- *[Selenium Webdriver](https://www.selenium.dev/)* as the web automation framework
- *[Google Chrome](https://www.google.com/chrome/)* as the web browser
- *[Visual Studio Code](https://code.visualstudio.com/)* as the IDE

## How to Run
- Clone this project
```
git clone https://github.com/sifatkamal/hrm-automation-testing.git
```

- Download and Install [Python](https://www.python.org/)

- Install Selenium
```
pip install selenium
```
- Install Pytest
```
pip install selenium pytest
```
- Run the script
```
python -m pytest tests/test_book_details.py -v
```


## Project Structure
```text
├── pages/
│   ├── login_page.py
│   ├── book_store_page.py
│   ├── book_details_page.py
│   └── profile_page.py
│
├── tests/
│   └── test_book_details.py
│
└── README.md
