# Som en användare vill jag lägga till namn på mig och min motspelare, så att vi kan ta tiden på våra drag.

Feature: Lägg till namn på spelare
  As a user, I want to add names for myself and my opponent,
  so that we can time our moves.

  Scenario Outline: Lägg till två spelare
    Given spelaren är på startsidan
    When spelaren klickar på knappen "Lägg till spelare"
    And spelaren skriver "<name1>" i textfältet
    And spelaren klickar på knappen "Lägg till spelare"
    Then "<name1>" dyker upp på sidan med texten "0:00.0"
    When spelaren skriver "<name2>" i textfältet
    And spelaren klickar på knappen "Lägg till spelare"
    Then "<name2>" dyker upp på sidan med texten "0:00.0"
    Examples:
      | name1 | name2 |
      | Ana   | Bob   |
      | Maria | Alex  |

  Scenario: Försök att lägga till utan namn
    Given spelaren är på startsidan
    When spelaren klickar på knappen "Lägg till spelare"
    Then ingen spelare tillagd