from datetime import date
import time
from selenium.webdriver.common.action_chains import ActionChains
from Funciones.Funciones import Funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class UsuariosPage(Funciones):

    def __init__(self, driver):
        super().__init__(driver)

    #######################################
    # Alta Usuario

    def IrAUsuarios(self):
        Funciones.Click_Field(self, By.XPATH, "//span[normalize-space()='Usuarios']")

    def CrearUsuario(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@data-bs-target='#myModalOrganismo']")

    def CampoCuit(self, nuevoUserCuit):
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", nuevoUserCuit)

    def BuscarAd(self):
        Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Buscar AD']")
        time.sleep(1)

    def seleccionarRol(self, rol):
        Funciones.Click_Field(self, By.XPATH, "(//select[@id='roles'])[1]")
        Funciones.Click_Field(self, By.XPATH, f"(//option[normalize-space()='{rol}'])[1]")

    def seleccionarOrganismo(self, organismo):
        Funciones.Click_Field(self, By.XPATH, "(//select[@id='organismos'])[1]")
        Funciones.Click_Field(self, By.XPATH, f"(//option[normalize-space()='{organismo}'])[1]")

    def GuardarUsuario(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@type='submit']")

    def ValidateToastAltaUSUARIO(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='toast-body']"))).text

        if element == "Usuario creado correctamente.":

            print("Se pudo dar de alta el usuario correctamente")

            Funciones.captura_pantalla(self, "captura Usuario dado de alta correctamente")
        else:
            print("No se pudo dar de alta el usuario")

    #################################################
    # Modificacion Usuario

    def FiltrarCuit(self, nuevoUserCuit):
        Funciones.Input_Texto(self, By.XPATH, "//input[@name='cuit']", nuevoUserCuit)

    def NuevoRolYOrganismo(self, organismo, rol):
        Funciones.Click_Field(self, By.XPATH, "(//select[@id='roles'])[2]")
        Funciones.Click_Field(self, By.XPATH, f"(//option[normalize-space()='{rol}'])[2]")

        Funciones.Click_Field(self, By.XPATH, "(//select[@id='organismos'])[2]")
        Funciones.Click_Field(self, By.XPATH, f"(//option[normalize-space()='{organismo}'])[2]")

    def EdicionGuardar(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@type='button'][normalize-space()='Guardar']")

    def ValidateToastEdicionUSUARIO(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='toast-body']"))).text

        if element == "Usuario Actualizado correctamente.":

            print("Se pudo editar el usuario correctamente")

            Funciones.captura_pantalla(self, "captura Usuario editado correctamente")
        else:
            print("No se pudo editar el usuario")

    #############################################
    # Baja Usuario

    def BorrarUsuario(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@title='Borrar']")

    def ValidateToastBajaUSUARIO(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='toast-body']"))).text

        if element == "Usuario eliminado exitosamente.":

            print("Se pudo eliminar el usuario correctamente")

            Funciones.captura_pantalla(self, "captura Usuario eliminado correctamente")
        else:
            print("No se pudo eliminar el usuario")

    ##############################################
    # Asignacion Perfil

    def AsignarPerfil(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@title='Asignar Perfil']")

    def seleccionarPerfil(self, Perfil):
        Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space() ='{Perfil}']")

    def GuardarAsignacion(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@data-bs-dismiss='modal'][normalize-space()='Guardar']")

    def ValidateToastAsignacionPerfil(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='toast-body']"))).text

        if element == "Usuario perfil editado correctamente.":

            print("Se pudo Asignar el perfil correctamente")
            Funciones.captura_pantalla(self, "captura perfil asignado correctamente")

        else:
            print("No se pudo asignar perfil al usuario")
            Funciones.captura_pantalla(self, "captura asignacion perfil a usuario fallo")

