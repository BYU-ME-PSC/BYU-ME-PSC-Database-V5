import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller


def runCharge(ID_CARD_NUMBER, ITEMS):
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    
    driver.get('https://awrbyu.atriumcampus.com/v2/MechanicalEngineeringProjectSupportCenterv2')
    username = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, "name"))
    username.send_keys("ksc")
    password = driver.find_element(By.ID, "password")
    password.send_keys("CB154")
    driver.find_element(By.NAME, "submit").click()
    transactions = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.LINK_TEXT, "Transactions"))
    transactions.click()
    ID = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, "card_number"))
    ID.send_keys(ID_CARD_NUMBER)
    list_button = driver.find_element(By.XPATH, '//div[@id="selected_products_dropdown"]//a[@href="javascript:void(0);"]')
    add_button = driver.find_element(By.ID, "add_misc_product")
    driver.execute_script("window.scrollTo(0,1000)")
    for i, item in enumerate(ITEMS):
        Description = driver.find_element(By.NAME, "misc_product_name")
        Description.send_keys(item[0])
        Amount = driver.find_element(By.NAME, "misc_product_amount")
        Amount.clear()
        Amount.send_keys(item[1])
        add_button.click()
        if(i==0):
            list_button.click()
            time.sleep(1)
        Quantity = driver.find_element(By.XPATH, "//div[@class='selected_products_details']/ul/li[last()]//a[last()]")
        for j in range(item[2]-1):
            Quantity.click()
        driver.execute_script("window.scrollBy(0,100)")
    time.sleep(180)
    driver.quit()
if __name__ == "__main__":
    runCharge('test', [['desc','1.20',2],['desc2','1.00',3],['desc3','3.60',7]])
