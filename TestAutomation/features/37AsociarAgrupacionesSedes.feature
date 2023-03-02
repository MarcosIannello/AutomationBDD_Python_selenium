Feature: Asociar Agrupaciones Sedes a Perfiles

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Asociar Agrupaciones Sedes a Perfiles
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en perfiles
    When Filtrar por nombre Perfil "<Perfil>"
    When Click en asociar agrupacion sede
    When Seleccionar AgrupacionSede "<AgrupacionSede>"
    When Guardar asociacion
    Then Validar Asociacion agrupacion sedes

    Examples:
      | cuit        | password | Perfil              | AgrupacionSede                 |
      | 27395625123 | Troquel1 | PerfilAutomatizado2 | AltaAgrupacionSedeAutomatizada |