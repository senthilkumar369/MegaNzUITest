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

-------------------------------------------------------------------------------------------

Please Note - Please install required libraries, please requiremenet.txt

Behave Allure command to run from command prompt

To run all the features available under feature folder 

To select browser , change browser=Chrome,Firefox or Edge
Output stores in -o Mega_test_run_Json


behave  -D browser=Chrome -f allure_behave.formatter:AllureFormatter  -o Mega_test_run_Json  -f pretty features/

To run a feature file, run the following command from the working directory.

behave  -D browser=Chrome -f allure_behave.formatter:AllureFormatter  -o Mega_test_run_Json  -f pretty features/TestCreateFile.feature


To run, failed test cases.

behave  -D browser=Firefox -f allure_behave.formatter:AllureFormatter  -o Mega_test_run_Json  -f pretty @rerun_failure.feature


To generate Report
allure generate report Mega_test_run_Json -o Mega_test_run_HTML_report

It generate Mega_test_run_HTML_report, open index.html using firefox browser.
