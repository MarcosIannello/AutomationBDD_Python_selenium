Feature: Asociar Agrupaciones Servicios a Perfiles

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Asociar Agrupaciones Servicios a Perfiles
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en perfiles
    When Filtrar por nombre Perfil "<Perfil>"
    When Click en asociar agrupacion servicios
    When Seleccionar AgrupacionServicios "<AgrupacionServicios>"
    When Guardar asociacion agrupacion servicio a perfil
    Then Validar Asociacion agrupacion servicios

    Examples:
      | cuit        | password | Perfil             |  AgrupacionServicios             |
      | 27395625123 | Troquel1 | PerfilAutomatizado4 |  AgrupacionServiciosAutomatizada |