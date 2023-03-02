import time
from pages.LoginPage import LoginPage
from behave import *
from pages.OrganismosPage import OrganismosPage


@when(u'Filtrar por nombre organismo "{nombreEdicionOrganismo}"')
def step_impl(context, nombreEdicionOrganismo):
    try:
        OrganismosPage.filtrarNombreOrganismo(context, nombreEdicionOrganismo)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Filtrar por nombre organismo"


@when(u'Click boton eliminar')
def step_impl(context):
    try:
        OrganismosPage.ClickBorrarOrganismo(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click boton eliminar "


@when(u'Click confirmar eliminacion')
def step_impl(context):
    try:
        OrganismosPage.ConfirmarBaja(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Confirmar baja"


@then(u'Validar Baja organismo')
def step_impl(context):
    try:
        OrganismosPage.ValidateToastBAJA(context)
        time.sleep(1)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Baja organismo"
