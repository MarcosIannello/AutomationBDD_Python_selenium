from datetime import date
import time
from behave import *
from pages.PerfilPage import PerfilPage


@when(u'Filtrar por nombre Perfil "{Perfil}"')
def step_impl(context, Perfil):
    try:
        PerfilPage.filtrarXNombre(context, Perfil)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Filtrar por nombre Perfil"


@when(u'Ingresar nuevo nombre perfil "{PerfilEditado}"')
def step_impl(context, PerfilEditado):
    try:
        PerfilPage.nuevoNombrePerfil(context, PerfilEditado)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar nuevo nombre perfil"


@when(u'Click en guardar PerfilEditado "{PerfilEditado}"')
def step_impl(context, PerfilEditado):
    try:
        PerfilPage.GuardarEdicion(context, PerfilEditado)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en guardar PerfilEditado"


@then(u'Validar Edicion perfil')
def step_impl(context):
    try:
        PerfilPage.ValidateToastModificacionPerfil(context)
        time.sleep(1)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Edicion perfil"

