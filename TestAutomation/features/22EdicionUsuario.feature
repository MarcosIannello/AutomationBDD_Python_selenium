Feature: Edicion Usuario automatizado.

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Edicion Usuario
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Usuarios
    When Filtrar por cuit "<nuevoUserCuit>"
    When Click en editar
    When Cambiar rol y organismo "<organismo>" "<rol>"
    When Click guardar edicion Usuario
    Then Validar Alta edicion


    Examples:
      | cuit        | password | nuevoUserCuit | organismo                       | rol                  |
      | 27395625123 | Troquel1 | 23432002209   | OrganismoEditadoAutomaticamente | Actualizador Estados |