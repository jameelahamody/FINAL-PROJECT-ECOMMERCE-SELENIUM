import time

import pytest
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FireFoxOptions




@pytest.fixture()
def driver():
    Firefox_driver_binary = r"./drivers/geckodriver"
    fire_fox_options = FireFoxOptions()
    fire_fox_options.add_argument("--width=414")
    fire_fox_options.add_argument("--height=896")
    fire_fox_options.set_preference("general.useragent.override", "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS "
                                                                  "X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                                                                  "Version/14.0.3 Mobile/15E148 Safari/604.1")
    ser_firefox = FirefoxService(Firefox_driver_binary)
    driver = webdriver.Firefox(service=ser_firefox, options=fire_fox_options)
    yield driver


def test_create_account(driver):
    try:
        time.sleep(3)
        driver.get('https://www.telerik.com/login')
        time.sleep(2)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        driver.delete_all_cookies()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#ContentPlaceholder1_C023_Col00 > div.sfContentBlock > div > a").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#Email-1").send_keys('fhfdssjam@gmail.com')
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#Textbox-1").send_keys("jameela")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#Textbox-2").send_keys("suliman")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#Textbox-3").send_keys("amazon")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#Country-1").send_keys("Isreal")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#Textbox-4").send_keys("0549212345")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#form--1 > div:nth-child(6) > div:nth-child(10) > button").click()
        time.sleep(3)
        actual_url = 'https://www.telerik.com/registration-login/registration-successful'
        expected_url = driver.current_url
        assert actual_url == expected_url
    except NoSuchElementException:
        print("error")
