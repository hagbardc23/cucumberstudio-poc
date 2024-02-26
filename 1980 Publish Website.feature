@Functional @Regression @Feature1980 @wip
Feature: 1980 Publishing website to public domain
  As a user I want to publish my website to public domain
  website is hosted
  website has a unique url that the user can share with others
  user canNOT choose own URL
  user is able to share the link with a friend and friend can view website but not edit

  @Story_1980_Publish_Website_to_public-1
  Scenario: Published website can be opened by others
    Given I have published a website
    And I am not logged on
    When I open the website url
    Then I should see the website
