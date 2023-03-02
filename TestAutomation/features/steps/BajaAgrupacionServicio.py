import time
from behave import *
from pages.AgrupacionServiciosPage import AgrupacionServiciosPage


@then(u'Validar Baja agrupacion servicio')
def step_impl(context):
    try:
        AgrupacionServiciosPage.ValidateToastBajaAgrupacionServicios(context)
        time.sleep(2)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Baja agrupacion servicio"
