from datetime import date
import time
from behave import *
from pages.PerfilPage import PerfilPage


@when(u'Click en asociar agrupacion sede')
def step_impl(context):
    try:
        PerfilPage.ClickAsociarASedeAPerfil(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en asociar agrupacion sede"


@when(u'Seleccionar AgrupacionSede "{AgrupacionSede}"')
def step_impl(context, AgrupacionSede):
    try:
        PerfilPage.seleccionarAgrupacionSede(context, AgrupacionSede)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar AgrupacionSede"


@when(u'Guardar asociacion')
def step_impl(context):
    try:
       PerfilPage.guardarAsociacionSedes(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Guardar asociacion"


@then(u'Validar Asociacion agrupacion sedes')
def step_impl(context):
    try:
        PerfilPage.ValidateToastAsociacionAgrupacionAPerfil(context)
        time.sleep(1)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Asociacion agrupacion sedes"
