Feature: Find out if it's Christmas or not
  As a person of celebration
  I want to know if it's Christmas
  So that I don't forget to celebrate.

  Background:
    Given I open the url "https://isitchristmas.com"

  Scenario: Page loads successfully
    Then I expect that the title contains "Is it Christmas?"

  Scenario: Main answer is visible
    Then I expect that element "a" is visible

  Scenario: Answer text is either YES or NO
    Then I expect that element "a" contains any of the texts "YES", "NO"

  Scenario: It's not Christmas (non-Dec 25)
    Then I expect that element "a" contains the text "NO"

  

  Scenario: Page has a link to GitHub
    Then I expect that element "a[href*='github']" exists

  Scenario: Clicking the answer does nothing (no navigation)
    When I click element "a"
    Then I expect that the url is "https://isitchristmas.com"

  Scenario: Page has no broken images
    Then I expect that all elements "img" have attribute "src" containing "http"

  Scenario: Footer exists
    Then I expect that element "footer" exists

  Scenario: Page is responsive on mobile
    When I resize the window to 375x667
    Then I expect that element "a" is visible

  Scenario: Page is responsive on desktop
    When I resize the window to 1920x1080
    Then I expect that element "a" is visible