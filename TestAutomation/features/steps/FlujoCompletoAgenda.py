import time
from behave import *
from pages.FlujoCompletoAgendaPage import FlujoCompletoAgendaPage


@when(u'Ingresar Nombre organismo "{Organismo}"')
def step_impl(context, Organismo):
    try:
        FlujoCompletoAgendaPage.InputNombreOrganismo(context, Organismo)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar Nombre organismo"


@when(u'Click guardar organismo automatizado "{Organismo}"')
def step_impl(context, Organismo):
    # try:
    FlujoCompletoAgendaPage.ClickGuardarOrganismo(context, Organismo)
    # except:
    #     context.driver.close()
    #     assert False, "La prueba fallo en: Click guardar organismo automatizado"


@when(u'Regreso a pagina principal1')
def step_impl(context):
    try:
        FlujoCompletoAgendaPage.VolverAlHome(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Regreso a pagina principal"


@when(u'Seleccionar organismo automatizado')
def step_impl(context):
    try:
        FlujoCompletoAgendaPage.SeleccionarOrganismo(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar organismo automatizado"


@when(u'Ingresar nombre de servicio "{Servicio}"')
def step_impl(context, Servicio):
    try:
        FlujoCompletoAgendaPage.ingresarNombreServicio(context, Servicio)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar nombre de servicio"


@when(u'Click Guardar servicio Automatizado "{Servicio}"')
def step_impl(context, Servicio):
    try:
        FlujoCompletoAgendaPage.GuardarServicio(context, Servicio)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click Guardar servicio Automatizado"


@when(u'Regreso a pagina principal2')
def step_impl(context):
    try:
        FlujoCompletoAgendaPage.VolverAlHome(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Regreso a pagina principal2"


@when(u'Ingresar nombre sede "{Sede}"')
def step_impl(context, Sede):
    try:
        FlujoCompletoAgendaPage.ingresarNombreSede(context, Sede)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar nombre sede"


@when(u'Click guardar Sede Automatizada "{Sede}"')
def step_impl(context, Sede):
    try:
        FlujoCompletoAgendaPage.GuardarSede(context, Sede)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click guardar Sede Automatizada"


@when(u'Regreso a pagina principal3')
def step_impl(context):
    try:
        FlujoCompletoAgendaPage.VolverAlHome(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Regreso a pagina principal"


@when(u'Seleccionar Sede automatizado')
def step_impl(context):
    try:
        FlujoCompletoAgendaPage.SeleccionarSede(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar Sede automatizado"


@when(u'Seleccionar Servicio automatizado')
def step_impl(context):
    try:
        FlujoCompletoAgendaPage.SeleccionarServicio(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar Sede automatizado"


@when(u'Regreso a pagina principal4')
def step_impl(context):
    try:
        FlujoCompletoAgendaPage.VolverAlHome(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Regreso a pagina principal4"


@when(u'Escribir Nombre Agenda Flujo Completo "{nombreAgenda}"')
def step_impl(context, nombreAgenda):
    try:
        FlujoCompletoAgendaPage.EscribirNombreAgenda(context, nombreAgenda)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Escribir Nombre Agenda Flujo Completo"


@when(u'Seleccionar Organismo, Servicio y sede automatizados')
def step_impl(context):
    try:
        FlujoCompletoAgendaPage.SeleccionarOrganismo_Servicio_Sede(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar Organismo, Servicio y sede automatizados"


@when(u'Click guardar Agenda flujo completo "{Agenda}"')
def step_impl(context, agenda):
    try:
        FlujoCompletoAgendaPage.GuardarAgenda(context, agenda)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click guardar Agenda flujo completo"


# @when(u'Filtrar por nombre Agenda')
# def step_impl(context):
#     FlujoCompletoAgendaPage
# # @when(u'Filtrar por nombre Agenda')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When Filtrar por nombre Agenda')
#



