import time
from datetime import date, timedelta, datetime

from Funciones.Funciones import Funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AgrupacionServiciosPage(Funciones):

    def __init__(self, driver):
        super().__init__(driver)

    ###############################################################
    # alta agrupacion

    def IrAAgrupacionServicio(self):
        Funciones.Click_Field(self, By.XPATH, "//span[normalize-space()='Agrupación Servicios']")

    def CrearAgrupacion(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@data-bs-target='#myModalagrupacion']")

    def IngresarNombreAgrupacion(self, NombreAgrupacion):
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", NombreAgrupacion)

    def SeleccionMultipleServicios(self, Servicio):
        Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{Servicio}']")
        Funciones.Click_Field(self, By.XPATH, "(//option)[1]")
        Funciones.Click_Field(self, By.XPATH, "(//option)[4]")
        Funciones.Click_Field(self, By.XPATH, "(//option)[6]")
        Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
        time.sleep(0.5)

    def GuardarAgrupacion(self, NombreAgrupacion):
        try:
            NameVariable = 0
            NameVariable += 1
            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[contains(text(),'El nombre ingresado ya existe.')]").text

            ChangeNombre = NombreAgrupacion + f'{NameVariable}'

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariable += 1
                ChangeNombre = NombreAgrupacion + f'{NameVariable}'

                Funciones.Clear_Field(self, By.XPATH, "//input[@id='nombre']")
                Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", ChangeNombre)

                Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
        except:
            assert True
            Funciones.captura_pantalla(self, "captura GuardarAgrupacionSede")

    def ValidateToastAltaAgrupacionServicio(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Agrupación Creada correctamente.":

            print("Se pudo crear la agrupacion correctamente")

            Funciones.captura_pantalla(self, "captura agrupacion de servicios creada correctamente")
        else:
            print("No se pudo crear la agrupacion")

    ###############################################################
    # Edicion agrupacion

    def FiltrarXNombre(self, NombreAgrupacion):
        time.sleep(1)
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='nom-ser-agrup']", NombreAgrupacion)

    def EditarNombre(self, NombreAgrupacionEditado):
        Funciones.Clear_Field(self, By.XPATH, "//input[@id='perfil']")
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='perfil']", NombreAgrupacionEditado)

    def NuevosServicios(self):
        Funciones.Click_Field(self, By.XPATH, "(//option[13])[2]")
        Funciones.Click_Field(self, By.XPATH, "(//option[16])[2]")
        Funciones.Click_Field(self, By.XPATH, "(//option[10])[2]")
        Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space()='Guardar'])[2]")
        time.sleep(0.5)

    def GuardarEdicion(self, NombreAgrupacion):
        try:
            NameVariable = 0
            NameVariable += 1

            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[contains(text(),'El nombre ingresado ya existe.')]").text

            ChangeNombre = NombreAgrupacion + f'{NameVariable}'

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariable += 1
                ChangeNombre = NombreAgrupacion + f'{NameVariable}'

                Funciones.Clear_Field(self, By.XPATH, "//input[@id='perfil']")
                Funciones.Input_Texto(self, By.XPATH, "//input[@id='perfil']", ChangeNombre)

                Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space()='Guardar'])[2]")
        except:
            assert True

        Funciones.captura_pantalla(self, "captura GuardarEdicionAgrupacion")

    def ValidateToastEdicionAgrupacionServicios(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Agrupación actualizada correctamente.":

            print("Se pudo editar la agrupacion correctamente")

            Funciones.captura_pantalla(self, "captura agrupacion de servicios editada correctamente")
        else:
            print("No se pudo crear la agrupacion")

    ###############################################################
    # Baja agrupacion

    def ValidateToastBajaAgrupacionServicios(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Agrupación eliminada exitosamente.":

            print("Se pudo dar de baja la agrupacion correctamente")

            Funciones.captura_pantalla(self, "captura agrupacion de servicios dada de baja correctamente")
        else:
            print("No se pudo eliminar la agrupacion")
