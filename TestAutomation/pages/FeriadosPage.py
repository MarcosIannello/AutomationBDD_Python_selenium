from datetime import date
import time
from selenium.webdriver.common.action_chains import ActionChains
from Funciones.Funciones import Funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FeriadosPage(Funciones):

    def __init__(self, driver):
        super().__init__(driver)

    def IrAFeriados(self):
        Funciones.Click_Field(self, By.XPATH, "//span[normalize-space()='Feriados']")

    def CrearFeriado(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@data-bs-target='#myModalNew']")

    def SeleccionarFecha(self):
        fecha = date.today().strftime("%dd-%mm-%Y")
        Funciones.Input_Texto(self, By.CSS_SELECTOR, "input[type='date']", fecha)

    def IngresarDescripcion(self, descripcionFeriado):
        Funciones.Input_Texto(self, By.XPATH, "//textarea[@id='descripcion']", descripcionFeriado)

    def GuardarFeriado(self):
        Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")

    def ValidateToastAltaFeriado(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Feriado creado correctamente.":

            print("Se pudo dar de alta el feriado correctamente")

            Funciones.captura_pantalla(self, "captura Feriado dado de alta correctamente")
        else:
            print("No se pudo dar de alta el feriado")

    # Edicion Feriado

    def filtrarXDescripcion(self, descripcionFeriado):
        Funciones.Input_Texto(self, By.XPATH, "//input[@name='descripcion']", descripcionFeriado)

    def ClickEditarFeriado(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@title='Editar']")

    def NuevaDescripcion(self, descripcionEditadaFeriado):
        Funciones.Clear_Field(self, By.XPATH, "(//textarea[@id='descripcion'])[2]")
        Funciones.Input_Texto(self, By.XPATH, "(//textarea[@id='descripcion'])[2]", descripcionEditadaFeriado)

    def EdicionGuardar(self):
        Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space()='Guardar'])[2]")

    def ValidateToastEdicionFeriado(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Datos guardados correctamente.":

            print("Se pudo editar el feriado correctamente")

            Funciones.captura_pantalla(self, "captura Feriado editado correctamente")
        else:
            print("No se pudo editar el feriado")

    # Baja Feriado

    def BorrarFeriado(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@title='Borrar']")

    def ValidateToastBAJAFeriado(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Feriado eliminado exitosamente.":

            print("Se pudo Borrar el feriado correctamente")

            Funciones.captura_pantalla(self, "captura Feriado borrado correctamente")
        else:
            print("No se pudo borrar el feriado")
