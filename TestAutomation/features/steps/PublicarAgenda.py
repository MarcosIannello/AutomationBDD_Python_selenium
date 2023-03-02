from pages.AgendaPage import AgendaPage
from behave import *
import time


@when(u'Click en Publicar Agenda')
def step_impl(context):
    try:
        AgendaPage.publicarAgenda(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en Publicar Agenda"


@when(u'Click en aceptar')
def step_impl(context):
    try:
        AgendaPage.AceptarPublicacion(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en aceptar"


@then(u'Validar Publicacion de Agenda')
def step_impl(context):
    try:
        AgendaPage.ValidateToastPublicarAgenda(context)
        time.sleep(2)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar publicacion de agenda"
