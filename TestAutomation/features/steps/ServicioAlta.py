import time
from behave import *
from pages.ServiciosPage import ServiciosPage


@when(u'Click en servicios')
def step_impl(context):
    try:
        ServiciosPage.IrAServicios(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en servicios"


@when(u'Click en boton crear servicio')
def step_impl(context):
    try:
        time.sleep(1)
        ServiciosPage.ClickCrearServicio(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en boton crear servicio"


@when(u'Seleccionar un organismo "{organismo}"')
def step_impl(context, organismo):
    try:
        ServiciosPage.SeleccionarOrganismo(context, organismo)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar un organismo"


@when(u'Ingresar un nombre de servicio "{Servicio}"')
def step_impl(context, Servicio):
    try:
        ServiciosPage.ingresarNombreServicio(context, Servicio)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar un nombre de servicio"


@when(u'Ingresar cantidad maxima de turnos por ciudadano "{cantMaximaTurnos}"')
def step_impl(context, cantMaximaTurnos):
    try:
        ServiciosPage.TurnosXCiudadano(context, cantMaximaTurnos)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar cantidad maxima de turnos por ciudadano"


@when(u'Ingresar tiempo Pre-Cancelacion cita "{tiempoPreCancelacion}"')
def step_impl(context, tiempoPreCancelacion):
    try:
        ServiciosPage.TiempoPreCancelacion(context, tiempoPreCancelacion)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar tiempo Pre-Cancelacion cita"


@when(u'Ingresar tiempo espera para toma turno "{tiempoEspera}"')
def step_impl(context, tiempoEspera):
    try:
        ServiciosPage.EsperaTiempo(context, tiempoEspera)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar tiempo espera para toma turno"


@when(u'Ingresar URL "{url}"')
def step_impl(context, url):
    try:
        ServiciosPage.IngresarURL(context, url)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar URL"


@when(u'Seleccionar servicio de cancelacion')
def step_impl(context):
    try:
        ServiciosPage.ServicioCancelacion(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar servicio de cancelacion"


@when(u'Seleccionar si requiere Login Con Miba')
def step_impl(context):
    try:
        ServiciosPage.LoginMiba(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar si requiere Login Con Miba"


@when(u'Seleccionar Documento admitido')
def step_impl(context):
    try:
        ServiciosPage.DocumentosAdmitidos(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Seleccionar Documento admitido"


@when(u'Seleccionar orden de preferencia "{lugar}" "{fecha}" "{proximo}"')
def step_impl(context, proximo, lugar, fecha):
    # try:
    ServiciosPage.SeleccionOrdenPreferencia(context, proximo, lugar, fecha)
    # except:
    #     context.driver.close()
    #     assert False, "La prueba fallo en: Seleccionar orden de preferencia"


@when(u'Click en Guardar servicio "{Servicio}"')
def step_impl(context, Servicio):
    try:
        ServiciosPage.GuardarServicio(context, Servicio)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en Guardar servicio"


@then(u'Validar Alta servicio')
def step_impl(context):
    try:
        ServiciosPage.ValidateToastAltaServicio(context)
        time.sleep(1)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar Alta servicio"
