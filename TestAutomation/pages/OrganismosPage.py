import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Funciones.Funciones import Funciones
from txt.CreatWriteRead import *


class OrganismosPage(Funciones):

    def __init__(self, driver):
        super().__init__(driver)

    # Alta Organismo

    def IrAOrganismos(self):
        Funciones.Click_Field(self, By.XPATH, "//span[text()='Organismos']")
        Funciones.captura_pantalla(self, "captura IrAOrganismos")

    def ClickCrearOrganismo(self):
        Funciones.Click_Field(self, By.XPATH, "//button[contains(.,'+ Crear Organismo')]")
        Funciones.captura_pantalla(self, "captura ClickCrearOrganismo")

    def InputNombreOrganismo(self, organismo):
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='organismo'])[2]", organismo)
        Funciones.Click_Field(self, By.XPATH, "(//button[contains(.,'Guardar')])[2]")
        time.sleep(1)

    def ClickGuardarOrganismo(self):
        try:
            NameVariable = 0
            NameVariable += 1
            Nombre = "AltaOrganismoAutomatizada"
            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[normalize-space()='El nombre ingresado ya existe.']").text
            ChangeNombre = Nombre + f'{NameVariable} '

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariable += 1
                ChangeNombre = Nombre + f'{NameVariable}'
                Funciones.Clear_Field(self, By.XPATH, "(//input[@id='organismo'])[2]")
                Funciones.Input_Texto(self, By.XPATH, "(//input[@id='organismo'])[2]", ChangeNombre)
                Funciones.Click_Field(self, By.XPATH, "(//button[contains(.,'Guardar')])[2]")
        except:
            assert True
            Funciones.captura_pantalla(self, "captura ClickGuardarOrganismo")

        # if Nombre != ChangeNombre:
        #     nombre = ChangeNombre
        #     Status = "True"
        #     dir_path = r"../txt"
        #     file_name = "ABM-Organismo.csv"
        #     file_path = os.path.join(dir_path, file_name)
        #     CreateWriterRead.CrearDocumento(self, file_path, nombre, Status)
        # else:
        #     Funciones.captura_pantalla(self, "captura ClickGuardarOrganismo")

    def ValidateToastAlta(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Organismo Creado correctamente.":

            print("Se pudo crear el organismo correctamente")

            Funciones.captura_pantalla(self, "captura organismo creado correctamente")
        else:
            print("No se pudo dar de alta el organismo")

    ####################################################
    # Baja Organismo

    def filtrarNombreOrganismo(self, nuevoorganismo):
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='name-organismo']", nuevoorganismo)
        Funciones.captura_pantalla(self, "captura filtrarNombreOrganismo")

    def ClickBorrarOrganismo(self):
        Funciones.Click_Field(self, By.XPATH, "//span[@class='bx bx-trash']")

    def ConfirmarBaja(self):
        try:
            element2 = WebDriverWait(self.driver, timeout=5).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  "//h5[contains(text(),'Este organismo cuenta con servicios asociados, no puede ser borrado.')]"))
            ).text

            if element2 == "Este organismo cuenta con servicios asociados, no puede ser borrado.":
                print("No se pudo borrar el organismo porque tiene servicios asociados")
                Funciones.captura_pantalla(self, "captura organismo baja fallo por tener servicios asociados")
        except:
            Funciones.Click_Field(self, By.XPATH, "//button[text()='Borrar']")
            Funciones.captura_pantalla(self, "captura ConfirmarBaja")

    def ValidateToastBAJA(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Registro borrado exitosamente.":

            print("Se pudo borrar el registro correctamente")
            Funciones.captura_pantalla(self, "captura organismo eliminado correctamente")
        else:
            print("No se pudo dar de baja el organismo")
            Funciones.captura_pantalla(self, "captura No se pudo dar de baja el organismo")

    ################################################
    # Edicion Organismo

    def ClickBotonEditar(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@data-bs-target='#myModaleditar']")
        Funciones.captura_pantalla(self, "captura ClickBotonEditar")

    def InputNombreEditado(self, nombreEdicionOrganismo):
        Funciones.Clear_Field(self, By.XPATH, "(//input[@id='organismo'])[1]")
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='organismo'])[1]", nombreEdicionOrganismo)
        Funciones.Click_Field(self, By.XPATH, "//button[@type='submit']")
        Funciones.captura_pantalla(self, "captura InputNombreEditado")
        # time.sleep(1)

    def ClickConfirmarEdicion(self, nombreEdicionOrganismo):
        try:
            NameVariable = 0
            NameVariable += 1
            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[normalize-space()='El nombre ingresado ya existe.']").text
            ChangeNombre = nombreEdicionOrganismo + f'{NameVariable} '

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariable += 1
                ChangeNombre = nombreEdicionOrganismo + f'{NameVariable}'
                Funciones.Clear_Field(self, By.XPATH, "(//input[@id='organismo'])[1]")
                Funciones.Input_Texto(self, By.XPATH, "(//input[@id='organismo'])[1]", ChangeNombre)
                Funciones.Click_Field(self, By.XPATH, "//button[@type='submit']")
        except:
            assert True
            Funciones.captura_pantalla(self, "captura ClickGuardarOrganismo")

    def ValidateToastEdicion(self):
        element = WebDriverWait(self.driver, timeout=6).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Organismo Actualizado correctamente.":
            print("Se pudo editar el organismo correctamente")
            Funciones.captura_pantalla(self, "captura organismo editado correctamente")
        else:
            print("No se pudo editar el organismo")
            Funciones.captura_pantalla(self, "captura No se pudo editar el organismo")
