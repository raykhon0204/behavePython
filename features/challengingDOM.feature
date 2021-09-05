Feature: Challenging DOM
  Scenario: Verify number of rows in table
    Given launch chrome browser
    When open the IH homepage
    Then click on Challenging DOM link
    And verify the number of rows


  Scenario: Verify canvas element
    Given launch chrome browser
    When open the IH homepage
    Then click on Challenging DOM link
    And Verify the canvas element exists