Feature: Inicio de sesion con datos validos.
  Background:
    Given  Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

    Scenario Outline: Login Fail
      When Escribiendo campo CUIT "<cuit>"
      When Escribiendo password "<password>"
      When Click en boton ingresar
      Then Validar pop up de credenciales incorrectas


       Examples:
         | cuit        | password |
         | 23432002209 | asdf     |
         | 23432002508 | asdf     |
         | 1111        | asdf     |
