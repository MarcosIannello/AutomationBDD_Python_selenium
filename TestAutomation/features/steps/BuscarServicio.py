from pages.BuscarServicioPage import BuscarServicioPage
from behave import *
import time


@when(u'Click en Buscar Servicio')
def step_impl(context):
    try:
        BuscarServicioPage.IraBuscarServicio(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en Buscar Ciudadano"


@when(u'Buscar por nombre de servicio "{Servicio}"')
def step_impl(context, Servicio):
    try:
        BuscarServicioPage.BuscadorServicio(context, Servicio)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Buscar por nombre de servicio"


@when(u'Click en Comenzar')
def step_impl(context):
    try:
        BuscarServicioPage.ClickComenzar(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en Comenzar"


@then(u"Modificar cuando se desarrolle completo")
def step_impl(context):
    BuscarServicioPage.SeleccionDeTurno(context)
    print("FALTA DESARROLLO LO CUAL IMPOSIBILITA CONTINUAR ESTE FLUJO")
    time.sleep(2)
    context.driver.close()

