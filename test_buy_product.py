
import pytest
import selenium
import time
from selenium import webdriver
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
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
  
def test_price(driver):
  driver.get("https://www.telerik.com/")
  driver.set_window_size(550, 693)
  element = driver.find_element(By.CSS_SELECTOR, ".TK-Products-Menu-Item-Button")
  actions = ActionChains(driver)
  actions.move_to_element(element).perform()
  element = driver.find_element(By.CSS_SELECTOR, "body")
  actions = ActionChains(driver)
  actions.move_to_element(element, 0, 0).perform()
  driver.find_element(By.CSS_SELECTOR, "#js-tlrk-nav-not-auth-container svg").click()
  driver.find_element(By.ID, "LoginButton-1").click()
  element = driver.find_element(By.CSS_SELECTOR, ".\\435 2\\435-dashboard-section:nth-child(3) .ng-star-inserted:nth-child(1) > .container-floating")
  actions = ActionChains(driver)
  actions.move_to_element(element).perform()
  driver.find_element(By.CSS_SELECTOR, ".js-tlrk-nav-shopping-cart-counter-container > svg").click()
  driver.execute_script("window.scrollTo(0,0)")
  driver.find_element(By.CSS_SELECTOR, ".color-success-dark").click()
  driver.find_element(By.CSS_SELECTOR, ".color-success-dark").click()
  element = driver.find_element(By.ID, "0cb09290-a8ca-48cc-bc5d-9b59ffadf61a")
  actions = ActionChains(driver)
  actions.move_to_element(element).click_and_hold().perform()
  element = driver.find_element(By.ID, "0cb09290-a8ca-48cc-bc5d-9b59ffadf61a")
  actions = ActionChains(driver)
  actions.move_to_element(element).perform()
  element = driver.find_element(By.ID, "0cb09290-a8ca-48cc-bc5d-9b59ffadf61a")
  actions = ActionChains(driver)
  actions.move_to_element(element).release().perform()
  driver.find_element(By.ID, "0cb09290-a8ca-48cc-bc5d-9b59ffadf61a").click()
  driver.find_element(By.ID, "0cb09290-a8ca-48cc-bc5d-9b59ffadf61a").click()
  driver.find_element(By.ID, "0cb09290-a8ca-48cc-bc5d-9b59ffadf61a").click()
  driver.find_element(By.CSS_SELECTOR, "#\\35 7f6982f-948e-4251-a810-c903441adf1c-2 > .ng-star-inserted").click()
  driver.find_element(By.CSS_SELECTOR, ".e2e-total-price").click()

