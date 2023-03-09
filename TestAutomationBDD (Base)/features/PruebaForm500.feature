Feature: Inicio de pagina web
  Background:
    Given  Iniciando Navegador "https://openai.com/blog/chatgpt"

    Scenario Outline: Se visualizan campos para iniciar sesion
      When Ingresar Al chat
#      When Escribiendo password "<password>"
#      When Click en boton ingresar
#      When validar Inicio Sesion
#      Then Click en cerrar sesion


       Examples:
      |cuit|password|
      |27395625123|Troquel1|
