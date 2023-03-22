Feature: Baja organismo automatizada

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Baja Organismo
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Organismos
    When Filtrar por nombre organismo "<nombreOrganismo>"
    When Click boton eliminar
    When Click confirmar eliminacion
    Then Validar Baja organismo


    Examples:
      | cuit        | password | nombreOrganismo           |
      | 27395625123 | Troquel1 | AltaOrganismoAutomatizada |