#Web scraping project for scraping search page::

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
file = 0 

driver = webdriver.Chrome() 
query = ''#query for particular product

for i in range(1,10):#loop through 9 elements 
    driver.get(f"URL/q={query}") #Go to python.org
    elems = driver.find_elements(By.CLASS_NAME,"ClassName")#ClassName for Container of product card  in website
# print(elem.get_attribute("outerHTML"))
    print(f"{len(elems)} item found")
    for elem in elems:
        d = elem.get_attribute("outerHTML") #Get your desired attribute
        with open(f"data/{query}_{file}","w",encoding ="utf-8") as f:
         f.write(d)
         file+=1



time.sleep(20)
driver.close()
