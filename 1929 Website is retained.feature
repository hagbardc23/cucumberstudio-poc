@Functional @Regression @Feature1929
Feature: 1929 Website is retained after user logs out
  As a user, I want to edit my website after it is first generated and keep this for later use
  After the website is generated I want to be able to edit the contents of the website, like the generated texts and images. If if visit my website at a later point in time, I still want these changes to be reflected in my website. On the website editor, I want to be able to edit individual text components and images on my website.
  Editing of text and images is possible
  When a user refreshes the page or goes back to his/her website, I can still see the changes I made
  A user is able to upload their own images
  Images will be saved based on their "data-attribute-name" attributes
  Only images with the "data-editable-image" attribute are allowed to be changed
  A user is able to change. allowed, text fragments on his/her website
  Only texts with the "data-editable-text" attribute are allowed to be changed
  An intuitive UX design should be available on how to upload/edit images & edit my text
  Technical details:
  Images should be saved under their "data-attribute-name", for example, "about-image"
  The structure should look like "<customer_uuid>/images<image:data-attribute-name>.png"
  Templates should be updated to include the "data-editable-image" attribute on images a user may edit
  Templates should not contain the base64 encoded image content anymore and should make use of the image resource URL
  Website text will be updated by uploading the whole website content for now

  @Story_1929_Website-is-retained-1
  Scenario: Generated Page is available after logout
    Given I generate a website
    And I log out of the website
    And I log into the website
    When I go to the website editor
    Then I should see the generated website

  @Story_1929_Website-is-retained-2
  Scenario: Generated page retains edits made by the user
    Given I generate a website
    And I edit the website
    And I log out of the website
    And I log into the website
    When I go to the website editor
    Then I should see the edited website
