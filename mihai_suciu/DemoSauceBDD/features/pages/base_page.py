class BasePage:

    URL = ''

    def __init__(self, browser):
        self.driver = browser.driver

    def get_page(self):
        self.driver.get(self.URL)
