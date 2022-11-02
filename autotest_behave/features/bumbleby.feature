Feature: Testing Bumbleby UI for compliance with the technical specification

  Scenario Outline: Testing the UI of the Personal account page
    Given Launch Chrome browser
    When Open the Account login page
    And Enter login "<login>" and password "<password>"
    And Click on the Submit button
    And Click on the Profile button
    And Verify that the Last name field present on a page
    And Verify that the First name field present on a page
    And Verify that the Patronymic field present on a page
    And Verify that the Postal address field present on a page
    And Verify that the Email field present on a page
    And Verify that the Telephone field present on a pages
    And Verify that the Date of birth field present on a page
    And Verify that the Category field present on a page
    Then Bumbleby UI meets the technical specification

    Examples:
      | login                 | password |
      | sergey28290@yandex.ru | 3046fjbe |
