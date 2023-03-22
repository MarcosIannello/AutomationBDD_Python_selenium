Feature: Baja Usuario automatizado.

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Baja Usuario
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Usuarios
    When Filtrar por cuit "<nuevoUserCuit>"
    When Borrar usuario
    When Confirmar Baja
    Then Validar baja usuario


    Examples:
      | cuit        | password | nuevoUserCuit|
      | 27395625123 | Troquel1 | 23432002209 |