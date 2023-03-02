import time
from behave import *
from pages.ServiciosXSedesPage import ServiciosXSedesPage


@when(u'Click en boton Eliminar ServicioxSede')
def step_impl(context):
    try:
        ServiciosXSedesPage.BajaServicioXSede(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en boton Eliminar ServicioxSede"


@then(u'Validar Baja ServicioXSede')
def step_impl(context):
    try:
        ServiciosXSedesPage.ValidateToastBAJAServicioXSede(context)
        time.sleep(3)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Baja ServicioXSede"

