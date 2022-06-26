
import pytest
import selenium
import time
from selenium import webdriver
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(autouse=True)
def driver():
    chrome_driver_binary = r'.\drivers\chromedriver'
    driver = webdriver.Chrome(chrome_driver_binary)
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
        actual_url='https://www.telerik.com/account'
        expected_url = driver.current_url
        assert expected_url == actual_url
        try:
            logout_button = driver.find_element_by_id("logout")
            print('Successfully logged in')
        except NoSuchElementException:
            print('Incorrect login/password')

