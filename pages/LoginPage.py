import time
from Funciones.Funciones import Funciones_epidata
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Funciones.Navegador import Funciones_driver
from configuration.config import Datatest
from Funciones.report_allure import Funciones_report

t = 1


class LoginPage(Funciones_epidata):

    cuitField = "//input[contains(@id,'cuit')]"
    passwordField = "//input[contains(@id,'contrasena')]"
    btnIngresar = "//button[text()=Ingresar]"
    loginValidationField = "//h2[normalize-space()='Organismos']"
    btnCerrarSesion = "//a[@class='list-group-item list-group-item-logout logout-sm']"

    """Constructor of CarrersPage class"""

    def __init__(self, driver):
        super().__init__(driver)

    def OpenBrowser(self):

        global navegador, fun , reporte
        navegador = Funciones_driver
        navegador.driver_Firefox(self, "C:\drivers\geckodriver.exe")
        fun = Funciones_epidata(self.driver)
        fun.Navegar(Datatest.URL, t)
        reporte = Funciones_report

    @staticmethod
    def InputCuit(cuit):
        fun.Input_Texto(By.XPATH, "//input[contains(@id,'cuit')]", cuit)

    @staticmethod
    def InputPassword(password):
        fun.Input_Texto(By.XPATH, "//input[contains(@id,'contrasena')]", password)

    @staticmethod
    def ClickIngresar():
        fun.Click_Field(By.CSS_SELECTOR, "button[type='submit']")

    @staticmethod
    def ValidacionInicioSesion():
        fun.validates(By.XPATH, "//p[text()='Gestión de las tareas internas del proyecto.']")

    @staticmethod
    def CerrarSesion():
        fun.Click_Field(By.XPATH, "//a[contains(@aria-label,'Cerrar sesión')]")  # "//a[@class='list-group-item list-group-item-logout logout-sm']"
        time.sleep(3)

    def ValidacionCredencialesIncorrectas(self):

        element = WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-header"))).text
        val = WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.toast-header"))).text

        if element == val:
            print(f"Se pudo comparar : -----{element} == {val}------")
            fun.captura_pantalla("captura")
        else:
            print("No se pudo validar el campo")

# ALTA ORGANISMO
    @staticmethod
    def IrAOrganismos():
        fun.Click_Field(By.XPATH, "//span[text()='Organismos']")

    @staticmethod
    def ClickCrearOrganismo():
        fun.Click_Field(By.XPATH, "//button[@data-bs-target='#myModalOrganismo']")

    @staticmethod
    def InputNombreOrganismo(nuevoorganismo):
        fun.Input_Texto(By.XPATH, "(//input[@id='organismo'])[2]", nuevoorganismo)
        time.sleep(1)

    @staticmethod
    def ClickGuardarOrganismo():
        fun.Click_Field(By.XPATH, "(//button[contains(.,'Guardar')])[2]")

    def ValidateToastAlta(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Organismo Creado correctamente.":

            print("Se pudo crear el organismo correctamente")

            fun.captura_pantalla("captura organismo creado correctamente")
        else:
            print("No se pudo dar de alta el organismo")

# BAJA ORGANISMO



