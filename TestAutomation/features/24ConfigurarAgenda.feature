Feature: Configurar Agenda automatizada.

  Background:
    Given Iniciando Navegador "https://baturnos-backoffice-preqa.gcba.gob.ar/"

  Scenario Outline: Configuracion AGENDA
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en Agenda
    When Filtrar por nombre agenda, organismo y servicio "<Agenda>" "<organismo>" "<Servicio>"
    When Click en Configurar Registro Agenda
    When Seleccionar Dias de agenda
    When Ingresar Duracion turno y confirmacion "<duracionTurno>"
    When Ingresar Fechas vigencia desde y hasta
    When Agregar franja horaria
    When Ingresar horario 1er turno y ultimo turno "<primerTurno>" "<ultimoTurno>"
    When Ingresar cantidad de turnos en simultaneo "<turnosSimultaneos>"
    When Click en Aceptar y Guardar configuracion de agenda
    Then Validar Alta correcta de configuracion Agenda

    Examples:
      | cuit        | password | Agenda               | organismo                 | Servicio                 | duracionTurno | primerTurno | ultimoTurno | turnosSimultaneos |
      | 27395625123 | Troquel1 | AutomatizacionAgenda | AltaOrganismoAutomatizada | AltaServicioAutomatizado | 20            | 10:00 AM    | 11:00 AM    | 2                 |