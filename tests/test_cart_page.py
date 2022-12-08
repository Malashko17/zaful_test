from pages.base_page import BasePage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from time import sleep


def test_check_empty_cart(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.close_ads()
    home_page.open_cart()
    home_page.cart_empty().is_displayed()
    assert home_page.cart_empty().text == "Your shopping bag is empty."


def test_continue_shopping_from_cart(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.close_ads()
    home_page.open_cart()
    home_page.continue_shopping_button()




