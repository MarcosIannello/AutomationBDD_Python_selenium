Feature: Baja Feriado automatizado.

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Baja Feriado
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en feriados
    When Filtrar por descripcion feriado "<descripcionEditadaFeriado>"
    When Click en borrar
    When Confirmar Baja
    Then Validar Baja feriado


    Examples:
      | cuit        | password | descripcionEditadaFeriado |
      | 27395625123 | Troquel1 | EdicionAutomatizadaDeFeriado |