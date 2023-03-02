import time
from behave import *
from pages.AgendaPage import AgendaPage


@when(u'Filtrar por nombre "{nombreAgenda}"')
def step_impl(context, nombreAgenda):
    try:
        AgendaPage.FiltrarNombreAgenda(context, nombreAgenda)
    except:
        context.driver.close()
        assert False, "La prueba fallo en:  Filtrar por nombre"


@when(u'Escribir Nuevo nombre Agenda "{nombreAgendaEditado}"')
def step_impl(context, nombreAgendaEditado):
    try:
        AgendaPage.NuevoNombreAgenda(context, nombreAgendaEditado)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Escribir Nuevo nombre Agenda "


@when(u'Click en Switch para cambiarlo de estado')
def step_impl(context):
    try:
        AgendaPage.CambiarEstadoSwitch(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en Switch para cambiarlo de estado"


@when(u'Click guardar Agenda Editada')
def step_impl(context):
    try:
        AgendaPage.GuardarEdicion(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click guardar Agenda Editada"


@then(u'Validar Edicion Agenda')
def step_impl(context):
    try:
        AgendaPage.ValidateToastEdicionAGENDA(context)
        time.sleep(3)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Edicion Agenda"

