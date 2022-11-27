Feature: Cart Page
  @Cart
  Scenario: I Buy products
    Given I am a logged in user
    And I am on the Inventory Page
    When I add to cart all the products under 20
    And I click the Cart button
    Then I am on the Cart Page
    And The Cart badge counter is 4
    When I click the Checkout button
    Then I am on the Checkout Step One Page
    When I input the first name
    And I input the last name
    And I input the Zip Code
    And I click the Continue button
    Then I am on the Checkout Step Two Page
    When I click Finish button
    Then I am on the Checkout Complete Page




