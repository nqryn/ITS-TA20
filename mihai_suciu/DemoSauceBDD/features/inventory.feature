Feature: Inventory Page
    @IP1
    Scenario: Add products to Cart and verify the Cart
      Given I am a logged in user
      And I am on the Inventory Page
      When I click product_1 button
      Then I am on the product_1 page
      When I click the Add to Cart button
      Then The product Add to Cart button changes to Remove
      And The Cart badge is increased

    @IP2
    Scenario: Remove one product from Cart
      Given I am a logged in user
      And I am on the Inventory Page
      When I click product_1 Add to Cart button
      Then The Remove button is displayed
      When I click product_1 Remove button
      Then The product button changes to Add to Cart

    @IP3
    Scenario: Add to cart all the products with prices under 20
      Given I am a logged in user
      And I am on the Inventory Page
      When I add to cart all the products under 20
      Then The Cart badge counter is 4
