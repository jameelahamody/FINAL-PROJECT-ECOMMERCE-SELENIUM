import selenium
import time
import pytest
from selenium import webdriver
from locale import atof, setlocale, LC_NUMERIC
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

#2. Test Case - Verify invalid email address error.

@pytest.fixture(autouse=True)
def driver():
    chrome_driver_binary = r'.\drivers\chromedriver'
    driver = webdriver.Chrome(chrome_driver_binary)

    yield driver
    driver.close()



def test_total_price(driver):
    try:
        time.sleep(2)
        driver.get('https://www.telerik.com/purchase')
        driver.maximize_window()
        buy_now_btn = driver.find_element(By.CSS_SELECTOR,".Pricings-button > th:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
        driver.execute_script("arguments[0].click();", buy_now_btn)
        time.sleep(6)
        unit_price = driver.find_element(By.CSS_SELECTOR, 'span.u-db:nth-child(1)').text
        quantity = driver.find_element(By.CSS_SELECTOR, '#c56dd4e9-8696-4457-8c7e-be9110f15c2f').text
        total = driver.find_element(By.CSS_SELECTOR, 'div.u-fr:nth-child(3)').text
        # setlocale(LC_NUMERIC, "YOURLOCALE")  # a locale where commas are used as the decimal point
        # atof(total.text.strip())
        # atof(unit_price.text.strip())
        # atof(quantity.text.strip())
        unit_price=float(unit_price[1:])
        quantity=float(quantity)
        total=float(total[1:])
        price= unit_price*quantity
        assert price == total
    except NoSuchElementException:

            print("TRUE")

    except UnboundLocalError as error:
       #Output expected UnboundLocalErrors.
         print('error')