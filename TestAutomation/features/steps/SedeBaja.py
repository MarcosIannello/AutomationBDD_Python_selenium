import time
from behave import *
from pages.SedesPage import SedesPage


@when(u'Filtrar mediante nombre sede "{Sede}"')
def step_impl(context, Sede):
    try:
        SedesPage.filtrarXNombreSede(context, Sede)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Filtrar mediante nombre sede "


@when(u'Confirmar baja sede')
def step_impl(context):
    try:
        SedesPage.ConfirmarBajaSede(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Confirmar baja sede"


@then(u'Validar Baja sede')
def step_impl(context):
    try:
        SedesPage.ValidateToastBajaSede(context)
        time.sleep(3)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Baja sede"
