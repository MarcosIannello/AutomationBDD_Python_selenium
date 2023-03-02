Feature: Edicion Servicio automatizado.

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Edicion Servicio
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en servicios
    When Filtrar por servicio automatizado "<nombreServicio>"
    When Click en boton editar
    When Ingresar un nuevo nombre de servicio "<nombreEditadoServicio>"
    When Ingresar nueva cantidad maxima de turnos "<cantMaximaTurnos>"
    When Click en Guardar edicion servicio "<nombreEditadoServicio>"
    Then Validar edicion servicio


    Examples:
      | cuit        | password | nombreServicio       | nombreEditadoServicio       | cantMaximaTurnos |
      | 27395625123 | Troquel1 | ServicioAutomatizado | EdicionAutomatizadaServicio | 1986             |