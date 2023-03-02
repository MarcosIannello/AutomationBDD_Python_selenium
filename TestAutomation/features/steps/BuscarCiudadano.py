from pages.CiudadanoPage import CiudadanoPage
from behave import *
import time


@when(u'Click en Buscar Ciudadano')
def step_impl(context):
    try:
        CiudadanoPage.IrABuscarCiudadano(context)
    except:
        context.driver.close()
        assert False, "La Prueba Fallo en: Click en Buscar Ciudadano"


@when(u'Completar los filtros Cabezera "{TipoDocumento}" "{NroDocumento}" "{Genero}"')
def step_impl(context, TipoDocumento, NroDocumento, Genero):
    try:
        CiudadanoPage.CompletarFiltros(context, TipoDocumento, NroDocumento, Genero)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Completar los filtros Cabezera"


@when(u'Click en boton Buscar')
def step_impl(context):
    try:
        CiudadanoPage.Buscar(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en boton Buscar"


@when(u'Completar cuando desarrollo este finalizado')
def step_impl(context):
    print("SE AVANZA HASTA ESTE PUNTO DEBIDO A QUE FALTA DESARROLLO")
    context.driver.close()


@then(u'Validar busqueda')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Validar busqueda')
