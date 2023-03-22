Feature: Alta Usuario automatizado.

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Alta Usuario
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Usuarios
    When Click en boton crear Usuarios
    When Completar campo Cuit "<nuevoUserCuit>"
    When Click en buscar por AD
    When Seleccionar rol del usuario "<rol>"
    When Seleccionar Organismo del usuario "<organismo>"
    When Click guardar Usuario
    Then Validar Alta usuario


    Examples:
      | cuit        | password | nuevoUserCuit | organismo             | rol        |
      | 27395625123 | Troquel1 | 23432002209   | OrganismoAutomatizado | BackOffice |
