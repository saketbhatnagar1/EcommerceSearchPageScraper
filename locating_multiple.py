from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome() 
query = 'laptop'
driver.get(f"https://www.amazon.in/s?k={query}&crid=293ZV7B0Q6PQC&sprefix=laptop%2Caps%2C208&ref=nb_sb_noss_2") #Go to python.org

elem = driver.find_element(By.CLASS_NAME,"puis-card-container")#ClassName for Container of product card  in amazon.in
# print(elem.get_attribute("outerHTML"))


time.sleep(20)
driver.close()