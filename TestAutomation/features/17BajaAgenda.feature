Feature: BAJA AGENDA automatizada.

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: BAJA AGENDA
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Agenda
    When Filtrar por nombre "<nombreAgenda>"
    When Click en boton Borrar
    When Confirmar baja
    Then Validar baja Agenda


    Examples:
      | cuit        | password | nombreAgenda           |
      | 27395625123 | Troquel1 | AltaAgendaAutomatizada |