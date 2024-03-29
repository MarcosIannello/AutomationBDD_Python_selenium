Feature: Buscar servicio de agenda publicada

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Buscar servicio de agenda publicada
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Buscar Servicio
    When Buscar por nombre de servicio "<Servicio>"
    When Click en Comenzar
    Then Modificar cuando se desarrolle completo

    Examples:
      | cuit        | password | Agenda             | organismo                 | Servicio                 |
      | 27395625123 | Troquel1 | AgendaAutomatizada | AltaOrganismoAutomatizada | AltaServicioAutomatizado |