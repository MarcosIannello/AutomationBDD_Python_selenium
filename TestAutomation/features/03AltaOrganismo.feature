Feature: Alta Organismo automatizado.

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Alta Organismo
    #noinspection CucumberUndefinedStep
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Organismos
    When Click en boton crear organismo
    When Escribiendo campo nombre nuevo organismo "<organismo>"
    When Click guardar organismo
    Then Validar Alta organismo


    Examples:
      | cuit        | password | organismo                 |
      | 27395625123 | Troquel1 | AltaOrganismoAutomatizada |