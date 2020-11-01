# Sa mga gagamit ng script na to, make sure na ireview nyo muna ung default apn niyo. atleast marunong kayo kumalikot ng inspect element ni firefox.
# For firefox users muna, kasi wala akong chrome driver
# Peded niyo imodify, make sure lang mag push kayo ng update tsaka magcommit din kayo sa github ko. for improvement
# May naka package na din na gecko driver yan, may tendency na hindi compatible si gecko ko sa firefox niyo. 
# kung ayaw niyo naman na walan browser na nag pa pop-up, uncomment niyo lang ung headless option sa webdriver
# depende sa router niyo, malaman di to gagana. 
# Ang router ko is Huawei B315-936

import time
import sys
import os
import platform
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

if platform.system() == "Windows":  # checking OS
    geckopath = "./geckodriver.exe" #driver path
else:
    geckopath = "./geckodriver" #driver path

#username and password
user = input("Please enter your web portal's username:")
password = input("Please enter your web portal's password:")


def console_cleaner():
        if platform.system == "Windows":
                global clear
                clear = lambda: os.system('cls')
        else:
                clear = lambda: os.system('clear')

while True:
        try:
                time_delay = int(input("Please enter your desired time delay(in Seconds):"))
        except ValueError:
                print("\n")
                print("Invalid time.")
                continue
        else:
                break


def change_apn():
        print("Changing Access point...")
        #loads gecko driver for firefox
        options = FirefoxOptions()
        
        #activate headless mode uncomment niyo ung options.add_argument

        options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=geckopath, options=options)
        driver.get('http://192.168.8.1/html/quicksetup.html')
        print("Headless mode initialized")
        # driver.set_window_size(1000, 800)

        #waits until element is clickable
        print("Logging In...")
        element = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.ID, "username")))
        element =  driver.find_element_by_xpath("//input[@id='username']")
        element.click()
        #inputs username
        element.send_keys(user)

        #waits until element is clickable
        element = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.ID, "password")))
        element = driver.find_element_by_xpath("//input[@id='password']")
        element.click()
        #inputs password
        element.send_keys(password)

        wait1 = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'pop_login'))
        )
        #clicks login
        element = driver.find_element_by_xpath("//input[@id='pop_login']")
        element.click()



        #####################################################################
        driver.get('http://192.168.8.1/html/profilesmgr.html')
        # driver.set_window_size(1000, 800)
        print("Login Success...")
        element = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.ID, "label_profile_management")))
        element = driver.find_element_by_xpath("//span[@id='label_profile_management']")
        element.click()

        element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "profilelist")))

        #ililipat temporarily ang apn to internet.globe.com.ph
        element = driver.find_element_by_id("profilelist").click()
        element = driver.find_element_by_xpath("//select/option[@value='1']").click()
        element = driver.find_element_by_xpath("//input[@id='select_apply']").click()
        print("Access Point Changed to option 1...")
        print("\n")

        #ibabalik sa default na apn which is the http.globe.com.ph
        element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "profilelist")))
        element = driver.find_element_by_id("profilelist").click()
        element = driver.find_element_by_xpath("//select/option[@value='2']").click()
        element = driver.find_element_by_xpath("//input[@id='select_apply']").click()
        print("Access Point Changed to option 2...")
        print("\n")

        driver.close()
        print("Apn Changed Successfully")
        print("\n")
        time.sleep(5)
        clear() #clears the console

        for i in reversed(range(0, int(time_delay))):
                time.sleep(1 - time. time() % 1) #sleep execution
                sys.stderr.write('\r%4d' % i + " seconds remaining . . . .")
                if i == 0:
                        clear()
while True:
        console_cleaner() 
        change_apn()


# eto ung basis ng profile list ko
# <select id="profilelist">
#         <option value="1">Globe&nbsp;Tattoo&nbsp;Broadband&nbsp;-&nbsp;Postpaid</option>
#         <option value="2">Globe&nbsp;Tattoo&nbsp;Broadband&nbsp;-&nbsp;Prepaid(default)</option>
#         <option value="3">ABS-CBN&nbsp;Mobile</option><option value="4">Custom</option>
# </select>
