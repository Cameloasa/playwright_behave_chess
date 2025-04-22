# Som en användare vill jag kunna starta tidtagningen
Feature: Starta och stoppa tidtagning
  As a user, I want to start and stop the timer by clicking buttons,
  so that each player's time is tracked accurately.

  Scenario: Överlämna turen till andra spelaren
    Given spelaren "Ana" har påbörjat sin tur
    When spelaren klickar på knappen "Överlämna till Bob"
    Then timern för "Bob" börjar räkna
    And knappen visar texten "Överlämna till Ana"