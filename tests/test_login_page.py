import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from selenium.webdriver import ActionChains
import settings


@allure.feature("Login Page")
@allure.description('Check login passed')
@allure.title("Loging passed")
def test_login_passed(driver):
    login_page = LoginPage(driver)
    with allure.step("Open login page"):
        login_page.open_login_page()
    with allure.step("Enter email and password and submit"):
        login_page.email_field().click()
        login_page.email_field().send_keys(settings.EMAIL)
        login_page.password_field().send_keys(settings.PASSWORD)
        login_page.sign_in().click()
        WebDriverWait(driver, 20).until(EC.staleness_of(login_page.account_icon()))
        ActionChains(driver).move_to_element(login_page.account_icon()).click(login_page.my_account()).perform()
    with allure.step("Check success sign in"):
        assert login_page.check_sign_in()


@allure.feature("Login Page")
@allure.description('Check wrong login error')
@allure.title("Wrong email format")
def test_wrong_email_format(driver):
    login_page = LoginPage(driver)
    with allure.step("Open login page"):
        login_page.open_login_page()
    with allure.step("Input wrong format email"):
        login_page.email_field().send_keys("pashaqap.mail.ru")
        login_page.click_text()
    with allure.step('Check wrong login error'):
        assert login_page.email_alert().text == "Please enter a valid email address."


@allure.feature("Login Page")
@allure.description('Check wrong email or password error')
@allure.title("Wrong email format")
def test_wrong_email_or_password(driver):
    login_page = LoginPage(driver)
    with allure.step("Open login page"):
        login_page.open_login_page()
    with allure.step("Input wrong email and password"):
        login_page.email_field().send_keys("pashaqapp@mail.com")
        login_page.password_field().send_keys("testqap10")
    with allure.step("Click sign in button"):
        login_page.sign_in().click()
    assert login_page.wrong_auth_data().text == "Your account name or password is incorrect."


@allure.feature("Login Page")
@allure.description('Check empty authorization fields')
@allure.title("Empty auth field")
def test_empty_auth_fields(driver):
    login_page = LoginPage(driver)
    with allure.step("Open login page"):
        login_page.open_login_page()
    with allure.step("Input empty email and password and submit sign in"):
        login_page.email_field().send_keys("")
        login_page.password_field().send_keys("")
        login_page.sign_in().click()
    assert login_page.password_alert().text == "Please provide a password" and \
           login_page.email_alert().text == "Please enter a valid email address."


@allure.feature("Login Page")
@allure.description('Check password recovery button')
@allure.title("Password recovery button")
def test_password_recovery_button(driver):
    login_page = LoginPage(driver)
    with allure.step("Open login page"):
        login_page.open_login_page()
    with allure.step("Click password recovery button"):
        login_page.password_recovery().click()
    assert "reset password" in login_page.page_title_reset_password().text


@allure.feature("Login Page")
@allure.description('Check correct google window authorization')
@allure.title("Google link")
def test_google_link(driver):
    login_page = LoginPage(driver)
    with allure.step("Open login page"):
        login_page.open_login_page()
    with allure.step("Open google authorization"):
        login_page.open_google_auth()
    with allure.step("Checking correct window authorization"):
        driver.switch_to.window(driver.window_handles[1])
        assert login_page.google_text() == 'Войдите в аккаунт Google'


@allure.feature("Login Page")
@allure.description('Check correct facebook window authorization')
@allure.title("Google link")
def test_facebook_link(driver):
    login_page = LoginPage(driver)
    with allure.step("Open login page"):
        login_page.open_login_page()
    with allure.step("Open google authorization"):
        login_page.open_facebook_link().click()
    with allure.step("Checking correct window authorization"):
        driver.switch_to.window(driver.window_handles[1])
        assert login_page.facebook_text().text == "Facebook"
