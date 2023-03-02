import time
from behave import *
from pages.AgendaPage import AgendaPage


@when(u'Click en boton Borrar')
def step_impl(context):
    try:
        AgendaPage.BorrarAgenda(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en : Click en boton Borrar "


@then(u'Validar baja Agenda')
def step_impl(context):
    try:
        AgendaPage.ValidateToastBajaAGENDA(context)
        time.sleep(3)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en : Validar baja Agenda"
