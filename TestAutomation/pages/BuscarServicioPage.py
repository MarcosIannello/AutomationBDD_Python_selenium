import time
from datetime import date, timedelta, datetime

from Funciones.Funciones import Funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BuscarServicioPage(Funciones):

    def __init__(self, driver):
        super().__init__(driver)

    ###############################################################
    # Busqueda Servicios

    def IraBuscarServicio(self):
        Funciones.Click_Field(self, By.XPATH, "//span[normalize-space()='Buscar servicio']")

    def BuscadorServicio(self, Servicio):
        Funciones.Click_Field(self, By.XPATH, "//button[@data-id='first-disabled']")
        Funciones.Click_Field(self, By.XPATH, f"//a[normalize-space()='{Servicio}']")

    def ClickComenzar(self):
        Funciones.Click_Field(self, By.XPATH, "//span[@class='access-title']")

    def SeleccionDeTurno(self):
        """COMPLETAR CUANDO SE TERMINE EL DESARROLLO DEL REQUERIMIENTO"""
        Funciones.captura_pantalla(self, "Captura para visualizar falta de desarrollo")
