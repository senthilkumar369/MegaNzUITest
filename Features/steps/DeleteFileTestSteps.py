from behave import given,when,then
from pages import HomePage,FileManagerPage,LoginPage

"""
 Given  a text file with filename as <filename>
    When Search AND Delete the file in FILE_MANAGER
    Then it should be deleted successfully

"""

@given('a text file with filename as {filename}')
def delete_TC_001_001(context,filename):
    context.filename=filename
    context.filemanager=FileManagerPage.FileManagerPage(context.browser)
    context.filemanager.is_fileManager_page()

@when('Search AND Delete the file in FILE_MANAGER')
def delete_TC_001_002(context):
    context.filemanager.get_contextMenu()
    context.filemanager.delete_a_file_from_table_file_manager(context.filename)
@then('it should be deleted successfully')
def delete_TC_001_002(context):
    context.filemanager.confirm_file_not_exist(context.filename)