Feature: Verify basic authentication
  Scenario: Login authentication
    Given launch chrome browser
    When open the IH homepage
    Then click on basic auth
    When login with username and pass
    And verify that user logged in successfully
