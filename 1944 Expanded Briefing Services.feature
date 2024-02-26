@Functional @Regression @Feature1944 @wip
Feature: 1944 Expanded services workflow
  As a user I want services to be displayed on my website, even if I do not enter them during the briefing, in order to show my customers what I can offer them
  Description:
  Currently, the services workflow is broken because the user is not required to enter a sufficient ammount of services during the briefing. This may mean that we are unable to fill the chosen template. We would have to either show an empty space or a lorem ipsum. The issue is further complicated by the fact that the user can also enter specialties or experises in the services input. This means that not every user input is guaranteed to be a service.
  Solution:
  We can address this by parsing the user input and generating additional services to fill the template if required. We can use a similar approach as we did for the portfolio and blog topics.
  the text-generation service MUST be extended with a /service-names endpoint that generates a list of N services
  the generated services MUST not already be present in the briefing services
  the text-generation service MUST be extended with a /service-description endpoint that generates a short text description for a given service name
  the template renderer MUST call the /service-names endpoint to generate missing services required to fill the template
  the template renderer MUST call the /service-description endpoint to generate text for each additional service

  @Story_1944_Expanded-Briefing-Services-1
  Scenario: Published website contains services I did not enter
    Given I have given only 1 service in the briefing
    When I start the website generation 
    And I open the website url
    Then I should see the service I entered
    And I should see additional services
