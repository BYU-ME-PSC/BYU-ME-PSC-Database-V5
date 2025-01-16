import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def runCharge(ID_CARD_NUMBER, TOTAL, DESCRIPTION):
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
    Description = driver.find_element(By.NAME, "misc_product_name")
    Description.send_keys(DESCRIPTION)
    Amount = driver.find_element(By.NAME, "misc_product_amount")
    Amount.clear()
    Amount.send_keys(TOTAL)
    add_button.click()
    list_button.click()
    time.sleep(180)
    driver.quit()
if __name__ == "__main__":
    runCharge(sys.argv[1], sys.argv[2], sys.argv[3])
