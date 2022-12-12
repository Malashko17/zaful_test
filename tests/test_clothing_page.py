import allure
from selenium.webdriver import ActionChains
from pages.clothing_page import ClothingPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@allure.feature("Clothing Page")
@allure.description('Checking that items with discount is available')
@allure.title("Discount availability")
def test_discount_availability(driver):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    with allure.step("Checking that discount item is available"):
        assert len(clothing_page.all_items_sale()) > 0


@allure.feature("Clothing Page")
@allure.description('Checking correct slider filter')
@allure.title("Price slider")
def test_price_slider(driver):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    with allure.step("Choose slider borders and accept them"):
        clothing_page.price_range_button().click()
        low_price_border = 9
        upper_price_border = 20
        ActionChains(driver).drag_and_drop_by_offset(clothing_page.first_slider(), low_price_border * 1.8, 0). \
            drag_and_drop_by_offset(clothing_page.second_slider(), -(100 - upper_price_border) * 1.8, 0). \
            perform()
        driver.execute_script("arguments[0].click()", clothing_page.apply_price_slider())

    with allure.step("Checking that item prices is located between borders"):
        price_slider_result = False
        for item in clothing_page.all_items_price():
            if upper_price_border > float(item.text[:-1].replace(',', '.')) > low_price_border:
                price_slider_result = True
        assert price_slider_result


@allure.feature("Clothing Page")
@allure.description('Checking view items 120')
@allure.title("View items 120")
def test_view_items_120(driver):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    with allure.step("Click 120 items view"):
        clothing_page.view_120().click()
    try:
        WebDriverWait(driver, 5).until(
            EC.staleness_of((clothing_page.all_items_price()[119]))
        )
    except TimeoutException:
        pass
    with allure.step("Checking correct view items"):
        assert len(clothing_page.all_items_price()) == 120


@allure.feature("Clothing Page")
@allure.description('Checking view items 60')
@allure.title("View items 60")
def test_view_items_60(driver):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    with allure.step("Click 60 items view"):
        clothing_page.view_60().click()
    with allure.step("Checking correct view items"):
        assert len(clothing_page.all_items_price()) == 60


@allure.feature("Clothing Page")
@allure.description('Checking filter with chosen "shirts"')
@allure.title("Filter shirts")
def test_filter_shirts(driver):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    with allure.step("Choose shirts on page"):
        ActionChains(driver).click(clothing_page.categories_button()).click(clothing_page.tops_button()).perform()
        clothing_page.shirts().click()
    items_is_shirts = 0
    with allure.step("Checking correct filter result"):
        for item in clothing_page.all_items_titles():
            if "shirt" in item.text.lower():
                items_is_shirts += 1
        assert items_is_shirts / len(clothing_page.all_items_titles()) > 0.9


@allure.feature("Clothing Page")
@allure.description('Checking filter with many parameters')
@allure.title("Filter shorts, color, size")
def test_filter_shorts_color_size(driver):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    with allure.step("Choose different filter parameters"):
        ActionChains(driver).click(clothing_page.categories_button()).click(clothing_page.bottoms_button()).perform()
        clothing_page.shorts().click()
        ActionChains(driver).click(clothing_page.size_choose()).click(clothing_page.size_m()).perform()
        ActionChains(driver).click(clothing_page.choose_color()).click(clothing_page.choose_black_color()).perform()
    black_m_shorts = 0
    with allure.step("Checking correct filter result"):
        for item in clothing_page.all_items_titles():
            if "shorts" and "black m" in item.text.lower():
                black_m_shorts += 1
        assert black_m_shorts == len(clothing_page.all_items_titles())


@allure.feature("Clothing Page")
@allure.description('Checking filter high to low prices')
@allure.title("Filter from high to low")
def test_filter_from_high_to_low(driver):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    ActionChains(driver).click(clothing_page.sort_button()).click(clothing_page.sort_high_to_low()).perform()
    correct_sort_result = True
    with allure.step("Algorithm which checking correct result filter results"):
        for i in (range(len(clothing_page.all_prices())-1)):
            if float(clothing_page.all_prices()[i].text[:-1].replace(',', '.')) >= float \
                        (clothing_page.all_prices()[i+1].text[:-1].replace(',', '.')):
                correct_sort_result = True
            else:
                correct_sort_result = False
                break
    assert correct_sort_result


@allure.feature("Clothing Page")
@allure.description('Checking clear filter button')
@allure.title("Clear filter")
def test_clear_filter(driver):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    with allure.step("Choose different filter parameters"):
        ActionChains(driver).click(clothing_page.categories_button()).click(clothing_page.bottoms_button()).perform()
        clothing_page.shorts().click()
        ActionChains(driver).click(clothing_page.size_choose()).click(clothing_page.size_m()).perform()
        ActionChains(driver).click(clothing_page.choose_color()).click(clothing_page.choose_black_color()).perform()
    black_m_shorts = 0
    for item in clothing_page.all_items_titles():
        if "shorts" and "black m" in item.text.lower():
            black_m_shorts += 1
    with allure.step("Checking result clear filter button"):
        clothing_page.clear_all_button().click()
        assert len(clothing_page.all_items_titles()) > black_m_shorts


@allure.feature("Clothing Page")
@allure.description('Checking currency change')
@allure.title("Currency change")
def test_currency_change(driver):
    clothing_page = ClothingPage(driver)
    with allure.step("Open clothing page"):
        clothing_page.open_page()
    with allure.step("Choose other currency:"):
        ActionChains(driver).move_to_element(clothing_page.currency_icon()).click(clothing_page.choose_currency()). \
            click(clothing_page.choose_dollar()).click(clothing_page.update_pref()).perform()
    correct_item_currency = 0
    with allure.step("Checking currency changes"):
        for item in clothing_page.all_prices():
            if "$" in item.text:
                correct_item_currency += 1
        assert correct_item_currency == len(clothing_page.all_prices())
