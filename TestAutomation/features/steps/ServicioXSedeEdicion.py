import time
from behave import *
from pages.ServiciosXSedesPage import ServiciosXSedesPage


@when(u'Filtrar X Servicio y Sede "{servicioAutomatizado}" "{sedeAutomatizada}"')
def step_impl(context,servicioAutomatizado, sedeAutomatizada):
    try:
        ServiciosXSedesPage.FiltrarXServicioYSede(context, servicioAutomatizado, sedeAutomatizada)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Filtrar X Servicio y Sede"


@when(u'Click en boton Editar ServicioxSede')
def step_impl(context):
    try:
        ServiciosXSedesPage.EditarServicioXSede(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en boton Editar ServicioxSede"


@when(u'Editar cant maxima de turnos por ciudadano "{cantMaximaTurnosEditado}"')
def step_impl(context, cantMaximaTurnosEditado):
    try:
        ServiciosXSedesPage.IngresarNuevaCantidadMaxDeTurnos(context, cantMaximaTurnosEditado)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Editar cant maxima de turnos por ciudadano"


@when(u'Editar dias previos a la cita "{diasPreviosCitaEditado}"')
def step_impl(context, diasPreviosCitaEditado):
    try:
        ServiciosXSedesPage.IngresarNuevosDiasPreviosCita(context, diasPreviosCitaEditado)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Editar dias previos a la cita"


@when(u'Editar maxima disponibilidad de dias "{maxDisponibilidadDiasEditado}"')
def step_impl(context, maxDisponibilidadDiasEditado):
    try:
        ServiciosXSedesPage.IngresarNuevaMaxDisponibilidadDeDias(context, maxDisponibilidadDiasEditado)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Editar maxima disponibilidad de dias"


@when(u'Click guardar edicion')
def step_impl(context):
    try:
        ServiciosXSedesPage.GuardarEdicionServicioXSede(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click guardar edicion"


@then(u'Validar Edicion ServicioXSede')
def step_impl(context):
    try:
        ServiciosXSedesPage.ValidateToastEdicionServicioXSede(context)
        time.sleep(3)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Edicion ServicioXSede"

