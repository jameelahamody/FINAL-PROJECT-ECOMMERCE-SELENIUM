
import pytest
import selenium
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service as ChromeService



#1. Test Case - Automate User Registration:

@pytest.fixture()
def driver():
    chrome_driver_binary = r'.\drivers\chromedriver.exe'
    # ser_chrome = ChromeService(chrome_driver_binary)
    driver = webdriver.Chrome(chrome_driver_binary)
    yield driver
    driver.close()


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
        actual_url='https://www.telerik.com/registration-login/registration-successful'
        expected_url=driver.current_url
        assert actual_url == expected_url
     except NoSuchElementException:
         print("error")


