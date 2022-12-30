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


@when(u'Escribiendo campo nombre nuevo organismo "{nuevoorganismo}"')
def step_impl(context, nuevoorganismo):
    try:
        OrganismosPage.InputNombreOrganismo(context,nuevoorganismo)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Escribiendo campo nombre nuevo organismo"


@when(u'Click guardar organismo')
def step_impl(context):
    try:
        OrganismosPage.ClickGuardarOrganismo(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: CLick en guardar organismo"


@then(u'Validar Alta organismo')
def step_impl(context):
    try:
        OrganismosPage.ValidateToastAlta(context)
        time.sleep(3)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Alta organismo"
