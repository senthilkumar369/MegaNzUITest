from behave import given,when,then
from pages import HomePage,FileManagerPage,LoginPage,RubbishBinPage

"""
  Given  a text file with filename as <filename>
    When Search AND RESTORE the file from RUBBISH Bin
    Then it should be RESTORED to FILE_MANAGER successfully
"""

@given('Restore text file with filename as {filename} in Rubbish Bin')
def restore_001_001(context,filename):
    context.filename = filename
    context.filemanager=FileManagerPage.FileManagerPage(context.browser)
    context.filemanager.goto_rubbish_bin_page()
    context.rubbishPage = RubbishBinPage.RubbishBinPage(context.browser)


@when('Search AND RESTORE the file from RUBBISH Bin')
def restore_001_002(context):
    context.rubbishPage = RubbishBinPage.RubbishBinPage(context.browser)
    context.rubbishPage.find_and_restore_files(context.filename)

@then('it should be RESTORED to FILE_MANAGER successfully')
def restore_001_003(context):
    context.rubbishPage.goto_clouddrive()
    context.filemanager.confirm_file_exist(context.filename)