import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

#driver = webdriver.Firefox(executable_path="C:\Driver\geckodriver.exe")
#driver = webdriver.Ie(executable_path="C:\Driver\IEDriverServer.exe")

driver.get("http://jatri.co/")
print(driver.title)  #driver title

print(driver.current_url)  #page url
#print(driver.page_source) #html code
driver.find_element_by_xpath("/html/body/section[3]/div/div/div/div/div/div[2]/div/div[2]/button").click()
time.sleep(5)
driver.close() #current tab
driver.quit() #close all tabs