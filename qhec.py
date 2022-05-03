import pytest
import time
import json
# from pandas import *
import os
import csv
import time
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException        

driver = webdriver.Chrome()
driver.set_window_size(1570, 882)
# Test name: search4qhec
# Step # | name | target | value
driver.get("https://potomac.buildingperformance.com/Account/LogOn?returnUrl=%2F")
inputElement1 = driver.find_element_by_id("username").send_keys('melissap0303@gmail.com')
inputElement2 = driver.find_element_by_id("password").send_keys('')
driver.find_element_by_id("loginSubmit").click()
driver.find_element_by_link_text("Create Job and Validate Customer").click()

file = open(os.path.join('./', 'potomac.csv'), "rU")
reader = csv.reader(file, delimiter=',')
for row in reader:
    # print(row[0])
    # print(row[1])
    numElement = driver.find_element_by_id("SERV_ADDR_HOUSE_NUM")
    numElement.clear()
    numElement.send_keys(row[0])

    addrElement = driver.find_element_by_id("SERV_ADDR_STREET_NAME")
    addrElement.clear()
    addrElement.send_keys(row[1])
    driver.find_element_by_css_selector(".c-btn").click()
    
    try:
        isqhec = driver.find_element(By.CSS_SELECTOR, ".even:nth-child(12) > td").text
        if isqhec == "":
            print("Good2Call")
        else:
            print(isqhec)
    except NoSuchElementException:
        print("errorNotFound")




# actions = ActionChains(driver)
# actions.double_click(element).perform()

# driver.quit()
