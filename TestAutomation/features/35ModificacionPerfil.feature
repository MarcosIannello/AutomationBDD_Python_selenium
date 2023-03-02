Feature: Modificacion Perfil

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Modificacion Perfil
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en perfiles
    When Filtrar por nombre Perfil "<Perfil>"
    When Click en editar
    When Ingresar nuevo nombre perfil "<PerfilEditado>"
    When Click en guardar PerfilEditado "<PerfilEditado>"
    Then Validar Edicion perfil

    Examples:
      | cuit        | password | Perfil             | PerfilEditado                |
      | 27395625123 | Troquel1 | PerfilAutomatizado | PerfilEditadoAutomaticamente |