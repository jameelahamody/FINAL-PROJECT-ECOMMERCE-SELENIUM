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

# Automate Buy Product feature
@pytest.fixture(autouse=True)
def driver():
    chrome_driver_binary = r'.\drivers\chromedriver'
    driver = webdriver.Chrome(chrome_driver_binary)
    yield driver
    driver.close()


def test_buy_product(driver):
    driver.get("https://www.telerik.com/purchase")
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.delete_all_cookies()
    driver.implicitly_wait(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1)
    driver.delete_all_cookies()
    btn = driver.find_element(By.CSS_SELECTOR,"#ContentPlaceholder1_C1091_Col01 > a")
    driver.execute_script("arguments[0].click();", btn)
    buy_now_btn=driver.find_element(By.CSS_SELECTOR,"#ContentPlaceholder1_C140_Col00 > div > div > div.PricingTable-Wrap > table > thead > tr.Pricings-button > th.UI > div > a")
    driver.execute_script("arguments[0].click();", buy_now_btn)
    time.sleep(3)
    select=driver.find_element(By.XPATH,'//*[@id="k-24825c5c-ad78-4d47-b942-d7a01f538f65"]')
    for option in select:
        if option == 2:
            option.click()
    try:
        continue_btn = driver.find_element(By.XPATH,"/html/body/div[1]/div/shopping-cart-app/section/your-order/div/div/div[6]/button")
        time.sleep(3)
        driver.delete_all_cookies()
        url = driver.execute_script("arguments[0].click();", continue_btn)
        time.sleep(3)
        driver.delete_all_cookies()
        assert url.is_displayed()== True
    except NoSuchElementException:
        print("Something wrong ,please try again!")


    #NOW CONTACT INFO:(i will add an extra calling for a success buying)
    driver.get("https://store.progress.com/contact-info")
    #billing information:
    first_name=driver.find_element(By.CSS_SELECTOR,"#biFirstName").send_keys("safa")
    time.sleep(2)
    last_name=driver.find_element(By.CSS_SELECTOR,"#biLastName").send_keys("hamody")
    time.sleep(2)
    E_mail=driver.find_element(By.CSS_SELECTOR,"#biEmail").send_keys("jojo.om.h@gmail.com")
    time.sleep(2)
    Company=driver.find_element(By.CSS_SELECTOR,"#biCompany").send_keys("adham")
    time.sleep(2)
    Phone=driver.find_element(By.CSS_SELECTOR,"#biPhone").send_keys("0547838841")
    time.sleep(2)
    Address=driver.find_element(By.CSS_SELECTOR,"#biAddress").send_keys("Abu hossi 22")
    time.sleep(2)
    Country=driver.find_element(By.NAME,"billCountry")
    all_options=Country.find_element(By.TAG_NAME,"option")
    for option in all_options:
        if option.text == 'Isreal':
            option.click()
    time.sleep(2)
    City=driver.find_element(By.CSS_SELECTOR,"#biCity").send_keys("haifa")
    time.sleep(2)
    continue_btn = driver.find_element(By.CSS_SELECTOR,"#ContentPlaceholder1_C140_Col00 > div > div > div.PricingTable-Wrap > table > thead > tr.Pricings-button > th.UI > div > a")
    driver.execute_script("arguments[0].click();", continue_btn)
    time.sleep(3)

