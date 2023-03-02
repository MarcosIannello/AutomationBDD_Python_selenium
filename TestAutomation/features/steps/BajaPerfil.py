from datetime import date
import time
from behave import *
from pages.PerfilPage import PerfilPage


@then(u'Validar Edicion Baja')
def step_impl(context):
    try:
        PerfilPage.ValidateToastBajaPerfil(context)
        time.sleep(1)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Edicion Baja"

