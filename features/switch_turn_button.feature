Feature: Ändra knapptext efter överlämning

  Scenario: Knappen visar nästa spelares namn efter överlämning
    Given två spelare "Ana" och "Bob" är tillagda
    And spelaren "Ana" har påbörjat sin tur
    When spelaren klickar på knappen "Överlämna"
    Then knappen visar texten "Överlämna till Bob"
    When spelaren klickar på knappen "Överlämna"
    Then knappen visar texten "Överlämna till Ana"