Feature: Baja Agrupacion servicio

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Baja Agrupacion servicio
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Agrupacion de servicios
    When Filtrar por Nombre Agrupacion "<NombreAgrupacion>"
    When Click en boton eliminar
    When Confirmar baja
    Then Validar Baja agrupacion servicio

    Examples:
      | cuit        | password | NombreAgrupacion                |
      | 27395625123 | Troquel1 | AgrupacionServiciosAutomatizada |
