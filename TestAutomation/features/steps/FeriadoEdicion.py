from datetime import date
import time
from behave import *
from pages.FeriadosPage import FeriadosPage

#Prueba de pusheo git


@when(u'Filtrar por descripcion feriado "{descripcionFeriado}"')
def step_impl(context, descripcionFeriado):
    try:
        FeriadosPage.filtrarXDescripcion(context,  descripcionFeriado)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Filtrar por descripcion feriado"


@when(u'Click en editar')
def step_impl(context):
    try:
        FeriadosPage.ClickEditarFeriado(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en editar"


@when(u'Escribir nueva descripcion del feriado editado "{descripcionEditadaFeriado}"')
def step_impl(context, descripcionEditadaFeriado):
    try:
        FeriadosPage.NuevaDescripcion(context, descripcionEditadaFeriado)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Escribir nueva descripcion del feriado editado"


@when(u'Click guardar')
def step_impl(context):
    try:
        FeriadosPage.EdicionGuardar(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click guardar"


@then(u'Validar Edicion feriado')
def step_impl(context):
    try:
        FeriadosPage.ValidateToastEdicionFeriado(context)
        time.sleep(3)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Edicion feriado"
