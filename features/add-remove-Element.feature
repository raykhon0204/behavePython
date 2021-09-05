Feature: Adding and removing elements
  Scenario: add one element and remove it
    Given launch chrome browser
    When open the IH homepage
    Then click on Add/Remove Elements
    Then click on add element button
    When new element Delete is added
    Then click on Delete and remove the element
    And close the browser