from selenium.webdriver import ActionChains
from pages.clothing_page import ClothingPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_discount_availability(driver):
    clothing_page = ClothingPage(driver)
    clothing_page.open_page()
    assert len(clothing_page.all_items_sale()) > 0


def test_price_slider(driver):
    clothing_page = ClothingPage(driver)
    clothing_page.open_page()
    clothing_page.price_range_button().click()
    low_price_border = 9
    upper_price_border = 20
    ActionChains(driver).drag_and_drop_by_offset(clothing_page.first_slider(), low_price_border * 1.8, 0). \
        drag_and_drop_by_offset(clothing_page.second_slider(), -(100 - upper_price_border) * 1.8, 0). \
        perform()
    driver.execute_script("arguments[0].click()", clothing_page.apply_price_slider())
    price_slider_result = False
    for item in clothing_page.all_items_price():
        if upper_price_border > float(item.text[:-1].replace(',', '.')) > low_price_border:
            price_slider_result = True
    assert price_slider_result


def test_view_items_120(driver):
    clothing_page = ClothingPage(driver)
    clothing_page.open_page()
    clothing_page.view_120().click()
    try:
        WebDriverWait(driver, 5).until(
            EC.staleness_of((clothing_page.all_items_price()[119]))
        )
    except TimeoutException:
        pass

    assert len(clothing_page.all_items_price()) == 120


def test_view_items_60(driver):
    clothing_page = ClothingPage(driver)
    clothing_page.open_page()
    clothing_page.view_60().click()
    assert len(clothing_page.all_items_price()) == 60


def test_filter_shirts(driver):
    clothing_page = ClothingPage(driver)
    clothing_page.open_page()
    # driver.implicitly_wait(10)
    ActionChains(driver).click(clothing_page.categories_button()).click(clothing_page.tops_button()).perform()
    clothing_page.shirts().click()
    items_is_shirts = 0
    for item in clothing_page.all_items_titles():
        if "shirt" in item.text.lower():
            items_is_shirts += 1
    assert items_is_shirts / len(clothing_page.all_items_titles()) > 0.9


def test_filter_shorts_color_size(driver):
    clothing_page = ClothingPage(driver)
    clothing_page.open_page()
    ActionChains(driver).click(clothing_page.categories_button()).click(clothing_page.bottoms_button()).perform()
    clothing_page.shorts().click()
    ActionChains(driver).click(clothing_page.size_choose()).click(clothing_page.size_m()).perform()
    ActionChains(driver).click(clothing_page.choose_color()).click(clothing_page.choose_black_color()).perform()
    black_m_shorts = 0
    for item in clothing_page.all_items_titles():
        if "shorts" and "black m" in item.text.lower():
            black_m_shorts += 1
    assert black_m_shorts == len(clothing_page.all_items_titles())


def test_clear_filter(driver):
    clothing_page = ClothingPage(driver)
    clothing_page.open_page()
    ActionChains(driver).click(clothing_page.categories_button()).click(clothing_page.bottoms_button()).perform()
    clothing_page.shorts().click()
    ActionChains(driver).click(clothing_page.size_choose()).click(clothing_page.size_m()).perform()
    ActionChains(driver).click(clothing_page.choose_color()).click(clothing_page.choose_black_color()).perform()
    black_m_shorts = 0
    for item in clothing_page.all_items_titles():
        if "shorts" and "black m" in item.text.lower():
            black_m_shorts += 1
    clothing_page.clear_all_button().click()
    assert len(clothing_page.all_items_titles()) > black_m_shorts



