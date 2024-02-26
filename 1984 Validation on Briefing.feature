@Functional @Regression @Feature1984
Feature: 1984 Frontend Validation on Briefing
  As a SmA agent I want the user's input to be validated so it can be used to properly generate content for the website.
  User input is not validated yet in the briefing process. You can type text where only numbers are allowed. This should not be possible.
  Inputting text in number fields should not be possible
  Text fields should only allow 255 characters. Users cannot exceed this when filling the field
  Fields with a maximum number of characters must contain a hint of the maximum number
  services: minimal 1 maximum 10
  required question should be filled otherwise not allowed to click next

  @Story_1984_Validation-in-Briefing-1
  Scenario Outline: Briefing questions with text input, successful validation
    Given I am on the briefing page <question>
    When I input <input> into the input field
    Then I should not see a validation error
    And the next button should be enabled
    Examples:
      | question                                                                            | input                                                                                                                                                                                                                                                           |
      | Hast du bereits eine Website?                                                       | https://mediaan.com                                                                                                                                                                                                                                             |
      | Hast du bereits eine Website?                                                       | https://abcdefg.de/abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdea |
      | Wie ist der Name deines Unternehmens?                                               | Mediaan                                                                                                                                                                                                                                                         |
      | Wie ist der Name deines Unternehmens?                                               | MediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMedia |
      | In welcher Region oder Stadt möchtest du Kunden ansprechen?                         | Braunschweig                                                                                                                                                                                                                                                    |
      | In welcher Region oder Stadt möchtest du Kunden ansprechen?                         | BraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBra |
      | In welcher Branche bist du tätig?                                                   | Webentwicklung                                                                                                                                                                                                                                                  |
      | In welcher Branche bist du tätig?                                                   | WebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWeb |
      | Welche drei wichtigsten Eigenschaften repräsentieren die Werte deines Unternehmens? | Pünktlichkeit, Zuverlässigkeit, Präzision                                                                                                                                                                                                                       |
      | Welche drei wichtigsten Eigenschaften repräsentieren die Werte deines Unternehmens? | LangerErsterEintragLangerErsterEintragLangerErsterEintragLangerErsterEintrag, LangerZweiterEintragLangerZweiterEintragLangerZweiterEintrag, LangerDritterEintragLangerDritterEintragLangerDritterEintragLangerDritterEintragLangerDritterEintragLangerDritterEi |

  @Story_1984_Validation-in-Briefing-2
  Scenario Outline: Briefing questions with text input, unsuccessful validation, too many characters
    Given I am on the briefing page <question>
    When I input <input> into the input field
    Then I should see a validation error
    And the next button should be disabled
    Examples:
      | question                                                                            | input                                                                                                                                                                                                                                                            |
      | Hast du bereits eine Website?                                                       | https://abcdefg.de/abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeaa |
      | Wie ist der Name deines Unternehmens?                                               | MediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaMediaa |
      | In welcher Region oder Stadt möchtest du Kunden ansprechen?                         | BraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraunschweigBraa |
      | In welcher Branche bist du tätig?                                                   | WebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWebentwicklungWeba |
      | Welche drei wichtigsten Eigenschaften repräsentieren die Werte deines Unternehmens? | LangerErsterEintragLangerErsterEintragLangerErsterEintragLangerErsterEintrag, LangerZweiterEintragLangerZweiterEintragLangerZweiterEintrag, LangerDritterEintragLangerDritterEintragLangerDritterEintragLangerDritterEintragLangerDritterEintragLangerDritterEia |

  @Story_1984_Validation-in-Briefing-3
  Scenario Outline: Briefing questions with number input, successful validation
    Given I am on the briefing page <question>
    When I input <input> into the input field
    Then I should not see a validation error
    And the next button should be enabled
    Examples:
      | question                                                         | input                                                                                                                                                                                                                                                           |
      | Wann wurde dein Unternehmen gegründet?                           | 1999                                                                                                                                                                                                                                                            |
      | Wie viele Teammitglieder möchtest du auf die Website vorstellen? | 1                                                                                                                                                                                                                                                               |
      | Wie viele Teammitglieder möchtest du auf die Website vorstellen? | 4                                                                                                                                                                                                                                                               |

  @Story_1984_Validation-in-Briefing-4
  Scenario Outline: Briefing questions with number input, unsuccessful validation
    Given I am on the briefing page <question>
    When I input <input> into the input field
    Then I should see a validation error
    And the next button should be disabled
    Examples:
      | question                               | input                                                                                                                                                                                                                                                            |
      | Wann wurde dein Unternehmen gegründet? | 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456 |

  @Story_1984_Validation-in-Briefing-5
  Scenario Outline: Briefing questions with chips input, successful validation
    Given I am on the briefing page <question>
    When I add <number> chips to the input field
    Then I should not see a validation error
    And the next button should be enabled
    Examples:
      | question                                                          | number |
      | Welche Produkte oder Dienstleistungen bietet dein Unternehmen an? | 1      |
      | Welche Produkte oder Dienstleistungen bietet dein Unternehmen an? | 6     |
      | Wer ist deine Zielgruppe?                                         | 1      |
      | Wer ist deine Zielgruppe?                                         | 6     |

  @Story_1984_Validation-in-Briefing-6
  Scenario Outline: Briefing questions with chips input, unsuccessful not enough chips
    Given I am on the briefing page <question>
    When I add <number> chips to the input field
    Then I should see a validation error
    And the next button should be disabled
    Examples:
      | question                                                          | number |
      | Welche Produkte oder Dienstleistungen bietet dein Unternehmen an? | 0      |
      | Wer ist deine Zielgruppe?                                         | 0      |

  @Story_1984_Validation-in-Briefing-7
  Scenario Outline: Briefing questions with chips input, unsuccessful too many chips
    Given I am on the briefing page <question>
    When I add <number> chips to the input field
    Then I should not be able to add more chips
    And the next button should be enabled
    Examples:
      | question                                                          | number |
      | Welche Produkte oder Dienstleistungen bietet dein Unternehmen an? | 6     |
      | Wer ist deine Zielgruppe?                                         | 6     |

  @Story_1984_Validation-in-Briefing-8
  Scenario Outline: Briefing questions with radio input, successful validation
    Given I am on the briefing page <question>
    When I select <input> in the input field
    Then I should not see a validation error
    And the next button should be enabled
    Examples:
      | question                                  | input          |
      | Wie möchtest du deinen Kunden ansprechen? | Formal (Sie)   |
      | Wie möchtest du deinen Kunden ansprechen? | Informell (Du) |

  @Story_1984_Validation-in-Briefing-9
  Scenario Outline: Required Briefing questions validation
    Given I am on the briefing page <question>
    When the input field is empty
    Then the next button should be disabled
    Examples:
      | question                                                                            |
      | Wie ist der Name deines Unternehmens?                                               |
      | In welcher Region oder Stadt möchtest du Kunden ansprechen?                         |
      | In welcher Branche bist du tätig?                                                   |
      | Wann wurde dein Unternehmen gegründet?                                              |
      | Wie viele Teammitglieder möchtest du auf die Website vorstellen?                    |
      | Welche Produkte oder Dienstleistungen bietet dein Unternehmen an?                   |
      | Wer ist deine Zielgruppe?                                                           |
      | Wie möchtest du deinen Kunden ansprechen?                                           |
