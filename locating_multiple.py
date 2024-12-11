from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome() 
query = 'laptop'
driver.get(f"URL") #Go to python.org

elem = driver.find_element(By.CLASS_NAME,"ClassName")#ClassName for Container of product card  in amazon.in
# print(elem.get_attribute("outerHTML"))


time.sleep(20)
driver.close()
