Feature: Inicio de sesion con datos validos.
  Background:
    Given  Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

    Scenario Outline: Se visualizan campos para iniciar sesion
      When Escribiendo campo CUIT "<cuit>"
      When Escribiendo password "<password>"
      When Click en boton ingresar
      When validar Inicio Sesion
      Then Click en cerrar sesion


       Examples:
      |cuit|password|
      |27395625123|Troquel1|
