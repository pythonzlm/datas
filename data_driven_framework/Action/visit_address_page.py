#encoding=utf-8
from selenium import webdriver
from Util.log import *
from Util.FormatTime import *
import time
from PageObject.login_page import *
from PageObject.home_page import *
from login import *

def visit_address_page(driver):
    hp = HomePage(driver)
    hp.address_book_page_link().click()
    time.sleep(5)