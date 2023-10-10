import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def runCharge(ID_CARD_NUMBER, TOTAL, DESCRIPTION):
    driver = webdriver.Edge()
    
    driver.get('https://awrbyu.atriumcampus.com/mechanicalengineering/dashboard')
    username = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, "name"))
    username.send_keys("ksc")
    password = driver.find_element(By.ID, "password")
    password.send_keys("CB154")
    driver.find_element(By.NAME, "submit").click()
    transactions = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, "custom-button-1"))
    transactions.click()
    ID = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, "transaction_card_number"))
    ID.send_keys(ID_CARD_NUMBER)
    Amount = driver.find_element(By.NAME, "transaction_amount")
    Amount.clear()
    Amount.send_keys(TOTAL)
    Description = driver.find_element(By.NAME, "transaction_description")
    Description.send_keys(DESCRIPTION)
    time.sleep(30)
    driver.quit()
if __name__ == "__main__":
    runCharge(sys.argv[1], sys.argv[2], sys.argv[3])
