from pages.base_page import BasePage
from selenium.webdriver.common.by import By

cart_button = (By.XPATH, "//i[@class='bag-icon']")
ads = (By.LINK_TEXT, "No, thanks")
cart_empty = (By.XPATH, "//h4[text()='Your shopping bag is empty.']")
continue_shopping_button = (By.CLASS_NAME, "sign_btn")
my_account = (By.XPATH, '//*[@id="header_account_list_user"]/li[1]/a')
extra_20_off = (By.XPATH, '//p[text()="Extra 20% OFF"]')
cookie_button = (By.CLASS_NAME, 'sidebar-linkto-cookie')
agree_cookie_button = (By.XPATH, '//span[text()="Agree"]')
support_button = (By.CLASS_NAME, 'link-support-icon')
support_text = (By.XPATH, '//span[text()="Support Center"]')
warranty_icon = (By.XPATH, '//*[@id="js_allFixedCtn"]/div[2]/div[3]/div')
return_warranty = (By.XPATH, '//a[text()="Return Warranty"]')
return_policy = (By.XPATH, '//h1[text()="ZAFUL RETURN POLICY"]')
satisfaction_survey = (By.CLASS_NAME, 'title')
survey_icon = (By.CLASS_NAME, 'survey-monkey-icon')
clothes_button = (By.XPATH, "//span[normalize-space()='CLOTHING']")
men_button = (By.XPATH, "//span[normalize-space()='Men']")
all_clothes_links = (By.CLASS_NAME, 'js_list_title')
add_to_bag = (By.CLASS_NAME, 'js-normal-text')
add_to_favorite = (By.CLASS_NAME, 'like-icon')
favorite_list = (By.CLASS_NAME, 'header-favorite')
all_favorite_items = (By.CLASS_NAME, 'pro_name')
delete_from_favorite_items = (By.CLASS_NAME, 'fav_delete')
confirm_deleting_from_favorite = (By.CLASS_NAME, 'js-comfirm')
search_field = (By.XPATH, "//input[@id='js-search-input-box']")


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
        return self.find_element(continue_shopping_button)

    def sign_in_success(self):
        return self.find_element(my_account).click()

    def click_extra_off(self):
        return self.find_element(extra_20_off).click()

    def cookie_button(self):
        return self.find_element(cookie_button)

    def agree_cookie_button(self):
        return self.find_element(agree_cookie_button)

    def support_button(self):
        return self.find_element(support_button)

    def support_text(self):
        return self.find_element(support_text)

    def warranty_icon(self):
        return self.find_element(warranty_icon)

    def return_warranty(self):
        return self.find_element(return_warranty)

    def return_policy(self):
        return self.find_element(return_policy)

    def survey_button(self):
        return self.find_element(survey_icon)

    def satisfaction_survey(self):
        return self.find_element(satisfaction_survey)

    def clothes(self):
        return self.find_element(clothes_button)

    def men(self):
        return self.find_element(men_button)

    def all_items_links(self):
        return self.find_elements(all_clothes_links)

    def add_to_bag(self):
        return self.find_element(add_to_bag)

    def add_to_favorite(self):
        return self.find_elements(add_to_favorite)

    def open_favorite_list(self):
        return self.find_element(favorite_list)

    def all_favorite_items(self):
        return self.find_elements(all_favorite_items)

    def delete_favorite_item(self):
        return self.find_elements(delete_from_favorite_items)

    def confirm_deleting_from_favorite(self):
        return self.find_element(confirm_deleting_from_favorite)

    def search_field(self):
        return self.find_element(search_field)
