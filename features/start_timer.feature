# Som en användare vill jag kunna starta tidtagningen

Feature: Starta och stoppa tidtagning
  As a user, I want to start and stop the timer by clicking buttons,
  so that each player's time is tracked accurately.

  Scenario: Starta timern för första spelaren
    Given två spelare "Ana" och "Bob" är tillagda
    When spelaren klickar på knappen "Börja ditt drag"
    Then timern för "Ana" börjar räkna
    And knappen visar texten "Överlämna till Bob"


  Scenario: Överlämna turen till andra spelaren
    Given spelaren "Ana" har påbörjat sin tur
    When spelaren klickar på knappen "Överlämna till Bob"
    Then timern för "Ana" slutar räkna
    And timern för "Bob" börjar räkna
    And knappen visar texten "Överlämna till Ana"