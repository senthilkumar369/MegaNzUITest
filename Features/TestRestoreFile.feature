Feature: Test file restore features

  Background: Login into Mega
      Given Open Mega Portal
      When login with valid credentials
      Then it navigates to FileManager successfully

  @Chrome @Firefox

 Scenario Outline: This test to RESTORE Files from RUBBISH BIN and confirm RESTORED
    Given  Restore text file with filename as <filename> in Rubbish Bin
    When Search AND RESTORE the file from RUBBISH Bin
    Then it should be RESTORED to FILE_MANAGER successfully
    Examples:
    |filename|
    | a.txt  |
