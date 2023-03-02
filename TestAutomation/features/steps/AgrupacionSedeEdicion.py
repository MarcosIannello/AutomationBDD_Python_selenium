import time
from behave import *
from pages.AgrupacionSedesPage import AgrupacionSedesPage


@when(u'Filtrar por Nombre Agrupacion sede "{NombreAgrupacion}"')
def step_impl(context, NombreAgrupacion):
    try:
        AgrupacionSedesPage.filtrarXNombre(context, NombreAgrupacion)
    except:
        context.driver.close()
        assert False, "La prueba fallo en : Filtrar por Nombre Agrupacion sede"


@when(u'Editar nombre Agrupacion sede "{NombreAgrupacionEditado}"')
def step_impl(context, NombreAgrupacionEditado):
    try:
        AgrupacionSedesPage.EditarNombre(context, NombreAgrupacionEditado)
    except:
        context.driver.close()
        assert False, "La prueba fallo en : Editar nombre Agrupacion sede"


@when(u'Seleccionar nuevas sedes para agrupar')
def step_impl(context):
    try:
        AgrupacionSedesPage.nuevasSedes(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en : Seleccionar nuevas sedes para agrupar"


@when(u'Click guardar edicion Agrupacion Sedes "{NombreAgrupacionEditado}"')
def step_impl(context, NombreAgrupacionEditado):
    try:
        AgrupacionSedesPage.guardarAgrupacionSede(context, NombreAgrupacionEditado)
    except:
        context.driver.close()
        assert False, "La prueba fallo en : Click guardar edicion Agrupacion Sedes"


"""FINALIZAR CUANDO SOLUCIONEN EL BUG DE MODIFICACION DE AGRUPACION DE SEDES"""


@then(u'Validar Edicion agrupacion sedes')
def step_impl(context):
    try:
        AgrupacionSedesPage.ValidateToastEdicionAgrupacionSede(context)
        time.sleep(2)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en : Validar Edicion agrupacion sedes"
