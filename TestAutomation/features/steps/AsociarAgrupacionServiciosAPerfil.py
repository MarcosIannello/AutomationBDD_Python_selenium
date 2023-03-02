from datetime import date
import time
from behave import *
from pages.PerfilPage import PerfilPage


@when(u'Click en asociar agrupacion servicios')
def step_impl(context):
    try:
        PerfilPage.ClickAsociarAServiciosAPerfil(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en asociar agrupacion servicios"


@when(u'Seleccionar AgrupacionServicios "{AgrupacionServicios}"')
def step_impl(context, AgrupacionServicios):
    try:
        PerfilPage.seleccionarAgrupacionServicio(context, AgrupacionServicios)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar AgrupacionServicios"


@when(u'Guardar asociacion agrupacion servicio a perfil')
def step_impl(context):
    try:
        PerfilPage.GuardarAsociacionServicios(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Guardar asociacion agrupacion servicio a perfil"


@then(u'Validar Asociacion agrupacion servicios')
def step_impl(context):
    try:
        PerfilPage.ValidateToastAsociacionAgrupacionServicioAPerfil(context)
        time.sleep(1)
        context.driver.close()
    except:
        assert False, "La prueba fallo en: Validar Asociacion agrupacion servicios"
