#encoding=utf-8
import os
project_path=os.path.dirname(os.path.dirname(__file__))

page_object_repository_path = project_path.decode("utf-8")+u"\\Conf\\PageObjectRepository.ini"

test_data_excel_path = project_path.decode("utf-8")+u"\\TestData\\testExcel.xlsx"
username_col_no=1
password_col_no=2
is_executed_col_no=4
test_result_col_no=6
assert_keyword_col_no=7
