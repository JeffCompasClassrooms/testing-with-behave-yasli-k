Feature: Peppers Ghost DIY Project – custom steps
  As a Halloween enthusiast
  I want a reliable Instructables page
  So that I can build my own ghost illusion

  Background:
    Given I open the Peppers Ghost Instructables page

  Scenario: Page title is correct
    Then the page title contains "Pepper's Ghost Illusion"

  Scenario: Main heading is visible
    Then the heading "Pepper's Ghost Illusion in a Small Space" is visible

  Scenario: At least one picture exists
    Then I expect that there is at least one picture there

  Scenario: Author name is shown
    Then the author name is displayed

  Scenario: Project contains many steps
    Then the project has at least 5 steps

  Scenario: Related Instructables section appears at the bottom
    When I scroll to the bottom of the page
    Then I see the "Related Instructables" section

  Scenario: First step image opens a modal
    When I click the first step image
    Then a larger image modal opens

  Scenario: Modal can be closed
    When I click the first step image
    And a larger image modal opens
    Then the modal can be closed with the close button

  Scenario: Search for the word "mirror" highlights it
    When I search the page for the word "mirror"
    Then the word "mirror" is highlighted

  Scenario: Download PDF opens a new tab
    When I click the "Download PDF" button
    Then a new tab with a PDF opens

  # ----- additional coverage scenarios -----
  Scenario: Page loads under 5 seconds
    Then I expect that the page load time is less than 5 seconds

  Scenario: All step images are visible
    Then I expect that all elements ".step-image img" are visible

  Scenario: No broken images
    Then I expect that no element "img" has attribute "src" containing "broken"

  Scenario: The project has a license badge
    Then I expect that element ".license-badge" exists

  Scenario: The "Comments" section is present
    Then I expect that element "#comments" exists