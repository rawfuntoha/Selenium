from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")


driver.get("http://fb.com/")

ele=driver.find_element_by_name("email")


print(ele.is_displayed())

print(ele.is_enabled())

pwd_ele=driver.find_element_by_name("pass")

print(pwd_ele.is_displayed())

print(pwd_ele.is_enabled())


ele.send_keys("marcury")

pwd_ele.send_keys("1234")
driver.find_element_by_name("login").click()

"""

driver.get("https://mbasic.facebook.com/reg")

ele=driver.find_element_by_name("email")

print(ele.is_displayed())

print(ele.is_enabled())

pwd_ele=driver.find_element_by_name("pass")

print(pwd_ele.is_displayed())

print(pwd_ele.is_enabled())

ele.send_keys("marcury")
pwd_ele.send_keys("1234")
driver.find_element_by_name("login").click()

"""