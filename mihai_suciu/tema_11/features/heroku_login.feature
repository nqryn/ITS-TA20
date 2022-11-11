Feature: Login page

  Scenario: Fail login with fake username
    Given I am on the Login page
    When I input a fake username
    And I input a valid password
    And I click on the Login button
    Then I receive the "Your username is invalid!" error message
    And I am still on the Login page

  Scenario: Fail login with fake password
    Given I am on the Login page
    When I input a valid username
    And I input a fake password
    And I click on the Login button
    Then I receive the "Your password is invalid!" error message
    And I am still on the Login page

  Scenario: Successful login with valid username and password
    Given I am on the Login page
    When I input a valid username
    And I input a valid password
    And I click on the Login button
    Then I receive the "You logged into a secure area!" login message
    And I am on the Secure page
