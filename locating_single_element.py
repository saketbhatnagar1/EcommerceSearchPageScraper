from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome() 
query = ''#Optional
driver.get(f"URL") #Go to python.org

elem = driver.find_element(By.CLASS_NAME,"ClassName")
print(elem.get_attribute("outerHTML"))
time.sleep(20)
driver.close()
