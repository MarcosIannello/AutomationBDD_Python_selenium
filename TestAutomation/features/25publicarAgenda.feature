Feature: Publicar Agenda automatizada.

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Publicar AGENDA
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Agenda
    When Filtrar por nombre agenda, organismo y servicio "<Agenda>" "<organismo>" "<Servicio>"
    When Click en Publicar Agenda
    When Click en aceptar
    Then Validar Publicacion de Agenda

    Examples:
      | cuit        | password | Agenda             | organismo                 | Servicio                 |
      | 27395625123 | Troquel1 | AgendaAutomatizada | AltaOrganismoAutomatizada | AltaServicioAutomatizado |