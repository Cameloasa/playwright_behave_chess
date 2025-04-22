Feature: Pausa spelet
  Som en användare vill jag kunna pausa spelet, så att vi kan pausa spelet tillsammans.

  Scenario: Pausa spelet
    Given spelet är i gång
    When spelaren klickar på knappen "Pausa"
    Then spelet ska visa att det är pausat

  Scenario: Återuppta spelet
    Given spelet är pausat
    When spelaren klickar på knappen "Pausa"
    Then spelet ska visa att det är återupptaget