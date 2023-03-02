import time
from behave import *
from pages.AgrupacionServiciosPage import AgrupacionServiciosPage


@when(u'Click en Agrupacion de servicios')
def step_impl(context):
    try:
        AgrupacionServiciosPage.IrAAgrupacionServicio(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en Agrupacion de servicios"


@when(u'Click en Crear Agrupacion')
def step_impl(context):
    try:
        AgrupacionServiciosPage.CrearAgrupacion(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en Crear Agrupacion"


@when(u'Ingresar Nombre Agrupacion "{NombreAgrupacion}"')
def step_impl(context, NombreAgrupacion):
    try:
        AgrupacionServiciosPage.IngresarNombreAgrupacion(context, NombreAgrupacion)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar Nombre Agrupacion"


@when(u'Seleccionar Servicios que completaran la Agrupacion "{Servicio}"')
def step_impl(context, Servicio):
    try:
        AgrupacionServiciosPage.SeleccionMultipleServicios(context, Servicio)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar Servicios que completaran la Agrupacion"


@when(u'Click en guardar "{NombreAgrupacion}"')
def step_impl(context, NombreAgrupacion):
    try:
        AgrupacionServiciosPage.GuardarAgrupacion(context, NombreAgrupacion)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en guardar"


@then(u'Validar alta agrupacion servicio')
def step_impl(context):
    try:
        AgrupacionServiciosPage.ValidateToastAltaAgrupacionServicio(context)
        time.sleep(2)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar alta agrupacion servicio"
