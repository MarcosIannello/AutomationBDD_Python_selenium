import time
from Funciones.Funciones import Funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Funciones.Navegador import Funciones_driver
from configuration.config import Datatest
from Funciones.report_allure import Funciones_report

t = 1


class LoginPage(Funciones):

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
        # navegador.driver_Firefox(self, "C:\drivers\geckodriver.exe")
        navegador.driver_Chrome(self)
        fun = Funciones(self.driver)    
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
        time.sleep(0.5)
        fun.captura_pantalla("captura ClickIngresar")

    @staticmethod
    def ValidacionInicioSesion():
        fun.validates(By.XPATH, "//p[text()='Gestión de las tareas internas del proyecto.']")
        time.sleep(0.5)
        fun.captura_pantalla("captura ValidacionInicioSesion")

    @staticmethod
    def CerrarSesion():
        fun.Click_Field(By.XPATH, "//a[contains(@aria-label,'Cerrar sesión')]")  # "//a[@class='list-group-item list-group-item-logout logout-sm']"
        fun.captura_pantalla("captura CerrarSesion")
        time.sleep(1)

    def ValidacionCredencialesIncorrectas(self):

        element = WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-header"))).text
        val = WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.toast-header"))).text

        if element == val:
            print(f"Se pudo comparar : -----{element} == {val}------")
            fun.captura_pantalla("captura")
        else:
            print("No se pudo validar el campo")


