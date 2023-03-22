Feature: Asignaciones a Perfil Flujo Completo

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Asignaciones a Perfil Flujo Completo
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en perfiles
    When Click en Crear
    When Ingresando Nombre Perfil "<Perfil>"
    When Click sobre boton guardar "<Perfil>"
    When Regreso a pagina principal1
    When Click en Agrupacion de sedes
    When Click en Crear Agrupacion Sedes
    When Ingresando nombre agrupacion sede "<AgrupacionSedes>"
    When Seleccionar Sedes que completaran la Agrupacion "<Sede>"
    When Click sobre boton guardar agrupacion Sedes "<AgrupacionSedes>"
    When Regreso a pagina principal2
    When Click en Agrupacion de servicios
    When Click en Crear Agrupacion
    When Ingresando nombre agrupacion servicios "<AgrupacionServicios>"
    When Seleccionar Servicios que completaran la Agrupacion "<Servicio>"
    When Click sobre boton guardar agrupacion servicios "<AgrupacionServicios>"
    When Regreso a pagina principal2
    When Click en perfiles
    When Filtrar por nombre Perfil
    When Click en asociar agrupacion sede
    When Seleccionar AgrupacionSede automatizada
    When Guardar asociacion agrupacion sede a perfil
    When Click en asociar agrupacion servicios
    When Seleccionar AgrupacionServicios automatizada
    When Guardar asociacion agrupacion servicio a perfil
    Then Validacion Final flujo

    Examples:
      | cuit        | password | Perfil     | AgrupacionSedes | Sede                 | AgrupacionServicios | Servicio                 |
      | 27395625123 | Troquel1 | PerfilAAEE | ASedeAAEE       | AltaSedeAutomatizada | AServiciosAAEE      | AltaServicioAutomatizado |