Feature: Edicion AGENDA automatizada.

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Edicion AGENDA
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Agenda
    When Filtrar por nombre "<nombreAgenda>"
    When Click en boton editar
    When Escribir Nuevo nombre Agenda "<nombreAgendaEditado>"
    When Click en Switch para cambiarlo de estado
    When Click guardar Agenda Editada
    Then Validar Edicion Agenda


    Examples:
      | cuit        | password | nombreAgenda       |  nombreAgendaEditado     |
      | 27395625123 | Troquel1 | AgendaAutomatizada | AgendaEditadaAutomaticamente  |