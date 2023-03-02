from behave import *
from pages.ServiciosPage import ServiciosPage


@when(u'Filtrar por servicio automatizado "{nombreServicio}"')
def step_impl(context, nombreServicio):
    try:
        ServiciosPage.FiltrarXNombreServicio(context, nombreServicio)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Filtrar por servicio automatizado"


@when(u'Click en boton editar')
def step_impl(context):
    try:
        ServiciosPage.ClickBotonEditarServicio(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en boton editar"


@when(u'Ingresar un nuevo nombre de servicio "{nombreEditadoServicio}"')
def step_impl(context, nombreEditadoServicio):
    try:
        ServiciosPage.NuevoNombreServicio(context, nombreEditadoServicio)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar un nuevo nombre de servicio"


@when(u'Ingresar nueva cantidad maxima de turnos "{cantMaximaTurnos}"')
def step_impl(context, cantMaximaTurnos):
    try:
        ServiciosPage.NuevaCantMaximaDeTurnos(context, cantMaximaTurnos)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Ingresar nueva cantidad maxima de turnos"


@when(u'Click en Guardar edicion servicio "{nombreEditadoServicio}"')
def step_impl(context, nombreEditadoServicio):
    try:
        ServiciosPage.GuardarEdicionServicio(context, nombreEditadoServicio)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en Guardar edicion servicio"


@then(u'Validar edicion servicio')
def step_impl(context):
    try:
        ServiciosPage.ValidateToastEdicionServicio(context)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Validar edicion servicio"
