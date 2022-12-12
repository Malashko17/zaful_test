import allure
from selenium.webdriver import ActionChains
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.clothing_page import ClothingPage


@allure.feature("Home Page")
@allure.description('Checking cookie window is displayed')
@allure.title("Cookie window")
def test_cookie_window(driver):
    home_page = HomePage(driver)
    with allure.step("Open home page"):
        home_page.open_page()
        home_page.close_ads()
    driver.execute_script("window.scrollTo(0, 500)")
    with allure.step("Click cookie button"):
        home_page.cookie_button().click()
    assert home_page.agree_cookie_button().is_enabled()


@allure.feature("Home Page")
@allure.description('Checking support window is displayed')
@allure.title("Support window")
def test_support_window(driver):
    home_page = HomePage(driver)
    with allure.step("Open home page"):
        home_page.open_page()
        home_page.close_ads()
    driver.execute_script("window.scrollTo(0, 500)")
    with allure.step("Click support button"):
        home_page.support_button().click()
    driver.switch_to.window((driver.window_handles[1]))
    assert home_page.support_text().text == "Support Center"


@allure.feature("Home Page")
@allure.description('Checking warranty window is displayed')
@allure.title("Warranty window")
def test_warranty_window(driver):
    home_page = HomePage(driver)
    with allure.step("Open home page"):
        home_page.open_page()
        home_page.close_ads()
    driver.execute_script("window.scrollTo(0, 500)")
    with allure.step("Click warranty button"):
        ActionChains(driver).move_to_element(home_page.warranty_icon()).click(home_page.return_warranty()).perform()
    assert "return policy".upper() in home_page.return_policy().text


@allure.feature("Home Page")
@allure.description('Checking survey window is displayed')
@allure.title("Satisfaction survey window")
def test_satisfaction_survey(driver):
    home_page = HomePage(driver)
    with allure.step("Open home page"):
        home_page.open_page()
        home_page.close_ads()
    driver.execute_script("window.scrollTo(0, 500)")
    with allure.step("Click survey button"):
        home_page.survey_button().click()
    assert "Survey" in home_page.satisfaction_survey().text


@allure.feature("Home Page")
@allure.description('Checking all sidebar buttons are clickable')
@allure.title("Sidebar buttons clickable")
def test_sidebar_buttons_clickable(driver):
    home_page = HomePage(driver)
    with allure.step("Open home page"):
        home_page.open_page()
        home_page.close_ads()
    sidebar_buttons = [home_page.support_button().get_attribute('href'),
                       home_page.cookie_button().get_attribute('href'), home_page.survey_button().get_attribute('href'),
                       home_page.warranty_icon().get_attribute('href')]
    driver.execute_script("window.scrollTo(0, 500)")
    with allure.step("Checking all sidebar buttons are clickable"):
        clickability = True
        for href in sidebar_buttons:
            if href is None:
                clickability = False
        assert clickability


@allure.feature("Home Page")
@allure.description('Checking added item in favorite list')
@allure.title("Add item to favorite list")
def test_add_item_to_favorite_list(driver, login):
    home_page = HomePage(driver)
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    WebDriverWait(driver, 15).until(EC.visibility_of(home_page.open_cart()))
    with allure.step("Add second item to favorite list"):
        home_page.add_to_favorite()[1].click()
    first_item_in_favorite_list = home_page.all_items_links()[1].text
    with allure.step("Open favorite list"):
        home_page.open_favorite_list().click()
    with allure.step("Checking added item in favorite list"):
        assert home_page.all_favorite_items()[0].text in first_item_in_favorite_list


@allure.feature("Home Page")
@allure.description('Checking added item in favorite list is deleted')
@allure.title("Delete added item from favorite list")
def test_delete_item_from_favorite_list(driver, login):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    home_page = HomePage(driver)
    with allure.step("Add second item to favorite list"):
        home_page.add_to_favorite()[1].click()
    first_item_in_favorite_list = home_page.all_items_links()[1].text
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(home_page.open_favorite_list()))
    with allure.step("Open favorite list"):
        home_page.open_favorite_list().click()
    with allure.step("Delete item from favorite list and check it"):
        home_page.delete_favorite_item()[0].click()
        home_page.confirm_deleting_from_favorite().click()
        assert first_item_in_favorite_list not in home_page.all_favorite_items()[0].text
