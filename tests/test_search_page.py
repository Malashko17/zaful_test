import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.clothing_page import ClothingPage


@allure.feature("Search")
@allure.description('Check broken search input')
@allure.title("error search input")
def test_error_search_input(driver):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    with allure.step("Open search and input error text"):
        home_page = HomePage(driver)
        home_page.search_field().click()
        home_page.search_field_input().send_keys("javascript:;")
        home_page.start_search().click()
    WebDriverWait(driver, 5).until(EC.visibility_of(home_page.search_error()))
    with allure.step("Checking correct page error"):
        assert home_page.search_error().text == "403 ERROR"


@allure.feature("Search")
@allure.description('Check wrong search input')
@allure.title("Wrong search input")
def test_wrong_search_input(driver):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    with allure.step("Open search and input wrong text"):
        home_page = HomePage(driver)
        home_page.search_field().click()
        wrong_text = "wdqewqeqsda"
        home_page.search_field_input().send_keys(wrong_text)
        home_page.start_search().click()
    with allure.step("Checking search result"):
        assert wrong_text + " did not match any products" in home_page.wrong_search().text


@allure.feature("Search")
@allure.description('Check correct search result')
@allure.title("Search")
def test_search(driver):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    home_page = HomePage(driver)
    with allure.step("Open search and input item 'cargo'"):
        home_page.search_field().click()
        search_text = "cargo"
        home_page.search_field_input().send_keys(search_text)
        home_page.start_search().click()
        correct_result = 0
    with allure.step("Checking correct search results"):
        for i in range(len(home_page.all_searched_items())):
            if search_text in home_page.all_searched_items()[i].text.lower():
                correct_result += 1
        assert correct_result/len(home_page.all_searched_items()) > 0.9

