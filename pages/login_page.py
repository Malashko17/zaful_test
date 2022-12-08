from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

sign_in_text = (By.XPATH, "//h4[text()='Sign In']")
email_field = (By.ID, "email")
password_field = (By.ID, "passwordsign")
sign_in_button = (By.CLASS_NAME, "elf-mood-sign-btn")
account_icon = (By.CLASS_NAME, "js-topaccount-user")
my_account = (By.XPATH, '//a[text()="MY ACCOUNT"]')
nickname = (By.NAME, 'nickname')
email_error = (By.XPATH, '//label[text()="Please enter a valid email address."]')
password_error = (By.XPATH, '//label[text()="Please provide a password"]')
wrong_email_password = (By.XPATH, '//p[text()="Your account name or password is incorrect."]')
password_recovery = (By.ID, "getpassword")
password_recovery_title = (By.CLASS_NAME, "mb30")
google_link = (By.XPATH, "//span[text()='Google']")
google_text = (By.XPATH, "//div[text()='Войдите в аккаунт Google']")


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_login_page(self):
        self.driver.get("https://user.zaful.com/zfie/sign-up.html")

    def email_field(self):
        return self.find_element(email_field)

    def password_field(self):
        return self.find_element(password_field)

    def sign_in(self):
        return self.find_element(sign_in_button)

    def account_icon(self):
        return self.find_element(account_icon)

    def my_account(self):
        return self.find_element(my_account)

    def check_sign_in(self):
        return self.find_element(nickname).is_displayed()

    def email_alert(self):
        return self.find_element(email_error)

    def password_alert(self):
        return self.find_element(password_error)

    def wrong_auth_data(self):
        return self.find_element(wrong_email_password)

    def password_recovery(self):
        return self.find_element(password_recovery)

    def page_title_reset_password(self):
        return self.find_element(password_recovery_title)

    def open_google_auth(self):
        return self.find_element(google_link).click()

    def google_text(self):
        return self.find_element(google_text).text

    def click_text(self):
        return self.find_element(sign_in_text).click()