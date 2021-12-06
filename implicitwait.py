import time

from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

driver.get("http://fb.com/")

#assert "toha" in driver.title
driver.implicitly_wait(10)
driver.find_element_by_name("email").send_keys("marcury")
driver.find_element_by_name("pass").send_keys("1234")



driver.find_element_by_name("login").click()


time.sleep(10)

driver.quit()
driver.close()