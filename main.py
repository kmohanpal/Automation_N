from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https:\\www.google.com")
searchbar = driver.find_element(By.ID, "APjFqb")
searchbar.send_keys("Automation")
time.sleep(4)
searchbar.send_keys(Keys.ENTER)
time.sleep(4)