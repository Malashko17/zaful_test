from pages.base_page import BasePage
from selenium.webdriver.common.by import By

all_clothes_item_sale = (By.CLASS_NAME, 'color_tag')
all_clothes_item_price = (By.CLASS_NAME, 'shop-price')
price_range = (By.XPATH, "//dt[text()='Price Range']")
price_slider1 = (By.XPATH, "//div[@class='noUi-handle noUi-handle-lower']")
price_slider2 = (By.XPATH, "//div[@class='noUi-handle noUi-handle-upper']")
apply_price_slider = (By.CLASS_NAME, "start-price-filter")
clear_price = (By.LINK_TEXT, "Clear")
count_items_view_120 = (By.LINK_TEXT, "120")
count_items_view_60 = (By.LINK_TEXT, "60")
all_clothes_titles = (By.CLASS_NAME, "js_list_title")
categories = (By.XPATH, "//dt[text()='Categories']")
sort = (By.XPATH, "//dt[@class='fsb']")
sort_high_to_low = (By.XPATH, "//a[normalize-space()='Price High To Low']")
tops = (By.XPATH, "//div[@class='menu']//a[contains(text(),'Tops')]")
bottoms = (By.XPATH, "//div[@class='menu']//a[contains(text(),'Bottoms')]")
shorts = (By.XPATH, "//li[@data-name='Shorts']")
shirts = (By.XPATH, "//li[@data-name='Shirts']")
size_choose = (By.XPATH, "//dt[text()='Size']")
choose_m_size = (By.XPATH, "//a[@class='logsss_event_cl'][normalize-space()='M']")
color_choose = (By.XPATH, "//dt[text()='Color']")
choose_black_color = (By.XPATH, "//a[@title='Black']//span[@class='color-item']")
clear_all_button = (By.XPATH, "//a[normalize-space()='Clear All']")
currency_icon = (By.CLASS_NAME, "has_arrow")
currency_choose_button = (By.CLASS_NAME, "header-current-currency")
choose_dollar_currency = (By.CSS_SELECTOR, "a[data-icon='$']")
update_preferences = (By.CLASS_NAME, "link-update-preferences")
all_prices = (By.CLASS_NAME, 'js_list_shopprice')


class ClothingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        self.driver.get("https://eur.zaful.com/men-e_118/")

    def all_items_sale(self):
        return self.find_elements(all_clothes_item_sale)

    def all_items_price(self):
        return self.find_elements(all_clothes_item_price)

    def all_items_titles(self):
        return self.find_elements(all_clothes_titles)

    def price_range_button(self):
        return self.find_element(price_range)

    def first_slider(self):
        return self.find_element(price_slider1)

    def second_slider(self):
        return self.find_element(price_slider2)

    def apply_price_slider(self):
        return self.find_element(apply_price_slider)

    def clear_price(self):
        return self.find_element(clear_price)

    def view_120(self):
        return self.find_element(count_items_view_120)

    def view_60(self):
        return self.find_element(count_items_view_60)

    def categories_button(self):
        return self.find_element(categories)

    def sort_button(self):
        return self.find_element(sort)

    def sort_high_to_low(self):
        return self.find_element(sort_high_to_low)

    def shirts(self):
        return self.find_element(shirts)

    def tops_button(self):
        return self.find_element(tops)

    def bottoms_button(self):
        return self.find_element(bottoms)

    def shorts(self):
        return self.find_element(shorts)

    def size_choose(self):
        return self.find_element(size_choose)

    def size_m(self):
        return self.find_element(choose_m_size)

    def choose_color(self):
        return self.find_element(color_choose)

    def choose_black_color(self):
        return self.find_element(choose_black_color)

    def clear_all_button(self):
        return self.find_element(clear_all_button)

    def currency_icon(self):
        return self.find_element(currency_icon)

    def choose_currency(self):
        return self.find_element(currency_choose_button)

    def choose_dollar(self):
        return self.find_element(choose_dollar_currency)

    def update_pref(self):
        return self.find_element(update_preferences)

    def all_prices(self):
        return self.find_elements(all_prices)