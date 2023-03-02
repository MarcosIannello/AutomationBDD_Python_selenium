Feature: Edicion SEDE automatizado.

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Edicion SEDE
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Sedes
    When Filtrar por nombre sede "<Sede>"
    When Click en boton editar sede
    When Editando nuevo nombre de sede "<nombreEditadoSede>"
    When Editando campo calle y altura "<direccion>"
    When Ingresar Descripcion "<descripcion>"
    When Click guardar Sede editada
    Then Validar edicion sede


    Examples:
      | cuit        | password | Sede                 | nombreEditadoSede       | direccion    | descripcion |
      | 27395625123 | Troquel1 | AltaSedeAutomatizada | EdicionSedeAutomatizada | Arenales 663 | Se Edito Esta sede mediante pruebas automatizadas |