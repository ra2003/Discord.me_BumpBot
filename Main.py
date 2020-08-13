import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import gmtime, strftime
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

DiscordEmail = "example@gmail.com"
DiscordPassword = "Hacker1337"

def CreateEvent():
    chrome_options = Options()
    executable_path = (r"C:\Users\zanluka\Desktop\chromedriver_win32 (4)\chromedriver.exe") ##Change this to your computer location of chrome driver
    os.environ["webdriver.chrome.driver"] = executable_path
    browser = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options)
    browser.get("https://discord.me/dashboard")
    time.sleep(10)
    submit=browser.find_element_by_xpath("//button[@type='submit']")
    email=browser.find_element_by_xpath("//input[@type='email']") 
    email.send_keys(DiscordEmail)
    password= browser.find_element_by_xpath("//input[@type='password']") 
    password.send_keys(DiscordPassword)
    submit.click()
    time.sleep(10)
    browser.get(browser.current_url)
    time.sleep(10)
    submit2 = browser.find_element_by_xpath("//button[@class='button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeMedium-1AC_Sl grow-q77ONN']")
    submit2.click()
    time.sleep(10)
    browser.get(browser.current_url)
    submit= browser.find_element_by_xpath("//a[@class='bump-btn']") 
    submit.click()
    time.sleep(10)
    submit2 = browser.find_element_by_id("bump-server-submit")
    submit2.click()

while  (True):
    if strftime("%H:%M:%S", gmtime()) == "19:01:00":
        CreateEvent()
    elif strftime("%H:%M:%S", gmtime()) == "01:01:00":
        CreateEvent()
    elif strftime("%H:%M:%S", gmtime()) == "07:01:00":
        CreateEvent()
    elif strftime("%H:%M:%S", gmtime()) == "13:01:00":
       CreateEvent()
    time.sleep(1) 

