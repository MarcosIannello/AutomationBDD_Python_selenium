Feature: BAJA Agrupacion sedes

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: BAJA Agrupacion sedes
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Agrupacion de Sedes
    When Filtrar por Nombre Agrupacion sede "<NombreAgrupacion>"
    When Click en boton eliminar
    When Click en Confirmar baja
    Then Validar Baja agrupacion sedes

    Examples:
      | cuit        | password | NombreAgrupacion            |
      | 27395625123 | Troquel1 | AgrupacionSedesAutomatizada |