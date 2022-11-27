from selenium.webdriver import Edge
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class Browser:

    def __init__(self):
        service = EdgeService(EdgeChromiumDriverManager().install())
        self.driver = Edge(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def get_current_url(self):
        return self.driver.current_url

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
