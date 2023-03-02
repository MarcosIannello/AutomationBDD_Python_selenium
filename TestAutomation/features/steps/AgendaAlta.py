import time
from behave import *
from pages.AgendaPage import AgendaPage


@when(u'Click en Agenda')
def step_impl(context):
    try:
        AgendaPage.IraAgenda(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en:Click en Agenda"


@when(u'Click en boton crear Agenda')
def step_impl(context):
    try:
        AgendaPage.CrearAgenda(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en boton crear Agenda"


@when(u'Escribir Nombre Agenda "{nombreAgenda}"')
def step_impl(context, nombreAgenda):
    try:
        AgendaPage.EscribirNombreAgenda(context, nombreAgenda)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Escribir Nombre Agenda"


@when(u'Seleccionar Organismo, Servicio y sede "{organismoAutomatizado}" "{servicioAutomatizado}" "{sedeAutomatizado}"')
def step_impl(context, organismoAutomatizado, servicioAutomatizado, sedeAutomatizado):
    try:
        AgendaPage.SeleccionarOrganismo_Servicio_Sede(context, organismoAutomatizado, servicioAutomatizado, sedeAutomatizado)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar Organismo, Servicio y sede"


@when(u'Click guardar Agenda')
def step_impl(context):
    try:
        AgendaPage.GuardarAgenda(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click guardar Agenda"


@then(u'Validar Alta Agenda')
def step_impl(context):
    try:
        AgendaPage.ValidateToastAltaAGENDA(context)
        time.sleep(3)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Alta Agenda"
