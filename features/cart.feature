Feature: Add product to cart

  Scenario: Search and add diapers to cart
    Given the app is launched
    When I click on the continue button in the launch screen
    And I am on the Explore tab
    And I search for diapers
    And I go to the first product PDP page
    And I add the product to the cart
    Then I should see the product in the cart
