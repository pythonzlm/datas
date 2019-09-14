from Util.FormatTime import *
import time
from PageObject.login_page import *
from PageObject.home_page import *
from selenium import webdriver
from Util.log import *

def login(driver,username,password):
    driver.get("http://mail.163.com")
    time.sleep(2)
    lp = LoginPage(driver)
    driver.switch_to_frame(lp.frame())
    lp.username().clear()
    lp.username().send_keys(username)
    lp.password().send_keys(password)
    lp.loginbutton().click()
    time.sleep(4)
    info("login successfully")
    print date_time_chinese()