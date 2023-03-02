from pages.AgendaPage import AgendaPage
from behave import *
import time


@when(u'Filtrar por nombre agenda, organismo y servicio "{Agenda}" "{organismo}" "{Servicio}"')
def step_impl(context, Agenda, organismo, Servicio):
    try:
        AgendaPage.FiltrarXComponenetesAgenda(context, Agenda, organismo, Servicio)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Filtrar por nombre agenda, organismo y servicio"


@when(u'Click en Configurar Registro Agenda')
def step_impl(context):
    try:
        AgendaPage.ConfiguracionAgenda(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en Configurar Registro Agenda"


@when(u'Seleccionar Dias de agenda')
def step_impl(context):
    try:
        AgendaPage.SeleccionarDias(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar Dias de agenda"


@when(u'Ingresar Duracion turno y confirmacion "{duracionTurno}"')
def step_impl(context, duracionTurno):
    try:
        AgendaPage.IngresarYConfirmarDuracionTurno(context, duracionTurno)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar Duracion turno y confirmacion"


@when(u'Ingresar Fechas vigencia desde y hasta')
def step_impl(context):
    try:
        AgendaPage.FechasDesdeYHasta(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar Fechas vigencia desde y hasta"


@when(u'Agregar franja horaria')
def step_impl(context):
    try:
        AgendaPage.AgregarFranjaHoraria(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Agregar franja horaria"


@when(u'Ingresar horario 1er turno y ultimo turno "{primerTurno}" "{ultimoTurno}"')
def step_impl(context, primerTurno, ultimoTurno):
    try:
        AgendaPage.IngresarPrimerYUltimoTurno(context, primerTurno, ultimoTurno)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar horario 1er turno y ultimo turno"


@when(u'Ingresar cantidad de turnos en simultaneo "{turnosSimultaneos}"')
def step_impl(context, turnosSimultaneos):
    try:
        AgendaPage.TurnosSimultaneos(context, turnosSimultaneos)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar cantidad de turnos en simultaneo"


@when(u'Click en Aceptar y Guardar configuracion de agenda')
def step_impl(context):
    try:
        AgendaPage.AceptarYGuardar(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Alta correcta de configuracion Agenda"


@then(u'Validar Alta correcta de configuracion Agenda')
def step_impl(context):
    try:
        AgendaPage.ValidateToastAltaConfiguracionAGENDA(context)
        time.sleep(2)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Alta correcta de configuracion Agenda"



