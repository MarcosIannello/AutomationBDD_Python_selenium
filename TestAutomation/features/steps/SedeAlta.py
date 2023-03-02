import time
from behave import *
from pages.SedesPage import SedesPage


@when(u'Click en Sedes')
def step_impl(context):
    try:
        SedesPage.irASedes(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en Sedes"


@when(u'Click en boton crear Sedes')
def step_impl(context):
    try:
        SedesPage.CrearSede(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en boton crear Sedes"


@when(u'Escribiendo campo nombre sede "{Sede}"')
def step_impl(context, Sede):
    try:
        SedesPage.ingresarNombreSede(context, Sede)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Escribiendo campo nombre sede "


@when(u'Escribiendo campo calle y altura "{direccion}"')
def step_impl(context, direccion):
    try:
        SedesPage.IngresarCalleAltura(context, direccion)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Escribiendo campo calle y altura"


@when(u'Click guardar Sede')
def step_impl(context):
    try:
        SedesPage.GuardarSede(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click guardar Sede"


@then(u'Validar Alta sede')
def step_impl(context):
    try:
        SedesPage.ValidateToastAltaSede(context)
        time.sleep(3)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Alta sede"
