import time
from behave import *
from pages.ServiciosXSedesPage import ServiciosXSedesPage


@when(u'Click en ServicioXSede')
def step_impl(context):
    try:
        ServiciosXSedesPage.irAServiciosXSede(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en ServicioXSede"


@when(u'Click en boton crear ServicioXSede')
def step_impl(context):
    try:
        ServiciosXSedesPage.CrearServicioXSede(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en boton crear ServicioXSede"


@when(u'Seleccionar Servicio "{servicioAutomatizado}"')
def step_impl(context, servicioAutomatizado):
    try:
        ServiciosXSedesPage.SeleccionarServicio(context, servicioAutomatizado)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar Servicio"


@when(u'Seleccionar Sede "{sedeAutomatizada}"')
def step_impl(context, sedeAutomatizada):
    try:
        ServiciosXSedesPage.SeleccionarSede(context, sedeAutomatizada)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar Sede"


@when(u'Ingresar cant maxima de turnos por ciudadano "{cantMaximaTurnos}"')
def step_impl(context, cantMaximaTurnos):
    try:
        ServiciosXSedesPage.CompletarCantMaxTurnos(context, cantMaximaTurnos)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar cant maxima de turnos por ciudadano"


@when(u'Ingresar dias previos a la cita "{diasPreviosCita}"')
def step_impl(context, diasPreviosCita):
    try:
        ServiciosXSedesPage.CompletarDiasPreviosACita(context, diasPreviosCita)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar dias previos a la cita"


@when(u'Ingresar maxima disponibilidad de dias "{maxDisponibilidadDias}"')
def step_impl(context, maxDisponibilidadDias):
    try:
        ServiciosXSedesPage.CompletarMaxDisponibilidadDias(context, maxDisponibilidadDias)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar maxima disponibilidad de dias"


@when(u'Click guardar ServicioXSede')
def step_impl(context):
    try:
        ServiciosXSedesPage.GuardarServiciosXSede(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click guardar ServicioXSede"


@then(u'Validar Alta ServicioXSede')
def step_impl(context):
    try:
        ServiciosXSedesPage.ValidateToastAltaServicioXSede(context)
        time.sleep(3)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click guardar ServicioXSede"
