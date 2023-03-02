from pages.LoginPage import LoginPage
from behave import *


# Se ejecuta en LoginFail para validar popup de credenciales incorrectas
@then(u'Validar pop up de credenciales incorrectas')
def step_impl(context):
    try:
        LoginPage.ValidacionCredencialesIncorrectas(context)
        context.driver.close()
    except:
        # context.driver.close()
        assert False, "La prueba fallo en: Validar pop up de credenciales incorrectas"
