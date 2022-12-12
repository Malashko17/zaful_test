import allure
from selenium.webdriver import ActionChains
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.clothing_page import ClothingPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@allure.feature("Cart Page")
@allure.description('Checking empty cart without authorization')
@allure.title("Check empty cart")
def test_check_empty_cart(driver):
    clothing_page = ClothingPage(driver)
    with allure.step("Open home page"):
        clothing_page.open_page()
    home_page = HomePage(driver)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(home_page.open_cart()))
    with allure.step("Open cart"):
        home_page.open_cart().click()
    with allure.step("Check that cart is empty"):
        home_page.empty_cart_without_sign_in().is_displayed()
    assert home_page.empty_cart_without_sign_in().text == "You can sign in to check your shopping bag!"


@allure.feature("Cart Page")
@allure.description('Adding item to cart')
@allure.title("Add to cart")
def test_add_to_cart(driver, login):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    home_page = HomePage(driver)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(home_page.all_items_links()[2]))
    item_which_add_to_cart = home_page.all_items_links()[2].text
    with allure.step("Add item to cart"):
        ActionChains(driver).move_to_element(home_page.all_clothes_img()[2]).\
            click(home_page.all_add_to_cart_buttons()[2]).perform()
        home_page.quick_choose_size().click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(home_page.open_cart()))
    with allure.step("Open cart"):
        home_page.open_cart().click()
    cart_page = CartPage(driver)
    with allure.step("Check added item in cart"):
        assert cart_page.all_cart_items()[0].text in item_which_add_to_cart


@allure.feature("Cart Page")
@allure.description('Checking delete button in cart')
@allure.title("Clear added item from cart")
def test_clear_added_item_from_cart(driver, login):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    home_page = HomePage(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(home_page.all_items_links()[1]))
    item_which_add_to_cart = home_page.all_items_links()[4].text
    with allure.step("Add item to cart"):
        home_page.all_items_links()[4].click()
        home_page.add_to_bag().click()
    cart_page = CartPage(driver)
    with allure.step("Open cart"):
        cart_page.open_cart().click()
    with allure.step("Delete item from cart"):
        cart_page.delete_item_from_cart().click()
        cart_page.accept_deletion().click()
    try:
        WebDriverWait(driver, 5).until(EC.staleness_of(cart_page.all_cart_items()[0]))
    except TimeoutException:
        pass
    with allure.step("Checking that item is deleted"):
        assert cart_page.all_cart_items()[0].text not in item_which_add_to_cart


@allure.feature("Cart Page")
@allure.description('Checking select all and delete')
@allure.title("Delete all cart items")
def test_delete_all_cart_items(driver, login):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    home_page = HomePage(driver)
    with allure.step("Add a few items to cart"):
        ActionChains(driver).move_to_element(home_page.all_clothes_img()[3]).click(home_page.all_add_to_cart_buttons()[3]).\
            perform()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(home_page.quick_choose_size()))
        home_page.quick_choose_size().click()
        ActionChains(driver).move_to_element(home_page.all_clothes_img()[4]).click(home_page.all_add_to_cart_buttons()[4]).\
            perform()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(home_page.quick_choose_size()))
        home_page.quick_choose_size().click()
    with allure.step("Open cart"):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(home_page.open_cart()))
        home_page.open_cart().click()
    with allure.step("Delete all items from cart"):
        home_page.delete_all_from_cart().click()
        cart_page = CartPage(driver)
        cart_page.accept_deletion().click()
    with allure.step("Checking that cart is empty"):
        assert home_page.cart_empty().text == "Your shopping bag is empty."

