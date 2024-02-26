@Functional @Regression @Feature1933
Feature: 1933 Portal
  Set up a framework for the portal, that has an overview of marketing recommendations and services
  An initial landing page for the website, that will advise users to either start the briefing or log in to check their already configured/available service
  New users will be routed to either start the briefing in the Website Service or register themselves to the platform
  After the briefing is completed user will still be asked to create an account
  New back-end service(s) will be required to save the user data, like briefing answers
  These/This service(s) data will also be used to give advice to the user (Hints/Tips)
  Existing users will be routed to a portal where all their services will be shown, including some hints or tips
  Hints/tips could include creating their first Social Media post
  Design for the landing page & portal
  there needs to be a "homepage" where the user can log in
  the homepage also needs to be a starting point for the briefing process (also when users are not logged in)
  when logged in the user lands on a page where, in the future, he/she will have access to his/her services, data, dashboards, payments, etc.
  for now, the user can only access the generated website, if any
  accessing the generated website opens the editor
  if no website is generated, the user can start the briefing process from here

  @Story_1933_Portal-1
  Scenario: Portal page is reached at login
    Given I am not logged in
    And I log into the website
    Then I should see the portal page
