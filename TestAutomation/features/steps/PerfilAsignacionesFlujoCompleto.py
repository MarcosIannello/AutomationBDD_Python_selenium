import time
from behave import *
from pages.AsignacionesPerfilFlujoCompletoPage import AsignacionesPerfilFlujoCompletoPage


@when(u'Ingresando Nombre Perfil "{Perfil}"')
def step_impl(context, Perfil):
    try:
        AsignacionesPerfilFlujoCompletoPage.NombrePerfilFC(context, Perfil)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresando Nombre Perfil "


@when(u'Click sobre boton guardar "{Perfil}"')
def step_impl(context, Perfil):
    try:
        AsignacionesPerfilFlujoCompletoPage.GuardarPerfilFC(context, Perfil)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click sobre boton guardar"


@when(u'Ingresando nombre agrupacion sede "{AgrupacionSedes}"')
def step_impl(context, AgrupacionSedes):
    try:
        AsignacionesPerfilFlujoCompletoPage.IngresarNombreAgrupacion(context, AgrupacionSedes)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresando nombre agrupacion sede"


@when(u'Click sobre boton guardar agrupacion Sedes "{AgrupacionSedes}"')
def step_impl(context, AgrupacionSedes):
    try:
        AsignacionesPerfilFlujoCompletoPage.GuardarAgrupacion(context, AgrupacionSedes)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click sobre boton guardar agrupacion Sedes"


@when(u'Ingresando nombre agrupacion servicios "{AgrupacionServicios}"')
def step_impl(context, AgrupacionServicios):
    try:
        AsignacionesPerfilFlujoCompletoPage.IngresarNombreAgrupacionServicios(context, AgrupacionServicios)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresando nombre agrupacion servicios"


@when(u'Click sobre boton guardar agrupacion servicios "{AgrupacionServicios}"')
def step_impl(context, AgrupacionServicios):
    try:
        AsignacionesPerfilFlujoCompletoPage.GuardarAgrupacionServicio(context, AgrupacionServicios)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click sobre boton guardar agrupacion servicios"


@when(u'Filtrar por nombre Perfil')
def step_impl(context):
    try:
        AsignacionesPerfilFlujoCompletoPage.filtrarXNombre(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Filtrar por nombre Perfil"


@when(u'Seleccionar AgrupacionSede automatizada')
def step_impl(context):
    try:
        AsignacionesPerfilFlujoCompletoPage.seleccionarAgrupacionSede(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar AgrupacionSede automatizada"


@when(u'Guardar asociacion agrupacion sede a perfil')
def step_impl(context):
    try:
        AsignacionesPerfilFlujoCompletoPage.guardarAsociacionSedeAPerfil(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Guardar asociacion agrupacion sede a perfil"


@when(u'Seleccionar AgrupacionServicios automatizada')
def step_impl(context):
    try:
        AsignacionesPerfilFlujoCompletoPage.seleccionarAgrupacionServicio(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar AgrupacionServicios automatizada"


@then(u'Validacion Final flujo')
def step_impl(context):
    try:
        AsignacionesPerfilFlujoCompletoPage.ValidateToastAsociacionAgrupacionServicioAPerfil(context)
        time.sleep(1)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validacion Final flujo"
