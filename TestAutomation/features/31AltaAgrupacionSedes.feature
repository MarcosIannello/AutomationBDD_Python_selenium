Feature: Alta Agrupacion Sede

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Alta Agrupacion Sede
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Agrupacion de sedes
    When Click en Crear Agrupacion Sedes
    When Ingresar Nombre Agrupacion "<NombreAgrupacion>"
    When Seleccionar Sedes que completaran la Agrupacion "<Sede>"
    When Click en guardar Agrupacion Sedes "<NombreAgrupacion>"
    Then Validar alta agrupacion sedes

    Examples:
      | cuit        | password | NombreAgrupacion               | Sede                 |
      | 27395625123 | Troquel1 | AltaAgrupacionSedeAutomatizada | AltaSedeAutomatizada |
