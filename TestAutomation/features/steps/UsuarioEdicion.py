import time
from behave import *
from pages.UsuariosPage import UsuariosPage


@when(u'Filtrar por cuit "{nuevoUserCuit}"')
def step_impl(context, nuevoUserCuit):
    try:
        UsuariosPage.FiltrarCuit(context, nuevoUserCuit)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Filtrar por cuit"


@when(u'Cambiar rol y organismo "{organismo}" "{rol}"')
def step_impl(context, organismo, rol):
    try:
        UsuariosPage.NuevoRolYOrganismo(context, organismo, rol)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Cambiar rol y organismo"


@when(u'Click guardar edicion Usuario')
def step_impl(context):
    try:
        UsuariosPage.EdicionGuardar(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click guardar edicion"


@then(u'Validar Alta edicion')
def step_impl(context):
    try:
        UsuariosPage.ValidateToastEdicionUSUARIO(context)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Alta edicion"
