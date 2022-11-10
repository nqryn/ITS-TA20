Feature: Jules Sign In

  Scenario: Successful sign in with expired membership
    Given I am on the Sign In page
    When I input a valid email for expired membership
    And I input a valid password
    And I click the Log In button
    Then I receive the "This membership has expired." error message
    And I am still on the Sign In page

  Scenario: Fail sign in with fake email and password
    Given I am on the Sign In page
    When I input a fake email
    And I input a fake password
    And I click the Log In button
    Then I receive the "Invalid email/password combination" error message
    And I am still on the Sign In page

  Scenario: Fail sign in with correct email and wrong password
    Given I am on the Sign In page
    When I input a valid email for expired membership
    And I input a fake password
    And I click the Log In button
    Then I receive the "Invalid email/password combination" error message
    And I am still on the Sign In page


