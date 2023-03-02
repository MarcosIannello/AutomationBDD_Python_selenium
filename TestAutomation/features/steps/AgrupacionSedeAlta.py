import time
from behave import *
from pages.AgrupacionSedesPage import AgrupacionSedesPage


@when(u'Click en Agrupacion de sedes')
def step_impl(context):
    try:
        AgrupacionSedesPage.IrAgrupacionSedes(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en Agrupacion de sedes"


@when(u'Click en Crear Agrupacion Sedes')
def step_impl(context):
    try:
        AgrupacionSedesPage.CrearAgrupacionSedes(context)
    except:
        context.driver.close()
        assert False, "Click en Crear Agrupacion Sedes"


@when(u'Seleccionar Sedes que completaran la Agrupacion "{Sede}"')
def step_impl(context, Sede):
    try:
        AgrupacionSedesPage.SeleccionMultipleSedes(context, Sede)
    except:
        context.driver.close()
        assert False, "Seleccionar Sedes que completaran la Agrupacion"


@when(u'Click en guardar Agrupacion Sedes "{NombreAgrupacion}"')
def step_impl(context, NombreAgrupacion):
    try:
        AgrupacionSedesPage.GuardarAgrupacion(context, NombreAgrupacion)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en guardar Agrupacion Sedes"


@then(u'Validar alta agrupacion sedes')
def step_impl(context):
    try:
        AgrupacionSedesPage.ValidateToastAltaAgrupacionSede(context)
        time.sleep(1)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar alta agrupacion sedes"

