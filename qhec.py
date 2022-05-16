import pytest
import time
import json
# from pandas import *
import os
import csv
import time
import re
import sys
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
inputElement1 = driver.find_element(By.ID,"username").send_keys('melissap0303@gmail.com')
inputElement2 = driver.find_element(By.ID,"password").send_keys('')
driver.find_element(By.ID,"loginSubmit").click()
driver.find_element(By.LINK_TEXT,"Create Job and Validate Customer").click()
input = sys.argv[1]
file = open(os.path.join('./', input), "r")
reader = csv.reader(file, delimiter=',')
outfile = sys.argv[2]
#make new file save based on sourceFilename_results.csv
with open(outfile, 'a+', newline='') as f_object:
    writero = csv.writer(f_object, delimiter=',')
    for row in reader:
        # print(row[0])
        # print(row[1])
        numElement = driver.find_element(By.ID,"SERV_ADDR_HOUSE_NUM")
        numElement.clear()
        numElement.send_keys(row[0])
        addrElement = driver.find_element(By.ID,"SERV_ADDR_STREET_NAME")
        addrElement.clear()
        addrElement.send_keys(row[1])
        driver.find_element(By.CSS_SELECTOR,".c-btn").click()
        try:
            isqhec = driver.find_element(By.CSS_SELECTOR, ".even:nth-child(12) > td").text
            if isqhec == "":
                print("Good2Call")
                driver.find_element(By.ID, "WorkflowType").click()
                dropdown =  driver.find_element(By.ID, "WorkflowType")
                dropdown.find_element(By.XPATH, "//option[. = 'FEMD-QHEC']").click()
                driver.find_element(By.CSS_SELECTOR, ".c-btn:nth-child(4)").click()
                location =  driver.find_element(By.ID, "Address_City").get_attribute("value")
                zip =  driver.find_element(By.ID, "Address_Zip").get_attribute("value")
                fname =  driver.find_element(By.ID, "Owner_FirstName").get_attribute("value")
                lname =  driver.find_element(By.ID, "Owner_LastName").get_attribute("value")
                tele =  driver.find_element(By.ID, "Owner_PhoneNumber").get_attribute("value")
                email =  driver.find_element(By.ID, "Owner_Email").get_attribute("value")
                # listicle = [(row[0], row[1], location, zip, fname, lname, tele, email)]
                listicle = [(row[0], row[1], location, fname, lname, tele)]
                writero.writerow(listicle)
                driver.back()
            else:
                print(isqhec)
        except NoSuchElementException:
            print("errorNotFound")
    f_object.close()
    # actions = ActionChains(driver)
    # actions.double_click(element).perform()
    # driver.quit()

    #to put in production mode, move lines 47-59 to below line 44
