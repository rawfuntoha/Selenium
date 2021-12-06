from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

driver = webdriver.Firefox(executable_path="C:\Driver\geckodriver.exe")
#driver = webdriver.Ie(executable_path="C:\Driver\IEDriverServer.exe")

driver.get("http://jatri.co/")

print(driver.current_url)  #page url
#print(driver.page_source) #html code
print(driver.title)  #driver title
driver.close()