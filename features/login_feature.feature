Feature: Login feature testing

  @testLogin
  Scenario Outline: Testing login feature with valid password
    Given user goes to saucedemo website
    And user fill valid login details with username <username> and password <password>
    Then user should be on homepage

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |

