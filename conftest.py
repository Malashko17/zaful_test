from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import settings
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope="function")
def login(driver):
    driver.get("https://user.zaful.com/zfie/sign-up.html")
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(settings.EMAIL)
    password = driver.find_element(By.ID, "passwordsign")
    password.send_keys(settings.PASSWORD)
    driver.find_element(By.CLASS_NAME, "elf-mood-sign-btn").click()
    driver.implicitly_wait(5)
