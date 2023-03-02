import time
from datetime import date, timedelta, datetime

from Funciones.Funciones import Funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CiudadanoPage(Funciones):

    def __init__(self, driver):
        super().__init__(driver)

    ###############################################################
    # Busqueda Ciudadano

    def IrABuscarCiudadano(self):
        Funciones.Click_Field(self, By.XPATH, "//span[normalize-space()='Buscar ciudadano']")

    def CompletarFiltros(self, TipoDocumento, NroDocumento, Genero):
        #seleccion tipo documento
        Funciones.Click_Field(self, By.XPATH, "//select[@id='tipoDoc']")
        Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{TipoDocumento}']")

        #Ingresar numero Documento
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='nroDoc']", NroDocumento)

        #Seleccionar Genero
        Funciones.Click_Field(self, By.XPATH, "//select[@id='genero']")
        Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{Genero}']")

    def Buscar(self):
        Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Buscar Ciudadano']")

