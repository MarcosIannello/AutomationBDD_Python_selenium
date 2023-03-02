import time
from behave import *
from pages.UsuariosPage import UsuariosPage


@when(u'Click en asignar perfil')
def step_impl(context):
    try:
        UsuariosPage.AsignarPerfil(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en asignar perfil"


@when(u'Seleccionar perfil de la lista "{Perfil}"')
def step_impl(context, Perfil):
    try:
        UsuariosPage.seleccionarPerfil(context, Perfil)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar perfil de la lista"


@when(u'Click guardar Asignacion')
def step_impl(context):
    try:
        UsuariosPage.GuardarAsignacion(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click guardar Asignacion"


@then(u'Validar Asignacion perfil')
def step_impl(context):
    try:
        UsuariosPage.ValidateToastAsignacionPerfil(context)
        time.sleep(1)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Asignacion perfil"
