Feature:BAJA SEDE automatizado.

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: BAJA SEDE
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Sedes
    When Filtrar mediante nombre sede "<nuevaSede>"
    When Click boton eliminar
    When Confirmar baja sede
    Then Validar Baja sede


    Examples:
      | cuit        | password | nuevaSede            |
      | 27395625123 | Troquel1 | AltaSedeAutomatizada |