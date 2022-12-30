Feature: Baja organismo automatizada
  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

    Scenario Outline: Baja Organismo
      When Escribiendo campo CUIT "<cuit>"
      When Escribiendo password "<password>"
      When Click en boton ingresar
      Then Click en Organismos
      When Filtrar por nombre organismo
      When Escribiendo filtro nombre nuevo organismo "<nuevoorganismo>"
      When Click boton eliminar
      When Click confirmar eliminacion
      Then Validar Baja organismo


      Examples:
        | cuit        | password | nuevoorganismo          |
        | 27395625123 | Troquel1 | AltaOrganismoAutomatizada |