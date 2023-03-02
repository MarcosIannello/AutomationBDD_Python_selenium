Feature: Baja Servicio automatizado.

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Baja Servicio
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en servicios
    When Filtrar por servicio automatizado "<nombreServicio>"
    When Click en boton eliminar
    When Confirmar Baja
    Then Validar baja servicio


    Examples:
      | cuit        | password | nombreServicio           |
      | 27395625123 | Troquel1 | AltaServicioAutomatizado |