import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
import urllib3


def getPhoto(ID_CARD_NUMBER):
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    
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
    time.sleep(1)
    with open('temp.png', 'wb') as file:
        HTML = driver.find_element(By.XPATH, '//img[@class="user_photo"]').get_property('outerHTML')
        Photo = driver.find_element(By.XPATH, '//img[@class="user_photo"]')
        file.write(Photo.screenshot_as_png)
    driver.quit()
if __name__ == "__main__":
    getPhoto(sys.argv[1])
