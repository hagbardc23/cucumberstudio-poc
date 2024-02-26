@Functional @Regression @Feature1985 @wip
Feature: 1986 Frontend Text Validation on Editing
  As a user, when editing text on the generated website, I want my input to be validated so that it looks good on the website when submitting.
  Generated text now has a minimum and maximum word count. This is defined in the meta data file. When a user edits text in the generated website, the input needs to be validated a fitting character count for the edited page element.
  block input when max character is reached
  the user MUST NOT be able to type more characters than the defined maximum in the meta data file
  the number of characters MUST be higher or equal to the minimum defined in the meta data file
  if the input is not valid, a small message needs to be shown

  @Story_1985_Validation-On-Text-Editing-1
  Scenario: Successful text validation
    Given I am on the website editor page
    And I know the metadata for the page
    When I edit a section
    And the length of the text is less than the maximum
    And the length of the text is more than the minimum
    Then the edit should be accepted
    And the edited text should be shown on the website

  @Story_1985_Validation-On-Text-Editing-2
  Scenario: Successful text validation edge case maximum
    Given I am on the website editor page
    And I know the metadata for the page
    When I edit a section
    And the length of the text is exactly the maximum
    Then the edit should be accepted
    And the edited text should be shown on the website

  @Story_1985_Validation-On-Text-Editing-3
  Scenario: Unsuccessful text validation exceeding maximum
    Given I am on the website editor page
    And I know the metadata for the page
    When I edit a section
    And the length of the text is more than the maximum
    Then the edit should be rejected
    And the edited text should not be shown on the website
    And an error message should be shown

  @Story_1985_Validation-On-Text-Editing-4
  Scenario: Unsuccessful text validation edge case minimum
    Given I am on the website editor page
    And I know the metadata for the page
    When I edit a section
    And the length of the text is exactly the minimum
    Then the edit should be accepted
    And the edited text should be shown on the website

  @Story_1985_Validation-On-Text-Editing-5
  Scenario: Unsuccessful text validation below minimum
    Given I am on the website editor page
    And I know the metadata for the page
    When I edit a section
    And the length of the text is less than the minimum
    Then the edit should be rejected
    And the edited text should not be shown on the website
    And an error message should be shown
