import time
import pytest
from IPython.core.display import Javascript
from selenium import webdriver
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

#Automate 'Search Product' feature

@pytest.fixture(autouse=True)
def driver():
    chrome_driver_binary = r'.\drivers\chromedriver'
    driver = webdriver.Chrome(chrome_driver_binary)
    yield driver
    driver.close()

def test_search(driver):
    SCROLL_PAUSE_TIME = 0.5
    driver.get("https://www.telerik.com/search")
    driver.maximize_window()
    driver.implicitly_wait(3)
    input_search=driver.find_element(By.CSS_SELECTOR,"#ContentPlaceholder1_C006_Col00 > section.Section.Section--lightblue > div > div > div > tk-site-search > div > div > input")
    time.sleep(2)
    input_search.send_keys("UI for Blazor")
    search_btn=driver.find_element(By.CSS_SELECTOR,"#ContentPlaceholder1_C006_Col00 > section.Section.Section--lightblue > div > div > div > tk-site-search > div > button")
    time.sleep(2)
    search_btn.click()
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(2)
    assert f"Your search {input_search} did not match any documents. Search suggestions:" not in driver.page_source

