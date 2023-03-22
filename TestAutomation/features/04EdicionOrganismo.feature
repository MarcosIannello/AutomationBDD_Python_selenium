Feature: Edicion de organismo automatizada

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Edicion Organismo
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Organismos
    When Filtrar por nombre organismo "<organismoAutomatizado>"
    When Click editar organismo
    When Editar nombre organismo por "<nombreEdicionOrganismo>"
    When Click Confirmar edicion "<nombreEdicionOrganismo>"
    Then Validar Edicion Organismo


    Examples:
      | cuit        | password | organismoAutomatizado     | nombreEdicionOrganismo          |
      | 27395625123 | Troquel1 | AltaOrganismoAutomatizada | OrganismoEditadoAutomaticamente |