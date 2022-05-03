import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Chrome()
driver.set_window_size(1570, 882)
# Test name: search4
# Step # | name | target | value
# 1 | open | /Account/LogOn?returnUrl=%2F |
driver.get("https://potomac.buildingperformance.com/Account/LogOn?returnUrl=%2F")
# 2 | setWindowSize | 1270x82 |

inputElement = driver.find_element_by_id("username")
inputElement.send_keys('melissap0303@gmail.com')

inputElement = driver.find_element_by_id("password")
inputElement.send_keys('')

# 10 | click | id=loginSubmit |
driver.find_element_by_id("loginSubmit").click()

# 11 | click | linkText=Create Job and Validate Customer |
driver.find_element_by_link_text("Create Job and Validate Customer").click()

# 12 | click | id=SERV_ADDR_HOUSE_NUM |
numElement = driver.find_element_by_id("SERV_ADDR_HOUSE_NUM")
numElement.send_keys('6602')

# 14 | click | id=SERV_ADDR_STREET_NAME |
addrElement = driver.find_element_by_id("SERV_ADDR_STREET_NAME")
addrElement.send_keys('coldstream')

# 16 | click | css=.c-btn | click submit
driver.find_element(By.CSS_SELECTOR, ".c-btn").click()

# 17 Grab Used or Not
driver.find_element(By.CSS_SELECTOR, ".even:nth-child(12) > td").click()

# # 17 | click | css=.data-column-head > th:nth-child(2) |
# driver.find_element(By.CSS_SELECTOR, ".data-column-head > th:nth-child(2)").click()
# # 18 | click | css=.data-column-head > th:nth-child(2) |
# driver.find_element(By.CSS_SELECTOR, ".data-column-head > th:nth-child(2)").click()
# # 19 | doubleClick | css=.data-column-head > th:nth-child(2) |
# element = driver.find_element(By.CSS_SELECTOR, ".data-column-head > th:nth-child(2)")

actions = ActionChains(driver)
actions.double_click(element).perform()

# driver.quit()
