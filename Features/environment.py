from behave import fixture
from behave import use_fixture
import os,json,sys
from env import ROOT_DIR
from selenium import webdriver
configFile = os.path.join(ROOT_DIR, "ConfigsObjects", "ObjectRepository.json")
with open(configFile) as f:
    config = json.load(f)



def get_browser(context,browser):
    print("browser name ", browser)
    if browser == "Chrome":
        # Initialize the browser with platform, browser, etc.
        context.browser = webdriver.Chrome(r'C:\Users\senthilk\Documents\MegaTest\Drivers\chromedriver.exe')
        return context.browser
    elif browser == "Firefox":
        context.browser = webdriver.Firefox(executable_path=r'C:\Users\senthilk\Documents\MegaTest\Drivers\geckodriver.exe')
        return context.browser
    elif browser == "Edge":
        context.browser = webdriver.Edge(executable_path=r'C:\Users\senthilk\Documents\MegaTest\Drivers\msedgedriver.exe')
        return context.browser
    else:
        # DEFAULT BROWSER -- IF Browser not specified by user/ Tesster
        context.browser = webdriver.Chrome(r'C:\Users\senthilk\Documents\MegaTest\Drivers\chromedriver.exe')
        return context.browser

def before_scenario(context,scenario):

    browser = context.config.userdata.get("browser", "chrome")
    context.browser = get_browser(context, browser)
    context.url = str(config["URL"]["homeURL"])
    context.browser.get(context.url)
    context.browser.implicitly_wait(20)




def main():
    pass
    #setup(context)

if __name__ == "__main__":
    main()
