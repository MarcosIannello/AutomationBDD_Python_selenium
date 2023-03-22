Feature: Alta SEDE automatizado.

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Alta SEDE
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Sedes
    When Click en boton crear Sedes
    When Escribiendo campo nombre sede "<nuevaSede>"
    When Escribiendo campo calle y altura "<direccion>"
    When Click guardar Sede
    Then Validar Alta sede


    Examples:
      | cuit        | password | nuevaSede            | direccion          |
      | 27395625123 | Troquel1 | AltaSedeAutomatizada | ALMAFUERTE AV. 528 |