from behave import *
from pages.ServiciosPage import ServiciosPage


@when(u'Click en boton eliminar')
def step_impl(context):
    try:
        ServiciosPage.ClickBotonEliminar(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en boton eliminar"


@when(u'Confirmar Baja')
def step_impl(context):
    try:
        ServiciosPage.ConfirmarBaja(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Confirmar Baja"


@then(u'Validar baja servicio')
def step_impl(context):
    try:
        ServiciosPage.ValidateToastBajaServicio(context)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar baja servicio"
