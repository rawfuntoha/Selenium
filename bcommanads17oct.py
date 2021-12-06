import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(executable_path="C:\Driver\geckodriver.exe")

driver.get("https://www.sugarcrm.com/au/request-demo//")


print(driver.title)  #driver title

print(driver.current_url) #current url
selec=driver.find_element_by_xpath("/html[1]/body[1]/div[3]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[10]/div[3]/input[1]").click()

#driver.find_element_by_id("doi1").click()

time.sleep(15)
#driver.close() #close current browser

driver.quit()