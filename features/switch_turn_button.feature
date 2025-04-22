# Som en användare vill jag att knappen ska ändra text till "Överlämna",
# så att jag vet att jag kan lämna över till min motspelare.
Feature: Ändra knapptext efter överlämning
  Som en användare vill jag att knappen ska visa nästa spelares namn,
  så att jag vet vem som står på tur.

  Scenario: Knappen visar nästa spelares namn efter överlämning
    Given två spelare "Ana" och "Bob" är tillagda
    And spelaren "Ana" har påbörjat sin tur
    Then knappen visar texten "Överlämna till Bob"
    When spelaren klickar på knappen "Överlämna till Bob"
    Then knappen visar texten "Överlämna till Ana"
    When spelaren klickar på knappen "Överlämna till Ana"
    Then knappen visar texten "Överlämna till Bob"