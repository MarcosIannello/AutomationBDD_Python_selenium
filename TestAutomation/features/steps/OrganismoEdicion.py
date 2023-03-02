import time
from behave import *
from pages.OrganismosPage import OrganismosPage


@when(u'Click editar organismo')
def step_impl(context):
    try:
        OrganismosPage.ClickBotonEditar(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click editar organismo"


@when(u'Editar nombre organismo por "{nombreEdicionOrganismo}"')
def step_impl(context, nombreEdicionOrganismo):
    try:
        OrganismosPage.InputNombreEditado(context, nombreEdicionOrganismo)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Editar nombre organismo"


@when(u'Click Confirmar edicion "{nombreEdicionOrganismo}"')
def step_impl(context, nombreEdicionOrganismo):
    try:
        OrganismosPage.ClickConfirmarEdicion(context, nombreEdicionOrganismo)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click Confirmar edicion"


@then(u'Validar Edicion Organismo')
def step_impl(context):
    try:
        OrganismosPage.ValidateToastEdicion(context)
        time.sleep(1)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en : Validar Edicion Organismo"

