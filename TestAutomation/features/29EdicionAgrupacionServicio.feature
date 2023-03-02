Feature: Edicion Agrupacion servicio

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Edicion Agrupacion servicio
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Agrupacion de servicios
    When Filtrar por Nombre Agrupacion "<NombreAgrupacion>"
    When Click en boton editar
    When Editar nombre Agrupacion "<NombreAgrupacionEditado>"
    When Seleccionar nuevos Servicios para agrupar
    When Click en guardar edicion "<NombreAgrupacionEditado>"
    Then Validar Edicion agrupacion servicio

    Examples:
      | cuit        | password | NombreAgrupacion                | NombreAgrupacionEditado    |
      | 27395625123 | Troquel1 | AgrupacionServiciosAutomatizada | EdicionAgrupacionServicios |

