from pages.cart_page import CartPage
from pages.home_page import HomePage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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


def test_add_to_cart(driver, login):
    home_page = HomePage(driver)
    WebDriverWait(driver, 5).until(
        EC.staleness_of(home_page.clothes())
    )
    home_page.men().click()
    home_page.clothes().click()
    sleep(5)
    item_which_add_to_cart = home_page.all_items_links()[2].text
    home_page.all_items_links()[2].click()
    home_page.add_to_bag().click()
    sleep(5)
    cart_page = CartPage(driver)
    cart_page.open_cart().click()
    assert cart_page.all_cart_items()[0].text in item_which_add_to_cart


def test_clear_added_item_from_cart(driver, login):
    home_page = HomePage(driver)
    WebDriverWait(driver, 5).until(
        EC.staleness_of(home_page.clothes())
    )
    home_page.men().click()
    home_page.clothes().click()

    try:
        WebDriverWait(driver, 10).until(EC.staleness_of(home_page.all_items_links()[1]))
    except TimeoutException:
        pass
    item_which_add_to_cart = home_page.all_items_links()[1].text
    home_page.all_items_links()[1].click()
    home_page.add_to_bag().click()
    cart_page = CartPage(driver)
    cart_page.open_cart().click()
    cart_page.delete_item_from_cart().click()
    cart_page.accept_deletion().click()
    try:
        WebDriverWait(driver, 5).until(EC.staleness_of(cart_page.all_cart_items()[0]))
    except TimeoutException:
        pass
    assert cart_page.all_cart_items()[0].text not in item_which_add_to_cart



