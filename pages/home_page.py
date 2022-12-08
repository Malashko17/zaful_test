from pages.base_page import BasePage
from selenium.webdriver.common.by import By

cart_button = (By.CLASS_NAME, "bag-icon")
ads = (By.LINK_TEXT, "No, thanks")
cart_empty = (By.XPATH, "//h4[text()='Your shopping bag is empty.']")
continue_shoping_button = (By.CLASS_NAME, "sign_btn")
my_account = (By.XPATH, '//*[@id="header_account_list_user"]/li[1]/a')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        self.driver.get("https://eur.zaful.com/")

    def open_cart(self):
        self.find_element(cart_button).click()

    def close_ads(self):
        self.find_element(ads).click()

    def cart_empty(self):
        return self.find_element(cart_empty)

    def continue_shopping_button(self):
        return self.find_element(continue_shoping_button)

    def sign_in_success(self):
        return self.find_element(my_account).click()


# home_page_url = "https://gde.by"
#
# profile_button = (By.CLASS_NAME, "cabinet-btn")
# email_input = (By.ID, "LoginForm_email")
# password = (By.ID, "LoginForm_password")
# login_button = (By.NAME, "yt0")
# logout = (By.LINK_TEXT, 'Выйти')
# wrong_login_error = (By.CLASS_NAME, "error-text")
#
#
# logo = (By.CSS_SELECTOR, '[alt="Gde.by доска объявлений Беларуси"]')
# all_categories_button = (By.CLASS_NAME, "text1")
# all_categories = (By.ID, "show-cat")
# vip_ads = (By.XPATH, "//ul[@class='product-list']/li[@class='vip']")
#
#
# class HomePage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     def open_home_page(self):
#         self.driver.get(home_page_url)
#
#     def all_ads_on_home_page(self):
#         return self.find_elements(all_ads_on_home_page)
#     # def open_login_page(self):
#     #     self.find_element(profile_button).click()
#     #
#     # def login_failed(self):
#     #     return self.find_element(wrong_login_error).is_displayed()
#     #
#     # def input_login(self):
#     #     self.find_element(email_input).send_keys("pashaqap@mail.ru")
#     #
#     # def input_password(self):
#     #     self.find_element(password).send_keys("Testqap09")
#     #
#     # def logout_is_displayed(self):
#     #     return self.find_element(logout).text --> loginPage
#
#     def logo_is_displayed(self):
#         return self.find_element(logo).is_displayed()
#
#     def expand_all_categories(self):
#         self.find_element(all_categories).click()
#
#     def all_categories_is_displayed(self):
#         return self.find_element(all_categories).is_displayed()
