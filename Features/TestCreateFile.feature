Feature: Test file creation features

  Background: Login into Mega
      Given Open Mega Portal
      When login with valid credentials
      Then it navigates to FileManager successfully

  @Chrome @Firefox

 Scenario Outline: This test to create a text file and saves successfully
    Given create a text file with filename as <filename>
    When add text as <Test_text>
    Then it save the text file successfully
    Examples:
    |filename|Test_text|
    | a.txt  | megatesting|
