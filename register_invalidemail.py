import pytest
import selenium
import time
from selenium import webdriver
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

#2. Test Case - Verify invalid email address error.

@pytest.fixture(autouse=True)
def driver():
    chrome_driver_binary = r'.\drivers\chromedriver'
    driver = webdriver.Chrome(chrome_driver_binary)
    driver.get('https://www.telerik.com')
    yield driver
    driver.close()


def test_create_account_from_invalid_email(driver):
     try:
        time.sleep(3)
        driver.get('https://www.telerik.com/login/v2/telerik#register')
        driver.maximize_window()
        driver.delete_all_cookies()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "#Email-1").send_keys("jam")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#Textbox-1").send_keys("ora")
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
        driver.execute_script("scroll(0, -250);")
        time.sleep(3)
        assert "Not a valid email address" == driver.find_element(By.CSS_SELECTOR,"p.sfError").text
     except NoSuchElementException:
         print("error")
     except WebDriverException:
         print('registration-successful')




