from datetime import date
import time
from behave import *
from pages.FeriadosPage import FeriadosPage


@when(u'Click en borrar')
def step_impl(context):
    try:
        FeriadosPage.BorrarFeriado(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en borrar"


@then(u'Validar Baja feriado')
def step_impl(context):
    try:
        FeriadosPage.ValidateToastBAJAFeriado(context)
        time.sleep(2)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Baja feriado"