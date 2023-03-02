import time
from Funciones.Funciones import Funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ServiciosXSedesPage(Funciones):

    def __init__(self, driver):
        super().__init__(driver)

    # alta ServicioXSede

    def irAServiciosXSede(self):
        Funciones.Click_Field(self, By.XPATH, "//span[normalize-space()='Servicios por Sede']")

    def CrearServicioXSede(self):
        Funciones.Click_Field(self, By.XPATH, "//button[contains(.,'+ Crear Servicio por Sede')]")

    def SeleccionarServicio(self, servicioAutomatizado):
        Funciones.Click_Field(self, By.XPATH, "//select[@id='servicioId']")
        Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{servicioAutomatizado}']")

    def SeleccionarSede(self, sedeAutomatizada):
        Funciones.Click_Field(self, By.XPATH, "//select[@id='sedeId']")
        Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{sedeAutomatizada}']")

    def CompletarCantMaxTurnos(self, cantMaximaTurnos):
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='turnosCiudadano']", cantMaximaTurnos)

    def CompletarDiasPreviosACita(self, diasPreviosCita):
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='diasPrevioCita']", diasPreviosCita)

    def CompletarMaxDisponibilidadDias(self, maxDisponibilidadDias):
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='maximaDisponibilidad']", maxDisponibilidadDias)

    def GuardarServiciosXSede(self):
        Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")

    def ValidateToastAltaServicioXSede(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Servicio por sede creada correctamente.":

            print("Se pudo dar de alta el servicioXSede correctamente")

            Funciones.captura_pantalla(self, "captura servicioXSede dado de alta correctamente")
        else:
            print("No se pudo dar de alta el servicioXSede")

    # edicion ServicioXSede

    def FiltrarXServicioYSede(self, sedeAutomatizada, servicioAutomatizado):
        Funciones.Input_Texto(self, By.XPATH, "//input[@name='servicioNombre']", servicioAutomatizado)
        Funciones.Input_Texto(self, By.XPATH, "//input[@name='sedeNombre']", sedeAutomatizada)
        time.sleep(1)

    def EditarServicioXSede(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@title='Editar']")

    def IngresarNuevaCantidadMaxDeTurnos(self, cantMaximaTurnosEditado):
        Funciones.Clear_Field(self, By.XPATH, "(//input[@id='turnosCiudadano'])[2]")
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='turnosCiudadano'])[2]", cantMaximaTurnosEditado)

    def IngresarNuevosDiasPreviosCita(self, diasPreviosCitaEditado):
        Funciones.Clear_Field(self, By.XPATH, "(//input[@id='diasPrevioCita'])[2]")
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='diasPrevioCita'])[2]", diasPreviosCitaEditado)

    def IngresarNuevaMaxDisponibilidadDeDias(self, maxDisponibilidadDiasEditado):
        Funciones.Clear_Field(self, By.XPATH, "(//input[@id='maximaDisponibilidad'])[2]")
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='maximaDisponibilidad'])[2]", maxDisponibilidadDiasEditado)

    def GuardarEdicionServicioXSede(self):
        Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space()='Guardar'])[2]")

    def ValidateToastEdicionServicioXSede(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Servicio por sede actualizado correctamente.":

            print("Se pudo Editar el servicioXSede correctamente")

            Funciones.captura_pantalla(self, "captura servicioXSede Editado correctamente")
        else:
            print("No se pudo Editar el servicioXSede")

    # Baja ServicioXSede

    def BajaServicioXSede(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@title='Borrar']")

    def ValidateToastBAJAServicioXSede(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Servicio por sede eliminado exitosamente.":

            print("Se pudo ELIMINAR el servicioXSede correctamente")

            Funciones.captura_pantalla(self, "captura servicioXSede ELIMINADO correctamente")
        else:
            print("No se pudo ELIMINAR el servicioXSede")

