Feature: Login functionality

  Scenario: Login with valid credentials
    Given the app is launched
    When I click on the continue button in the launch screen
    And I click on the Account tab
    And I click on the Sign In button
    And I login with valid credentials
    Then I should be logged in successfully