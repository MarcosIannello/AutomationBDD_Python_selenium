Feature: Edicion Agrupacion servicio

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

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

