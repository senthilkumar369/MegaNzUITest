Feature: Test file creation features

  Background: Login into Mega
      Given Open Mega Portal
      When login with valid credentials
      Then it navigates to FileManager successfully

@Chrome @Firefox

 Scenario Outline: This test to DELETE a text file and confirms deleted
    Given  a text file with filename as <filename>
    When Search AND Delete the file in FILE_MANAGER
    Then it should be deleted successfully
    Examples:
    |filename|
    | a.txt  |
