from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


# @pytest.fixture(scope="session")
# def login():
#     chrome_driver = webdriver.Chrome()
#     chrome_driver.get("https://gde.by/user/login")
#     email_input = chrome_driver.find_element(By.ID, "LoginForm_email")
#     email_input.send_keys("pashaqap09@mail.ru")
#     password = chrome_driver.find_element(By.ID, "LoginForm_password")
#     password.send_keys("Testqap09")
