Feature: Edicion Agrupacion sedes

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Edicion Agrupacion sedes
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Agrupacion de Sedes
    When Filtrar por Nombre Agrupacion sede "<NombreAgrupacion>"
    When Click en boton editar
    When Editar nombre Agrupacion sede "<NombreAgrupacionEditado>"
    When Seleccionar nuevas sedes para agrupar
    When Click guardar edicion Agrupacion Sedes "<NombreAgrupacionEditado>"
    Then Validar Edicion agrupacion sedes

    Examples:
      | cuit        | password | NombreAgrupacion            | NombreAgrupacionEditado |
      | 27395625123 | Troquel1 | AgrupacionSedesAutomatizada | EdicionAgrupacionSedes  |