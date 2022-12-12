from time import sleep
from selenium.webdriver import ActionChains
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.clothing_page import ClothingPage


def test_cookie_window(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.close_ads()
    driver.execute_script("window.scrollTo(0, 500)")
    home_page.cookie_button().click()
    assert home_page.agree_cookie_button().is_enabled()


def test_support_window(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.close_ads()
    driver.execute_script("window.scrollTo(0, 500)")
    home_page.support_button().click()
    driver.switch_to.window((driver.window_handles[1]))
    assert home_page.support_text().text == "Support Center"


def test_warranty_window(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.close_ads()
    driver.execute_script("window.scrollTo(0, 500)")
    ActionChains(driver).move_to_element(home_page.warranty_icon()).click(home_page.return_warranty()).perform()
    assert "return policy".upper() in home_page.return_policy().text


def test_sidebar_buttons_clickable(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.close_ads()
    sidebar_buttons = [home_page.support_button().get_attribute('href'),
                       home_page.cookie_button().get_attribute('href'), home_page.survey_button().get_attribute('href'),
                       home_page.warranty_icon().get_attribute('href')]
    driver.execute_script("window.scrollTo(0, 500)")
    clickability = True
    for href in sidebar_buttons:
        if href is None:
            clickability = False
    assert clickability
    

def test_satisfaction_survey(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.close_ads()
    driver.execute_script("window.scrollTo(0, 500)")
    home_page.survey_button().click()
    assert "Survey" in home_page.satisfaction_survey().text


def test_add_item_to_favorite_list(driver, login):
    home_page = HomePage(driver)
    clothing_page = ClothingPage(driver)
    clothing_page.open_page()
    WebDriverWait(driver, 15).until(EC.visibility_of(home_page.open_cart()))
    home_page.add_to_favorite()[1].click()
    first_item_in_favorite_list = home_page.all_items_links()[1].text
    home_page.open_favorite_list().click()
    assert home_page.all_favorite_items()[0].text in first_item_in_favorite_list


def test_delete_item_from_favorite_list(driver, login):
    clothing_page = ClothingPage(driver)
    clothing_page.open_page()
    home_page = HomePage(driver)
    home_page.add_to_favorite()[1].click()
    first_item_in_favorite_list = home_page.all_items_links()[1].text
    home_page.open_favorite_list().click()
    home_page.delete_favorite_item()[0].click()
    home_page.confirm_deleting_from_favorite().click()
    assert first_item_in_favorite_list not in home_page.all_favorite_items()[0].text
