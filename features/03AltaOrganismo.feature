Feature: Alta Organismo automatizado.
  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

    Scenario Outline: Alta Organismo
      When Escribiendo campo CUIT "<cuit>"
      When Escribiendo password "<password>"
      When Click en boton ingresar
      When Click en Organismos
      When Click en boton crear organismo
      When Escribiendo campo nombre nuevo organismo "<nuevoorganismo>"
      When Click guardar organismo
      Then Validar Alta organismo


      Examples:
        | cuit        | password | nuevoorganismo          |
        | 27395625123 | Troquel1 | AltaOrganismoAutomatizada |

