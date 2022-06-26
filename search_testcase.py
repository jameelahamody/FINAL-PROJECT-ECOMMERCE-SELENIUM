from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FireFoxOptions
import time
import pytest


@pytest.fixture()
def driver():
    Firefox_driver_binary = r'./drivers/geckodriver'
    fire_fox_options = FireFoxOptions()
    fire_fox_options.add_argument("--width=414")
    fire_fox_options.add_argument("--height=896")
    fire_fox_options.set_preference("general.useragent.override", "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS "
                                                                  "X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                                                                  "Version/14.0.3 Mobile/15E148 Safari/604.1")
    ser_firefox = FirefoxService(Firefox_driver_binary)
    driver = webdriver.Firefox(service=ser_firefox, options=fire_fox_options)
    yield driver
    driver.close()


def test_LogIn(driver):
    driver.get('https://www.telerik.com/login')
    driver.maximize_window()
    driver.implicitly_wait(0.5)
    driver.delete_all_cookies()
    email = driver.find_element(By.ID, "username")
    email.send_keys("hamodyjameela@gmail.com")
    time.sleep(1)
    driver.delete_all_cookies()
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("jameela")
    time.sleep(2)
    btn = driver.find_element(By.CSS_SELECTOR, "#LoginButton-1")
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(10)
    actual_url = 'https://www.telerik.com/account'
    expected_url = driver.current_url
    assert expected_url == actual_url
    try:
        logout_button = driver.find_element_by_id("logout")
        print('Successfully logged in')
    except NoSuchElementException:
        print('Incorrect login/password')
