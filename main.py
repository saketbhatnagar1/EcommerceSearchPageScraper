from selenium import webdriver  # Import the WebDriver module from Selenium to interact with web browsers
from selenium.webdriver.common.keys import Keys  # Import Keys to simulate keyboard actions like ENTER, TAB, etc.
from selenium.webdriver.common.by import By  # Import By to specify methods for locating elements on a web page
import time

driver = webdriver.Chrome()  # Initialize a new Chrome browser instance using the WebDriver
driver.get("http://www.python.org")  # Navigate to the Python.org homepage
assert "Python" in driver.title  # Assert that "Python" is in the title of the page to ensure correct navigation

elem = driver.find_element(By.NAME, "q")  # Locate the search bar on the webpage by its "name" attribute (q)
elem.clear()  # Clear any pre-filled text in the search bar to prepare for input

elem.send_keys("pyadsasdasdcon")  # Type "pycon" into the search bar
elem.send_keys(Keys.RETURN)  # Simulate pressing the ENTER key to submit the search

assert "No results found." not in driver.page_source  # Verify that the search returned results by checking the page's content
time.sleep(10)
driver.close()  # Close the browser window and end the WebDriver session

'''

webdriver.Chrome()
Initializes an instance of the Chrome WebDriver, allowing automated interactions with a Chrome browser.

driver.get(url)
Opens the specified URL (http://www.python.org in this case) in the browser controlled by WebDriver.

driver.title
Retrieves the title of the current webpage.

assert
A Python keyword used for validation. It ensures that the specified condition is True. If not, the script raises an AssertionError.

driver.find_element(By.NAME, "q")
Locates a single web element using its "name" attribute. In this case, it finds the search bar on Python.org.

elem.clear()
Clears the text from an input field if there’s any pre-existing text.

elem.send_keys("pycon")
Simulates typing the string "pycon" into the identified element (elem).

Keys.RETURN
Simulates pressing the ENTER key. Used here to submit the search form.
driver.page_source

Retrieves the entire HTML source of the current webpage. Used to verify that "No results found." is not present.
driver.close()

Closes the browser window and ends the session associated with the WebDriver.
How the Script Works
Opens a Chrome browser and navigates to Python.org.
Checks the page title to confirm successful navigation.
Finds the search bar, clears it, types in "pycon," and submits the search.
Verifies that the search returns results by checking the absence of "No results found."
Closes the browser after completing the test.
This script automates a simple search functionality test on the Python.org website.







'''