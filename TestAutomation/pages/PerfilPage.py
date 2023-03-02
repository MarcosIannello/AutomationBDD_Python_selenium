import time
from datetime import date, timedelta, datetime

from Funciones.Funciones import Funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PerfilPage(Funciones):

    def __init__(self, driver):
        super().__init__(driver)

    #########################################################################################
    # alta perfil

    def irAPerfiles(self):
        Funciones.Click_Field(self, By.XPATH, "//span[normalize-space()='Perfiles']")

    def crearNuevoRegistro(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@data-bs-target='#myModalNew']")

    def NombrePerfil(self, Perfil):
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='perfil'])[1]", Perfil)
        Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space()='Guardar'])[1]")
        time.sleep(0.5)

    def GuardarPerfil(self, Perfil):
        try:
            NameVariable = 0
            NameVariable += 1
            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[normalize-space()='El nombre ingresado ya existe.']").text

            ChangeNombre = Perfil + f'{NameVariable}'

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariable += 1
                ChangeNombre = Perfil + f'{NameVariable}'

                Funciones.Clear_Field(self, By.XPATH, "(//input[@id='perfil'])[1]")
                Funciones.Input_Texto(self, By.XPATH, "(//input[@id='perfil'])[1]", ChangeNombre)

                Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space()='Guardar'])[1]")
        except:
            assert True

    def ValidateToastAltaPerfil(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Perfil creado correctamente.":

            print("Se pudo crear el perfil correctamente")

            Funciones.captura_pantalla(self, "captura perfil creado correctamente")
        else:
            print("No se pudo crear lel perfil")

    #########################################################################################
    # Modificacion perfil

    def filtrarXNombre(self, Perfil):
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='name-perfil']", Perfil)

    def nuevoNombrePerfil(self, PerfilEditado):
        Funciones.Clear_Field(self, By.XPATH, "(//input[@id='perfil'])[2]")
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='perfil'])[2]", PerfilEditado)
        Funciones.Click_Field(self, By.XPATH, "(//button[@type='submit'])[2]")
        time.sleep(0.5)

    def GuardarEdicion(self, PerfilEditado):
        try:
            NameVariable = 0
            NameVariable += 1
            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[normalize-space()='El nombre ingresado ya existe.']").text

            ChangeNombre = PerfilEditado + f'{NameVariable}'

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariable += 1
                ChangeNombre = PerfilEditado + f'{NameVariable}'

                Funciones.Clear_Field(self, By.XPATH, "(//input[@id='perfil'])[2]")
                Funciones.Input_Texto(self, By.XPATH, "(//input[@id='perfil'])[2]", ChangeNombre)

                Funciones.Click_Field(self, By.XPATH, "(//button[@type='submit'])[2]")
        except:
            assert True

    def ValidateToastModificacionPerfil(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Perfil actualizado correctamente.":

            print("Se pudo Modificar el perfil correctamente")

            Funciones.captura_pantalla(self, "captura perfil editado correctamente")
        else:
            print("No se pudo editar el perfil")

    #########################################################################################
    # Baja perfil

    def ValidateToastBajaPerfil(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Perfil borrado exitosamente.":

            print("Se pudo eliminar el perfil correctamente")

            Funciones.captura_pantalla(self, "captura perfil eliminado correctamente")
        else:
            print("No se pudo borrar el perfil")

    #########################################################################################
    # Asociacion agrupacionSede a perfil

    def ClickAsociarASedeAPerfil(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@title='Asignar Agrupación de Sede']")

    def seleccionarAgrupacionSede(self, AgrupacionSede):
        Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{AgrupacionSede}']")
        time.sleep(0.5)

    def guardarAsociacionSedes(self):
        Funciones.Click_Field(self, By.XPATH, "(//button[@type='button'][normalize-space()='Guardar'])[1]")

    def ValidateToastAsociacionAgrupacionAPerfil(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Sedes de perfil actualizadas correctamente.":

            print("Se pudo asociar a el perfil una agrupacion correctamente")
            Funciones.captura_pantalla(self, "captura asociacion a perfil OK")
        else:
            print("No se pudo asociar la agrupacion al perfil")
            Funciones.captura_pantalla(self, "captura asociacion a perfil ERROR")

    #########################################################################################
    # Asociacion agrupacionServicios a perfil

    def ClickAsociarAServiciosAPerfil(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@title='Asignar Agrupación de Servicio']")

    def seleccionarAgrupacionServicio(self, AgrupacionServicio):
        Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{AgrupacionServicio}']")
        time.sleep(1)

    def ValidateToastAsociacionAgrupacionServicioAPerfil(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Servicios de perfil actualizados correctamente.":

            print("Se pudo asociar a el perfil una agrupacion correctamente")
            Funciones.captura_pantalla(self, "captura asociacion a perfil OK")
        else:
            print("No se pudo asociar la agrupacion al perfil")
            Funciones.captura_pantalla(self, "captura asociacion a perfil ERROR")

    def GuardarAsociacionServicios(self):
        Funciones.Click_Field(self, By.XPATH, "(//button[@type='button'][normalize-space()='Guardar'])[2]")
