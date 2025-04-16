# Som en användare vill jag dölja rutan för att lägga till fler spelare när vi är igång,
# så att jag inte blir distraherad.

Feature: Dölja formuläret som visas lägg till spelare
  As a user, I want to hide the input field for adding players when the game start
  so that I am not distracted

  Scenario: Dölja formuläret
    Given spelaren är på startsidan
    And knappen "Lägg till spelare" är synlig
    When spelaren klickar på knappen "Lägg till spelare"
    Then formuläret för att lägga till spelare visas
    When spelaren klickar pe knappen "Dölj"
    Then formuläret för att lägga till spelare inte visas
    And knappen "Lägg till spelare" är synlig
