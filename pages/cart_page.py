from pages.base_page import BasePage
from selenium.webdriver.common.by import By

cart_button = (By.XPATH, "//a[@id='js_topCart']")
all_items = (By.CLASS_NAME, "tit")
delete_item_from_cart = (By.XPATH, "//ul[1]//li[3]//p[1]//a[2]")
alert_delete = (By.XPATH, "//a[normalize-space()='Delete']")


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        self.driver.get("https://cart.zaful.com/zfie/m-flow-a-cart_empty.htm")

    def open_cart(self):
        return self.find_element(cart_button)

    def all_cart_items(self):
        return self.find_elements(all_items)

    def delete_item_from_cart(self):
        return self.find_element(delete_item_from_cart)

    def accept_deletion(self):
        return self.find_element(alert_delete)