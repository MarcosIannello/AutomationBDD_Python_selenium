Feature: Alta Feriado automatizado.

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Alta Feriado
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en feriados
    When Click en boton crear feriados
    When Seleccionar fecha actual como feriado
    When Escribir descripcion del feriado "<descripcionFeriado>"
    When Click guardar feriado
    Then Validar Alta feriado


    Examples:
      | cuit        | password | descripcionFeriado        |
      | 27395625123 | Troquel1 |AltaAutomatizadaDeFeriado |