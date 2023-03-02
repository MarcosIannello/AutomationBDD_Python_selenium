Feature: Alta Agrupacion servicio

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Alta Agrupacion servicio
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Agrupacion de servicios
    When Click en Crear Agrupacion
    When Ingresar Nombre Agrupacion "<NombreAgrupacion>"
    When Seleccionar Servicios que completaran la Agrupacion "<Servicio>"
    When Click en guardar "<NombreAgrupacion>"
    Then Validar alta agrupacion servicio

    Examples:
      | cuit        | password | NombreAgrupacion                | Servicio                 |
      | 27395625123 | Troquel1 | AgrupacionServiciosAutomatizada | AltaServicioAutomatizado |