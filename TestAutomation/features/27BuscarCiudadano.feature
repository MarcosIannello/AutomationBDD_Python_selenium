Feature: Buscar Ciudadano

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

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