#encoding=utf-8
import time
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig

class LoginPage(object):
    def __init__(self,driver):
        self.driver= driver
        self.parse_config_file = ParsePageObjectRepositoryConfig()
        self.login_page_items=self.parse_config_file.getElementsFromSection("163mail_login")

    def frame(self):
        locateType,locateExpression = self.login_page_items['login_page.frame'].split(">")
        return getElement(self.driver,locateType,locateExpression)
    def username(self):
        locateType, locateExpression = self.login_page_items['login_page.username'].split(">")
        return getElement(self.driver, locateType, locateExpression)

    def password(self):
        locateType, locateExpression = self.login_page_items['login_page.password'].split(">")
        return getElement(self.driver, locateType, locateExpression)

    def loginbutton(self):
        locateType, locateExpression = self.login_page_items['login_page.loginbutton'].split(">")
        return getElement(self.driver, locateType, locateExpression)