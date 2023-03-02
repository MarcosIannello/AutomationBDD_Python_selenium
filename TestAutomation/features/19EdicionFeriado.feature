Feature: Edicion Feriado automatizado.

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Edicion Feriado
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en feriados
    When Filtrar por descripcion feriado "<descripcionFeriado>"
    When Click en editar
    When Escribir nueva descripcion del feriado editado "<descripcionEditadaFeriado>"
    When Click guardar
    Then Validar Edicion feriado


    Examples:
      | cuit        | password | descripcionFeriado        | descripcionEditadaFeriado |
      | 27395625123 | Troquel1 |AltaAutomatizadaDeFeriado | EdicionAutomatizadaDeFeriado |