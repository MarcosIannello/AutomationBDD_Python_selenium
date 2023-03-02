Feature: Alta AGENDA automatizada.

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Alta AGENDA
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Agenda
    When Click en boton crear Agenda
    When Escribir Nombre Agenda "<nombreAgenda>"
    When Seleccionar Organismo, Servicio y sede "<organismoAutomatizado>" "<servicioAutomatizado>" "<sedeAutomatizada>"
    When Click guardar Agenda
    Then Validar Alta Agenda


    Examples:
      | cuit        | password | nombreAgenda       |  organismoAutomatizado     | servicioAutomatizado | sedeAutomatizada     |
      | 27395625123 | Troquel1 | AutomatizacionAgenda | AltaOrganismoAutomatizada  | AltaServicioAutomatizado | AltaSedeAutomatizada |