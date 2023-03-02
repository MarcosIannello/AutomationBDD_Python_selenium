import time
from behave import *
from pages.UsuariosPage import UsuariosPage


@when(u'Click en Usuarios')
def step_impl(context):
    try:
        UsuariosPage.IrAUsuarios(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en Usuarios"


@when(u'Click en boton crear Usuarios')
def step_impl(context):
    try:
        UsuariosPage.CrearUsuario(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en boton crear Usuarios"


@when(u'Completar campo Cuit "{nuevoUserCuit}"')
def step_impl(context, nuevoUserCuit):
    try:
        UsuariosPage.CampoCuit(context, nuevoUserCuit)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Completar campo Cuit"


@when(u'Click en buscar por AD')
def step_impl(context):
    try:
        UsuariosPage.BuscarAd(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en buscar por AD"


@when(u'Click guardar Usuario')
def step_impl(context):
    try:
        UsuariosPage.GuardarUsuario(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click guardar Usuario"


@when(u'Seleccionar rol del usuario "{rol}"')
def step_impl(context, rol):
    try:
        UsuariosPage.seleccionarRol(context, rol)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar rol del usuario"


@when(u'Seleccionar Organismo del usuario "{organismo}"')
def step_impl(context, organismo):
    try:
        UsuariosPage.seleccionarOrganismo(context, organismo)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar Organismo del usuario"


@then(u'Validar Alta usuario')
def step_impl(context):
    try:
        UsuariosPage.ValidateToastAltaUSUARIO(context)
        time.sleep(2)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Alta usuario"
