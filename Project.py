#Web scraping project for scraping search page::

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
file = 0

driver = webdriver.Chrome() 
query = 'laptop'

for i in range(1,10):
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off") #Go to python.org
    elems = driver.find_elements(By.CLASS_NAME,"tUxRFH")#ClassName for Container of product card  in amazon.in
# print(elem.get_attribute("outerHTML"))
    print(f"{len(elems)} item found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}","w",encoding ="utf-8") as f:
         f.write(d)
         file+=1



time.sleep(20)
driver.close()
