import time
from behave import *
from pages.AgrupacionSedesPage import AgrupacionSedesPage


@when(u'Click en Confirmar baja')
def step_impl(context):
    try:
        AgrupacionSedesPage.ConfirmarBaja(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en Confirmar baja"


@then(u'Validar Baja agrupacion sedes')
def step_impl(context):
    try:
        AgrupacionSedesPage.ValidateToastBajaAgrupacionSede(context)
        time.sleep(2)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Baja agrupacion sedes"
