Feature: Buscar Ciudadano

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Buscar Ciudadano
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Buscar Ciudadano
    When Completar los filtros Cabezera "<TipoDocumento>" "<NroDocumento>" "<Genero>"
    When Click en boton Buscar
    When Completar cuando desarrollo este finalizado
    Then Validar busqueda

    Examples:
      | cuit        | password | TipoDocumento | NroDocumento | Genero    |
      | 27395625123 | Troquel1 | DNI           | 43200220     | Masculino |