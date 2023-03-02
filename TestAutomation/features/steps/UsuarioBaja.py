import time
from behave import *
from pages.UsuariosPage import UsuariosPage


@when(u'Borrar usuario')
def step_impl(context):
    try:
        UsuariosPage.BorrarUsuario(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Borrar usuario"


@then(u'Validar baja usuario')
def step_impl(context):
    try:
        UsuariosPage.ValidateToastBajaUSUARIO(context)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo: Validar baja usuario"

