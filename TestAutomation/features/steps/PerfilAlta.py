import time
from behave import *
from pages.PerfilPage import PerfilPage


@when(u'Click en perfiles')
def step_impl(context):
    try:
        PerfilPage.irAPerfiles(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en perfiles"


@when(u'Click en Crear')
def step_imp(context):
    try:
        PerfilPage.crearNuevoRegistro(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en Crear"


@when(u'Ingresar Nombre perfil "{Perfil}"')
def step_impl(context, Perfil):
    try:
        PerfilPage.NombrePerfil(context, Perfil)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar Nombre perfil"


@when(u'Click en guardar perfil "{Perfil}"')
def step_impl(context, Perfil):
    try:
        PerfilPage.GuardarPerfil(context, Perfil)
    except:
        context.driver.close()
        assert False, "La prueba fallo en : Click en guardar perfil"


@then(u'Validar alta perfil')
def step_impl(context):
    try:
        PerfilPage.ValidateToastAltaPerfil(context)
        time.sleep(2)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar alta perfil"
