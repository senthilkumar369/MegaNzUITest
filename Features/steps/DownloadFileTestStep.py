from behave import given,when,then
from pages import FileDownloadPage,HomePage,FileManagerPage,LoginPage

"""
 Given user Navigates to "https://www.mega.nz/sync" site
    When choose desired linux OS and click download
    Then file downloads successfully
"""

@when('user Navigates to "https://www.mega.nz/sync" site')
def download_001_001(context):
    context.homePage=HomePage.HomePage(context.browser)
    context.homePage.is_page_correct()
    context.homePage.acceptAll_cookies()
    context.filedownloadpage=FileDownloadPage.FileDownloadPage(context.browser)
    context.filedownloadpage.goto_sync_page()

@then('Selected linux OS download successfully')
def download_001_002(context):
    context.filedownloadpage.Linux_app_select_and_download()




