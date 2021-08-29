from behave import given,when,then
from pages import HomePage,FileManagerPage,LoginPage
import time

"""
@   Background steps for landing to Mega and login to the account
@     Given Open Mega Portal
@      When login with valid credentials
@      Then successfully landed to FileManager
 
"""
@given('Open Mega Portal')
def background_given_step(context):
    homepage = HomePage.HomePage(context.browser)
    homepage.acceptAll_cookies()
    homepage.is_page_correct()
    homepage.open_login_form()

@when('login with valid credentials')
def background_when_step(context):
    loginpage = LoginPage.LoginPage(context.browser)
    time.sleep(5)
    loginpage.loginWithValidUserNameAndPassword()

@then('it navigates to FileManager successfully')
def background_then_step(context):
    context.file_manage=FileManagerPage.FileManagerPage(context.browser)
    context.file_manage.is_fileManager_page()

"""
 Given create a file with a.txt
    When add text "megatesting"
    Then the text saves in the text file

"""


@given('create a text file with filename as {filename}')

def Test_case_001_01(context,filename):
    context.filename=filename
    context.file_manage.get_contextMenu()
    context.file_manage.select_file()
    context.file_manage.add_textFileName_and_create(filename)

@when('add text as {Test_text}')
def Test_case_001_01(context,Test_text):
    context.Test_text=Test_text
    context.file_manage.write_text_and_save(context.Test_text)

@then('it save the text file successfully')
def Test_case_001_01(context):
    context.file_manage.confirm_file_exist(context.filename)


