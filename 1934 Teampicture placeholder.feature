@Functional @Regression @Feature1934 @wip
Feature: 1934 Placeholder for Team picture
  As a user I want to see static image with call to action for the space where my team photo or personal photo should be, with a call to action, so I understand immediately that this is where I'm supposed to upload my picture and how

  @Story_1934_Teampicture-placeholder-1
  Scenario: Generated Page includes placeholder for team picture
    Given I generate a website
    And I am on the website editor page
    Then I should see a placeholder for team picture
