# Som en användare vill jag lägga till namn på mig och min motspelare, så att vi kan ta tiden på våra drag.

Feature: Lägg till namn på spelare
  As a user, I want to add names for myself and my opponent,
  so that we can time our moves.

  Scenario Outline: Lägg till två spelare
    Given spelaren är på startsidan
    When spelaren skriver "<player1>" som första spelaren
    And spelaren skriver "<player2>" som andra spelaren
    And spelaren klickar på "Lägg till spelare"
    Then "<player1>" visas på sidan med texten "0:00.0"
    And "<player2>" visas på sidan med texten "0:00.0"
    Examples:
      | player1 | player2 |
      | Ana     | Bob     |
      | Maria   | Alex    |

  Scenario: Försök att lägga till fără namn
    Given spelaren är på startsidan
    When spelaren klickar på "Lägg till spelare"
    Then ett felmeddelande visas

