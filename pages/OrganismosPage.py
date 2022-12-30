import time
from Funciones.Funciones import Funciones_epidata
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Funciones.Navegador import Funciones_driver
from configuration.config import Datatest
from Funciones.report_allure import Funciones_report

t = 1


class OrganismosPage(Funciones_epidata):

    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def IrAOrganismos(self):
        Funciones_epidata.Click_Field(self, By.XPATH, "//span[text()='Organismos']")

    @staticmethod
    def ClickCrearOrganismo(self):
        Funciones_epidata.Click_Field(self, By.XPATH, "//button[contains(.,'+ Crear Organismo')]")

    @staticmethod
    def InputNombreOrganismo(self, nuevoorganismo):
        Funciones_epidata.Input_Texto(self,By.XPATH, "(//input[@id='organismo'])[2]", nuevoorganismo)
        time.sleep(1)

    @staticmethod
    def ClickGuardarOrganismo(self):
        Funciones_epidata.Click_Field(self, By.XPATH, "(//button[contains(.,'Guardar')])[2]")

    def ValidateToastAlta(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Organismo Creado correctamente.":

            print("Se pudo crear el organismo correctamente")

            Funciones_epidata.captura_pantalla(self, "captura organismo creado correctamente")
        else:
            print("No se pudo dar de alta el organismo")
