Feature: Asignar Perfil a Usuario

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Asignar Perfil a Usuario
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Usuarios
    When Filtrar por cuit "<Cuit>"
    When Click en asignar perfil
    When Seleccionar perfil de la lista "<Perfil>"
    When Click guardar Asignacion
    Then Validar Asignacion perfil


    Examples:
      | cuit        | password | Cuit        | Perfil             |
      | 27395625123 | Troquel1 | 20337463836 | PerfilAutomatizado |