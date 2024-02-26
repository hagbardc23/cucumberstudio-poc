@Functional @Regression @Feature1986 @wip
Feature: 1986 Frontend Image Validation
  As a user, when uploading my own image, I want my image to be validated so it looks good on the website.
  Users can upload their own images, and those images need to fit within the template. The dimensions in the meta-data need to be used for validation. No validation on resolution yet.
  Uploaded images should be validated against the dimensions in the meta-data file (or default values)
  It should only check if it has the same ratio, no check on resolution
  Images should not exceed 5 MB
  A message should be shown when images are not valid and they can not be uploaded

  @Story_1986_Image-Validation-1
  Scenario: Uploading a valid image
    Given I am on the upload page
    And I know the metadata for the page
    When I upload an image with the correct dimensions
    Then the image should be uploaded

  @Story_1986_Image-Validation-2
  Scenario: Uploading an invalid image
    Given I am on the upload page
    And I know the metadata for the page
    When I upload an image with the incorrect dimensions
    Then I should see an error message
    And the image should not be uploaded

  @Story_1986_Image-Validation-3
  Scenario: Uploading an image that is too large
    Given I am on the upload page
    And I know the metadata for the page
    When I upload an image that is too large
    Then I should see an error message
    And the image should not be uploaded
