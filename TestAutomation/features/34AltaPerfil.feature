Feature: Alta Perfil

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Alta Perfil
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en perfiles
    When Click en Crear
    When Ingresar Nombre perfil "<Perfil>"
    When Click en guardar perfil "<Perfil>"
    Then Validar alta perfil

    Examples:
      | cuit        | password | Perfil             |
      | 27395625123 | Troquel1 | PerfilAutomatizado |