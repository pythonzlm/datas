#encoding=utf-8
import time
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig
from Action.login import *

class HomePage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parse_config_file = ParsePageObjectRepositoryConfig()
        self.home_page_items = self.parse_config_file.getElementsFromSection("163mail_homepage")

    def address_book_page_link(self):
        locateType,locateExpression = self.home_page_items["home_page.addressbook"].split(">")
        return getElement(self.driver,locateType,locateExpression)
    
