import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:\Driver\geckodriver.exe")

driver.get("http://jatri.co/")
time.sleep(5)

print(driver.title)  #jatri

driver.get("http://dev.rental.jatri.co/")

time.sleep(5)

print(driver.title)  #rental

driver.back()

time.sleep(5)
print(driver.title)  #jatri
driver.forward()
time.sleep(5)
print(driver.title)  #rental
