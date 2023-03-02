from datetime import date
import time
from behave import *
from pages.FeriadosPage import FeriadosPage


@when(u'Click en feriados')
def step_impl(context):
    try:
        FeriadosPage.IrAFeriados(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en feriados"


@when(u'Click en boton crear feriados')
def step_impl(context):
    try:
        FeriadosPage.CrearFeriado(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en boton crear feriados"


@when(u'Seleccionar fecha actual como feriado')
def step_impl(context):
    try:
        FeriadosPage.SeleccionarFecha(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar fecha actual como feriado"


@when(u'Escribir descripcion del feriado "{descripcionFeriado}"')
def step_impl(context, descripcionFeriado):
    try:
        FeriadosPage.IngresarDescripcion(context, descripcionFeriado)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Escribir descripcion del feriado"


@when(u'Click guardar feriado')
def step_impl(context):
    try:
        FeriadosPage.GuardarFeriado(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click guardar feriado"


@then(u'Validar Alta feriado')
def step_impl(context):
    try:
        FeriadosPage.ValidateToastAltaFeriado(context)
        time.sleep(3)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Alta feriado"
