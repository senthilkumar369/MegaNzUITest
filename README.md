# MegaNzUITest
# MegaNzUITest
This project test the Create/Delete/Restore and Download a file using Python Behave BDD Selenium

I have implemented Page Object Model for maintaining the based methods of the web pages. The available pages,Methods,Object repository created for supporting the current test case execution that means not coverd for all pages,all webelements.

As this project  contains combination of BDD Framework + Page Object Model, the framework structure conatins the following folders -Features, Steps, Pages, ConfigObjects,Drivers and Libs.

Feature folder contains Feature file which is in Gherkin language(Given,When,And & Then)
Steps folder defines the steps of each scenarios, each step utlises the page objects.

Config Object repository folder contains a Json which have all the Object identifiers


Drivers directory contains the chrome, Edge and firefox driver for Windows

requirements.txt file contains all the python packages needed to run this framework

reports_json directory contains the json files generated with allure reports

Final Report contains HTML report of the result
