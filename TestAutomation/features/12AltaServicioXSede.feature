Feature: Alta ServicioXSede automatizado.

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Alta ServicioXSede
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en ServicioXSede
    When Click en boton crear ServicioXSede
    When Seleccionar Servicio "<servicioAutomatizado>"
    When Seleccionar Sede "<sedeAutomatizada>"
    When Ingresar cant maxima de turnos por ciudadano "<cantMaximaTurnos>"
    When Ingresar dias previos a la cita "<diasPreviosCita>"
    When Ingresar maxima disponibilidad de dias "<maxDisponibilidadDias>"
    When Click guardar ServicioXSede
    Then Validar Alta ServicioXSede


    Examples:
      | cuit        | password | sedeAutomatizada     | servicioAutomatizado | cantMaximaTurnos | diasPreviosCita | maxDisponibilidadDias |
      | 27395625123 | Troquel1 | AltaSedeAutomatizada | AltaServicioAutomatizado | 19               | 86              | 309                  |