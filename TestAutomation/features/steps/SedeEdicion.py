import time
from behave import *
from pages.SedesPage import SedesPage


@when(u'Filtrar por nombre sede "{Sede}"')
def step_impl(context, Sede):
    SedesPage.filtrarXNombre(context, Sede)


@when(u'Click en boton editar sede')
def step_impl(context):
    SedesPage.EditarSede(context)


@when(u'Editando nuevo nombre de sede "{nombreEditadoSede}"')
def step_impl(context, nombreEditadoSede):
    SedesPage.NombreEditado(context, nombreEditadoSede)


@when(u'Editando campo calle y altura "{direccion}"')
def step_impl(context, direccion):
    SedesPage.AlturaYCalleEditada(context,direccion)


@when(u'Ingresar Descripcion "{descripcion}"')
def step_impl(context, descripcion):
    SedesPage.DescripcionEditada(context, descripcion)


@when(u'Click guardar Sede editada')
def step_impl(context):
    SedesPage.EdicionGuardar(context)


@then(u'Validar edicion sede')
def step_impl(context):
    SedesPage.ValidateToastEdicionSede(context)
    time.sleep(1)
    context.driver.close()

