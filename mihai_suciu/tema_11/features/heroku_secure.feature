Feature: Secure page

  Scenario:
    Given I am on the Login page
    When I input a valid username
    And I input a valid password
    And I click on the Login button
    Then I receive the "You logged into a secure area!" login message
    And I am on the Secure page
    When I click the Logout button
    Then I am on the Login page