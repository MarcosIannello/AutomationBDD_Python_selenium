Feature: Baja ServicioXSede automatizado.

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Baja ServicioXSede
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en ServicioXSede
    When Filtrar X Servicio y Sede "<sedeAutomatizada>" "<servicioAutomatizado>"
    When Click en boton Eliminar ServicioxSede
    When Confirmar Baja
    Then Validar Baja ServicioXSede

    Examples:
      | cuit        | password | sedeAutomatizada     | servicioAutomatizado |
      | 27395625123 | Troquel1 | AltaSedeAutomatizada | ServicioAutomatizado |