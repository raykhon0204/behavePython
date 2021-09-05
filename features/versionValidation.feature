Feature: AB tasting

  Scenario: Validate the version number of the page
    Given launch chrome browser
    When open the IH homepage
    Then click on AB testing link
    Then verify the version number
    And close the browser