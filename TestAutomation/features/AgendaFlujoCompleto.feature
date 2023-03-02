Feature: Flujo completo Agenda.

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Flujo completo Agenda

    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Organismos
    When Click en boton crear organismo
    When Ingresar Nombre organismo "<Organismo>"
    When Click guardar organismo automatizado "<Organismo>"
    When Regreso a pagina principal1
    When Click en servicios
    When Click en boton crear servicio
    When Seleccionar organismo automatizado
    When Ingresar nombre de servicio "<Servicio>"
    When Ingresar cantidad maxima de turnos por ciudadano "<cantMaximaTurnos>"
    When Ingresar tiempo Pre-Cancelacion cita "<tiempoPreCancelacion>"
    When Ingresar tiempo espera para toma turno "<tiempoEspera>"
    When Ingresar URL "<url>"
    When Seleccionar servicio de cancelacion
    When Seleccionar si requiere Login Con Miba
    When Seleccionar Documento admitido
    When Seleccionar orden de preferencia "<lugar>" "<fecha>" "<proximo>"
    When Click Guardar servicio Automatizado "<Servicio>"
    When Regreso a pagina principal2
    When Click en Sedes
    When Click en boton crear Sedes
    When Ingresar nombre sede "<Sede>"
    When Escribiendo campo calle y altura "<direccion>"
    When Click guardar Sede Automatizada "<Sede>"
    When Regreso a pagina principal3
    When Click en ServicioXSede
    When Click en boton crear ServicioXSede
    When Seleccionar Servicio automatizado
    When Seleccionar Sede automatizado
    When Ingresar cant maxima de turnos por ciudadano "<cantMaximaTurnos>"
    When Ingresar dias previos a la cita "<diasPreviosCita>"
    When Ingresar maxima disponibilidad de dias "<maxDisponibilidadDias>"
    When Click guardar ServicioXSede
    When Regreso a pagina principal4
    When Click en Agenda
    When Click en boton crear Agenda
    When Escribir Nombre Agenda Flujo Completo "<nombreAgenda>"
    When Seleccionar Organismo, Servicio y sede automatizados
    When Click guardar Agenda flujo completo "nombreAgenda"
    When Filtrar por nombre Agenda
    When Click en Configurar Registro Agenda
    When Seleccionar Dias de agenda
    When Ingresar Duracion turno y confirmacion "<duracionTurno>"
    When Ingresar Fechas vigencia desde y hasta
    When Agregar franja horaria
    When Ingresar horario 1er turno y ultimo turno "<primerTurno>" "<ultimoTurno>"
    When Ingresar cantidad de turnos en simultaneo "<turnosSimultaneos>"
    When Click en Aceptar y Guardar configuracion de agenda




    Examples:
      | cuit        | password | Organismo | Servicio    | cantMaximaTurnos | tiempoPreCancelacion | tiempoEspera | url                       | Sede      | direccion          | cantMaximaTurnos | diasPreviosCita | maxDisponibilidadDias | nombreAgenda | duracionTurno | primerTurno | ultimoTurno | turnosSimultaneos | proximo | fecha | lugar |
      | 27395625123 | Troquel1 | OTestAutomation | SerTestAuto | 22               | 120                  | 22           | https://www.google.com.ar | STestAuto | ALMAFUERTE AV. 528 | 19               | 86              | 309                   | TestAgenda   | 20            | 10:00 AM    | 11:00 AM    | 2                 | Próximo | Fecha | Lugar |



