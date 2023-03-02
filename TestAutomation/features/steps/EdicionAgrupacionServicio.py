import time
from behave import *
from pages.AgrupacionServiciosPage import AgrupacionServiciosPage


@when(u'Filtrar por Nombre Agrupacion "{NombreAgrupacion}"')
def step_impl(context, NombreAgrupacion):
    try:
        AgrupacionServiciosPage.FiltrarXNombre(context, NombreAgrupacion)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Filtrar por Nombre Agrupacion"


@when(u'Editar nombre Agrupacion "{NombreAgrupacionEditado}"')
def step_impl(context, NombreAgrupacionEditado):
    try:
        AgrupacionServiciosPage.EditarNombre(context, NombreAgrupacionEditado)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Editar nombre Agrupacion"


@when(u'Seleccionar nuevos Servicios para agrupar')
def step_impl(context):
    try:
        AgrupacionServiciosPage.NuevosServicios(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar nuevos Servicios para agrupar"


@when(u'Click en guardar edicion "{NombreAgrupacionEditado}"')
def step_impl(context, NombreAgrupacionEditado):
    try:
        AgrupacionServiciosPage.GuardarEdicion(context, NombreAgrupacionEditado)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en guardar edicion"


@then(u'Validar Edicion agrupacion servicio')
def step_impl(context):
    try:
        AgrupacionServiciosPage.ValidateToastEdicionAgrupacionServicios(context)
        time.sleep(2)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Edicion agrupacion servicio"
