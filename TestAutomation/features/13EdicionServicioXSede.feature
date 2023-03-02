Feature: Edicion ServicioXSede automatizado.

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Edicion ServicioXSede
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en ServicioXSede
    When Filtrar X Servicio y Sede "<sedeAutomatizada>" "<servicioAutomatizado>"
    When Click en boton Editar ServicioxSede
    When Editar cant maxima de turnos por ciudadano "<cantMaximaTurnosEditado>"
    When Editar dias previos a la cita "<diasPreviosCitaEditado>"
    When Editar maxima disponibilidad de dias "<maxDisponibilidadDiasEditado>"
    When Click guardar edicion
    Then Validar Edicion ServicioXSede


    Examples:
      | cuit        | password | sedeAutomatizada     | servicioAutomatizado | cantMaximaTurnosEditado | diasPreviosCitaEditado | maxDisponibilidadDiasEditado |
      | 27395625123 | Troquel1 | AltaSedeAutomatizada | ServicioAutomatizado | 20                      | 22                     | 528                          |