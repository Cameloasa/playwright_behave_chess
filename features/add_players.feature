# Som en användare vill jag lägga till namn på mig och min motspelare, så att vi kan ta tiden på våra drag.

Feature: Lägg till namn på spelare

  Scenario: Lägg till två spelare
    Given spelaren är på startsidan
    When spelaren klickar på "Lägg till spelare"
    And spelaren skriver "{Cami}" i textfälten
    And spelaren klickar på knappen "Lägg till spelare"
    Then "{Cami}" dycker upp på sidan med texten "0:00.0"
    When spelaren skriver "{Zoe}" i textfälten
    And spelaren klickar på knappen "Lägg till spelare"
    Then "{Zoe}" dycker upp på sidan med texten "0:00.0"