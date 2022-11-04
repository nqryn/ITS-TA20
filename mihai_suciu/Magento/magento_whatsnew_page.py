import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class MagentoWhatsnewPageTestCase(unittest.TestCase):

    def setUp(self) -> None:
        service = EdgeService(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=service)
        self.driver.implicitly_wait(10)
        self.driver.get("https://magento.softwaretestingboard.com/what-is-new.html")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_yoga_collection_button(self):
        yoga_collection_img_button = self.driver.find_element(By.XPATH,
                                                              '//html/body/div[2]/'
                                                              'main/div[4]/div[1]/'
                                                              'div[1]/div[1]/a/img')
        yoga_collection_img_button.click()
        assert self.driver.current_url == "https://magento.softwaretestingboard.com/" \
                                          "collections/yoga-new.html", "URL Link Error"

    def test_shop_new_yoga(self):
        shop_new_yoga_button = self.driver.find_element(By.XPATH, '//span[@class="more button"]')
        shop_new_yoga_button.click()
        assert self.driver.current_url == "https://magento.softwaretestingboard.com/" \
                                          "collections/yoga-new.html", "URL Link Error"

    def test_whatever_day_brings(self):
        whatever_day_brings_button = self.driver.find_element(By.XPATH, '//*[@id="maincontent"]/'
                                                                        'div[4]/div[1]/div[1]/'
                                                                        'div[1]/div/a[1]/span/'
                                                                        'span[2]')
        whatever_day_brings_button.click()
        assert self.driver.current_url == "https://magento.softwaretestingboard.com/" \
                                          "collections/performance-new.html", "URL Link Error"

    def test_a_sense_of_renewal(self):
        a_sense_of_renewal_button = self.driver.find_element(By.XPATH, '//*[@id="maincontent"]/'
                                                                       'div[4]/div[1]/div[1]/'
                                                                       'div[1]/div/a[2]/span/'
                                                                       'span[2]')
        a_sense_of_renewal_button.click()
        assert self.driver.current_url == "https://magento.softwaretestingboard.com/" \
                                          "collections/eco-new.html", "URL Link Error"

    def test_phoebe_img_button(self):
        buttons_list = self.driver.find_elements(By.XPATH, '//img[@class="product-image-photo"]')
        buttons_list[0].click()
        current_url = self.driver.current_url
        assert "phoebe" in current_url, "URL Link Error"

    def test_gobi_img_button(self):
        buttons_list = self.driver.find_elements(By.XPATH, '//img[@class="product-image-photo"]')
        buttons_list[1].click()
        current_url = self.driver.current_url
        assert "gobi" in current_url, "URL Link Error"

    def test_stellar_img_button(self):
        buttons_list = self.driver.find_elements(By.XPATH, '//img[@class="product-image-photo"]')
        buttons_list[2].click()
        current_url = self.driver.current_url
        assert "stellar" in current_url, "URL Link Error"

    def test_zoltan_img_button(self):
        buttons_list = self.driver.find_elements(By.XPATH, '//img[@class="product-image-photo"]')
        buttons_list[3].click()
        current_url = self.driver.current_url
        assert "zoltan" in current_url, "URL Link Error"

    def test_phoebe_size_XS(self):
        phoebe_size_button = self.driver.find_element(By.XPATH, '//*[@id="option-label-size-143-item-166"]')
        phoebe_size_button.click()
        assert phoebe_size_button.is_enabled(), "Button selection error"

    def test_phoebe_size_S(self):
        phoebe_size_button = self.driver.find_element(By.XPATH, '//*[@id="option-label-size-143-item-167"]')
        phoebe_size_button.click()
        assert phoebe_size_button.is_enabled(), "Button selection error"

    def test_phoebe_size_M(self):
        phoebe_size_button = self.driver.find_element(By.XPATH, '//*[@id="option-label-size-143-item-168"]')
        phoebe_size_button.click()
        assert phoebe_size_button.is_enabled(), "Button selection error"

    def test_phoebe_size_L(self):
        phoebe_size_button = self.driver.find_element(By.XPATH, '//*[@id="option-label-size-143-item-169"]')
        phoebe_size_button.click()
        assert phoebe_size_button.is_enabled(), "Button selection error"

    def test_phoebe_size_XL(self):
        phoebe_size_button = self.driver.find_element(By.XPATH, '//*[@id="option-label-size-143-item-170"]')
        phoebe_size_button.click()
        assert phoebe_size_button.is_enabled(), "Button selection error"

    def test_phoebe_gray(self):
        grey_button = self.driver.find_element(By.XPATH, '//*[@id="option-label-color-93-item-52"]')
        grey_button.click()
        assert grey_button.is_enabled(), "Button selection error"

    def test_phoebe_purple(self):
        grey_button = self.driver.find_element(By.XPATH, '//*[@id="option-label-color-93-item-57"]')
        grey_button.click()
        assert grey_button.is_enabled(), "Button selection error"

    def test_phoebe_white(self):
        grey_button = self.driver.find_element(By.XPATH, '//*[@id="option-label-color-93-item-59"]')
        grey_button.click()
        assert grey_button.is_enabled(), "Button selection error"
