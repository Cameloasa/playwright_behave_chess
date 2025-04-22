Feature: Pauza i spelet
  Som en användare vill jag kunna pausa spelet, så att vi kan pausa spelet tillsammans.

  Scenario: Pausarea spelet
    Given spelet är i gång
    When spelaren klickar på knappen "Pausa"
    Then spelet ska pausa och timern ska stanna

  Scenario: Återuppta spelet
    Given spelet är pausat
    When spelaren klickar på knappen "Pausa"
    Then spelet ska återupptas och timern ska börja igen