#encoding=utf-8
import time
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig
from Action.login import *
from Action.visit_address_page import *

class AddressPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parse_config_file = ParsePageObjectRepositoryConfig()
        self.address_page_items =self.parse_config_file.getElementsFromSection("163mail_addcontactspage")

    def add_contact_button(self):
        locateType,locateExpression = self.address_page_items("addcontacts_page.createcontactsbtn").split(">")
        return getElement(self.driver,locateType,locateExpression)

    def contact_name(self):
        locateType,locateExpression = self.address_page_items("addcontacts_page.contactpersonname").split(">")
        return getElement(self.driver,locateType,locateExpression)

    def contact_email(self):
        locateType,locateExpression = self.address_page_items("addcontacts_page.contactpersonemail").split(">")
        return getElement(self.driver,locateType,locateExpression)

    def contact_is_star(self):
        locateType,locateExpression = self.address_page_items("addcontacts_page.starcontacts").split(">")
        return getElement(self.driver,locateType,locateExpression)

    def contact_mobile(self):
        locateType,locateExpression = self.address_page_items("addcontacts_page.contactpersonmobile").split(">")
        return getElement(self.driver,locateType,locateExpression)

    def contact_other_info(self):
        locateType,locateExpression = self.address_page_items("addcontacts_page.contactpersoncomment").split(">")
        return getElement(self.driver,locateType,locateExpression)

    def contact_save_button(self):
        locateType,locateExpression = self.address_page_items("addcontacts_page.savecontaceperson").split(">")
        return getElement(self.driver,locateType,locateExpression)