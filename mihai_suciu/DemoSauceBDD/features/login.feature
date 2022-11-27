Feature: SauceDemo Login Page

  @first
  Scenario: Login with fake username and fake password
    Given I am on the Login Page
    When I input a fake username
    And I input a fake password
    And I click the Login button
    Then I receive the "Epic sadface: Username and password do not match any user in this service" error message

  @second
  Scenario: Login with valid username and fake password
    Given I am on the Login Page
    When I input a valid username
    And I input a fake password
    And I click the Login button
    Then I receive the "Epic sadface: Username and password do not match any user in this service" error message

  @third
  Scenario: Login with fake username and valid password
    Given I am on the Login Page
    When I input a fake username
    And I input a valid password
    And I click the Login button
    Then I receive the "Epic sadface: Username and password do not match any user in this service" error message

  @fourth
  Scenario: Login with valid username and valid password
    Given I am on the Login Page
    When I input a valid username
    And I input a valid password
    And I click the Login button
    Then I am logged in

