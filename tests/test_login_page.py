from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from selenium.webdriver import ActionChains
import settings


def test_login_passed(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.email_field().click()
    login_page.email_field().send_keys(settings.EMAIL)
    login_page.password_field().send_keys(settings.PASSWORD)
    login_page.sign_in().click()
    WebDriverWait(driver, 20).until(EC.staleness_of(login_page.account_icon()))
    ActionChains(driver).move_to_element(login_page.account_icon()).click(login_page.my_account()).perform()
    assert login_page.check_sign_in()


def test_wrong_email_format(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.email_field().send_keys("pashaqap.mail.ru")
    login_page.click_text()
    assert login_page.email_alert().text == "Please enter a valid email address."


def test_wrong_email_or_password(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.email_field().send_keys("pashaqap@mail.com")
    login_page.password_field().send_keys("testqap10")
    login_page.sign_in().click()
    assert login_page.wrong_auth_data().text == "Your account name or password is incorrect."


def test_empty_auth_fields(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.email_field().send_keys("")
    login_page.password_field().send_keys("")
    login_page.sign_in().click()
    assert login_page.password_alert().text == "Please provide a password" and \
           login_page.email_alert().text == "Please enter a valid email address."


def test_password_recovery_button(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.password_recovery().click()
    assert "reset password" in login_page.page_title_reset_password().text


def test_google_link(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.open_google_auth()
    driver.switch_to.window(driver.window_handles[1])
    assert login_page.google_text() == 'Войдите в аккаунт Google'


def test_facebook_link(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.open_facebook_link().click()
    driver.switch_to.window(driver.window_handles[1])
    assert login_page.facebook_text().text == "Facebook"