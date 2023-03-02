import time
from behave import *
from pages.OrganismosPage import OrganismosPage


@When(u'Click en Organismos')
def step_imp(context):
    try:
        OrganismosPage.IrAOrganismos(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en Organismos"


@When(u'Click en boton crear organismo')
def step_impl(context):
    try:
        OrganismosPage.ClickCrearOrganismo(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en boton crear organismo"


@when(u'Escribiendo campo nombre nuevo organismo "{organismo}"')
def step_impl(context, organismo):
    try:
        OrganismosPage.InputNombreOrganismo(context, organismo)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Escribiendo campo nombre nuevo organismo"


@when(u'Click guardar organismo')
def step_impl(context):
    try:
        OrganismosPage.ClickGuardarOrganismo(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Guardar Organismo"


@then(u'Validar Alta organismo')
def step_impl(context):
    try:
        OrganismosPage.ValidateToastAlta(context)
        time.sleep(5)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Alta organismo"
