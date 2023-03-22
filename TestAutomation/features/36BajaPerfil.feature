Feature: Baja Perfil

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Baja Perfil
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en perfiles
    When Filtrar por nombre Perfil "<Perfil>"
    When Click en borrar
    When Click en confirmar Baja
    Then Validar Edicion Baja

    Examples:
      | cuit        | password | Perfil             |
      | 27395625123 | Troquel1 | PerfilAutomatizado |