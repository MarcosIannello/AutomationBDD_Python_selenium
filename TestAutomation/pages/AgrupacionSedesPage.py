import time
from datetime import date, timedelta, datetime

from Funciones.Funciones import Funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AgrupacionSedesPage(Funciones):

    def __init__(self, driver):
        super().__init__(driver)

    #########################################
    # Alta Agrupacion Sede

    def IrAgrupacionSedes(self):
        Funciones.Click_Field(self, By.XPATH, "//span[normalize-space()='Agrupación de Sedes']")

    def CrearAgrupacionSedes(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@data-bs-target='#myModalNew']")

    def SeleccionMultipleSedes(self, Sede):
        Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{Sede}']")
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
                                                      "//div[contains(text(),'El nombre ya fue ingresado anteriormente.')]").text

            ChangeNombre = NombreAgrupacion + f'{NameVariable}'

            while nombreYaExiste == "El nombre ya fue ingresado anteriormente.":
                NameVariable += 1
                ChangeNombre = NombreAgrupacion + f'{NameVariable}'
                Funciones.Clear_Field(self, By.XPATH, "//input[@id='nombre']")
                Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", ChangeNombre)
                Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")

                # Funciones.captura_pantalla(self, "captura GuardarAgrupacionSede")
        except:
            assert True
            Funciones.captura_pantalla(self, "captura GuardarAgrupacionSede")

    def ValidateToastAltaAgrupacionSede(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Agrupación creada correctamente.":
            print("Se pudo crear la agrupacion correctamente")
            Funciones.captura_pantalla(self, "captura agrupacion de sedes creada correctamente")
        else:
            print("No se pudo crear la agrupacion")
            Funciones.captura_pantalla(self, "captura agrupacion de sedes Fallo")

    #########################################
    # Edicion Agrupacion Sede

    def filtrarXNombre(self, NombreAgrupacion):
        time.sleep(0.5)
        Funciones.Input_Texto(self, By.XPATH, "//input[@name='nombre']", NombreAgrupacion)

    def EditarNombre(self, NombreAgrupacionEditado):
        Funciones.Clear_Field(self, By.XPATH, "(//input[@id='nombre'])[2]")
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='nombre'])[2]", NombreAgrupacionEditado)

    def nuevasSedes(self):
        Funciones.Click_Field(self, By.XPATH, "(//option[12])[2]")
        Funciones.Click_Field(self, By.XPATH, "(//option[13])[2]")
        Funciones.Click_Field(self, By.XPATH, "(//option[14])[2]")
        Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space() = 'Guardar'])[2]")
        time.sleep(0.5)

    def guardarAgrupacionSede(self, NombreAgrupacion):
        try:
            NameVariable = 0
            NameVariable += 1

            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[contains(text(),'El nombre ya fue ingresado anteriormente.')]").text

            ChangeNombre = NombreAgrupacion + f'{NameVariable}'

            while nombreYaExiste == "El nombre ya fue ingresado anteriormente.":
                NameVariable += 1
                ChangeNombre = NombreAgrupacion + f'{NameVariable}'

                Funciones.Clear_Field(self, By.XPATH, "//input[@id='nombre']")
                Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", ChangeNombre)
                Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
                Funciones.captura_pantalla(self, "captura GuardarSedeEditada")
        except:
            assert True
            Funciones.captura_pantalla(self, "captura GuardarSedeEditada")

    """MODIFICAR MENSAJE TOAST CUANDO SOLUCIONEN EL BUG"""
    def ValidateToastEdicionAgrupacionSede(self):
        time.sleep(0.5)
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Agrupación creada correctamente.":

            print("Se pudo editar la agrupacion correctamente")
            Funciones.captura_pantalla(self, "captura agrupacion de sedes editada correctamente")
        else:
            print("No se pudo editar la agrupacion")
            Funciones.captura_pantalla(self, "captura agrupacion de sedes edicion fallo")

    #########################################
    # Baja agrupacion de sede

    def ConfirmarBaja(self):
        Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Borrar']")

    def ValidateToastBajaAgrupacionSede(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Agrupación eliminada exitosamente.":
            print("Se pudo eliminar la agrupacion correctamente")
            Funciones.captura_pantalla(self, "captura agrupacion de sedes eliminada correctamente")
        else:
            print("No se pudo dar de baja la agrupacion")
            Funciones.captura_pantalla(self, "captura agrupacion de sedes Fallo")


