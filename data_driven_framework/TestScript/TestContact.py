#encoding=utf-8
from selenium import webdriver
from Util.log import *
from Util.FormatTime import *
import time
from Action.visit_address_page import *
from Action.add_contact import *
from Action.login import *
from ProjectVar.Var import *

import sys
reload(sys)
sys.setdefaultencoding("utf8")

pe = ParseExcel(test_data_excel_path)
pe.set_sheet_by_index(0)
rows = pe.get_all_rows()[1:]
for id,row in enumerate(rows):
    if row[is_executed_col_no].value=='y':
        username = row[username_col_no].value
        password = row[password_col_no].value
        driver = webdriver.Chrome(executable_path="D:\\soft\\chromedriver_win32\\chromedriver.exe")
        try:
            login(driver,username,password)
            visit_address_page(driver)
            pe.set_sheet_by_index(1)
            test_data_result_flag=True
            for id2,row in enumerate(pe.get_all_rows()[1:]):
                if row[7].value=='y':
                    try:
                        add_contact(driver,row[1].value,row[2].value,row[3].value,row[4].value,row[5].value)
                        pe.write_cell_content(id2+2,9,date_time())
                        assert row[assert_keyword_col_no].value in driver.page_source
                        pe.write_cell_content(id2+2,10,"pass")
                    except Exception,e:
                        pe.write_cell_content(id2+2,9,date_time())
                        pe.write_cell_content(id2 + 2, 10, "fail")
                        test_data_result_flag=False
                else:
                    pe.write_cell_content(id2 + 2, 10, u"忽略")
                    continue
            if test_data_result_flag==True:
                pe.set_sheet_by_index(0)
                pe.write_cell_content(id+2,test_result_col_no,u"成功")
            else:
                pe.set_sheet_by_index(0)
                pe.write_cell_content(id + 2, test_result_col_no, u"失败")
        except Exception,e:
            pe.set_sheet_by_index(0)
            pe.write_cell_content(id+2,test_result_col_no,"fail")
            info("error:"+e.message)
        time.sleep(3)
        driver.quit()
    else:
        pe.set_sheet_by_index(0)
        pe.write_cell_content(id+2,test_result_col_no,u"忽略")
        continue




