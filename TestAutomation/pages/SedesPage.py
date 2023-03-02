import time
from Funciones.Funciones import Funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SedesPage(Funciones):

    def __init__(self, driver):
        super().__init__(driver)

    # alta sedes

    def irASedes(self):
        Funciones.Click_Field(self, By.XPATH, "//span[normalize-space()='Sedes']")
        Funciones.captura_pantalla(self, "captura irASedes")

    def CrearSede(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@data-bs-target='#myModalNew']")
        Funciones.captura_pantalla(self, "captura CrearSede")

    def ingresarNombreSede(self, nuevaSede):
        Funciones.Input_Texto(self, By.XPATH, "//input[@placeholder='Ingresar nombre']", nuevaSede)
        Funciones.captura_pantalla(self, "captura ingresarNombreSede")

    def IngresarCalleAltura(self, direccion):
        time.sleep(1)
        Funciones.Input_Texto(self, By.XPATH, "//input[@placeholder='Ingresar dirección']", direccion)
        time.sleep(1)

        Funciones.Click_Field(self, By.XPATH, "(//em)[1]")
        Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
        time.sleep(2)

    def GuardarSede(self):
        try:
            NameVariable = 0
            NameVariable += 1
            Nombre = "AltaSedeAutomatizada"

            nombreYaExiste = self.driver.find_element(By.XPATH, "//div[normalize-space()='El nombre ya fue ingresado anteriormente']").text

            ChangeNombre = Nombre + f'{NameVariable}'

            while nombreYaExiste == "El nombre ya fue ingresado anteriormente":
                NameVariable += 1
                ChangeNombre = Nombre + f'{NameVariable}'

                # Ingresar nuevo nombre sede
                Funciones.Clear_Field(self, By.XPATH, "//input[@placeholder='Ingresar nombre']")
                Funciones.Input_Texto(self, By.XPATH, "//input[@placeholder='Ingresar nombre']", ChangeNombre)

                Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
                time.sleep(2)

                nombreYaExiste = self.driver.find_element(By.XPATH, "//div[normalize-space()='El nombre ya fue ingresado anteriormente']").text

        except:
            assert True

        Funciones.captura_pantalla(self, "captura GuardarSede")

    def ValidateToastAltaSede(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='toast-body']"))).text

        if element == "Sede creada correctamente.":

            print("Se pudo crear la sede correctamente")

            Funciones.captura_pantalla(self, "captura sede creada correctamente")
        else:
            print("No se pudo dar de alta la sede")
            Funciones.captura_pantalla(self, "captura No se pudo dar de alta la sede")

    # edicion sede

    def filtrarXNombre(self, Sede):
        Funciones.Input_Texto(self, By.XPATH, "//input[@name='nombre']", Sede)

    def EditarSede(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@title='Editar']")

    def NombreEditado(self, nombreEditadoSede):
        Funciones.Clear_Field(self, By.XPATH, "(//input[@id='nombre'])[2]")
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='nombre'])[2]", nombreEditadoSede)

    def AlturaYCalleEditada(self, direccion):

        Funciones.Clear_Field(self, By.XPATH, "(//input[@id='direccion'])[2]")
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='direccion'])[2]", direccion)
        time.sleep(2)

        Funciones.Click_Field(self, By.XPATH, "(//em)[1]")

    def DescripcionEditada(self, descripcion):
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='detalle'])[2]", descripcion)
        Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space()='Guardar'])[2]")
        time.sleep(2)

    def EdicionGuardar(self):
        # Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space()='Guardar'])[2]")
        try:
            NameVariable = 0
            NameVariable += 1
            Nombre = "EdicionSedeAutomatizada"

            nombreYaExiste = self.driver.find_element(By.XPATH, "(//div[normalize-space()='El nombre ya fue ingresado anteriormente'])[1]").text

            ChangeNombre = Nombre + f'{NameVariable}'

            while nombreYaExiste == "El nombre ya fue ingresado anteriormente":
                NameVariable += 1
                ChangeNombre = Nombre + f'{NameVariable}'

                # Ingresar nuevo nombre sede
                Funciones.Clear_Field(self, By.XPATH, "(//input[@id='nombre'])[2]")
                Funciones.Input_Texto(self, By.XPATH, "(//input[@id='nombre'])[2]", ChangeNombre)

                Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space()='Guardar'])[2]")
                time.sleep(2)

                nombreYaExiste = self.driver.find_element(By.XPATH, "(//div[normalize-space()='El nombre ya fue ingresado anteriormente'])[1]").text

        except:
            assert True

        Funciones.captura_pantalla(self, "captura GuardarSede")

    def ValidateToastEdicionSede(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='toast-body']"))).text

        if element == "Sede actualizada correctamente.":

            print("Se pudo Editar la sede correctamente")

            Funciones.captura_pantalla(self, "captura sede editada correctamente")
        else:
            print("No se pudo dar de alta la sede")
            Funciones.captura_pantalla(self, "captura No se pudo editar la sede")

    # Baja Sede

    def filtrarXNombreSede(self, Sede):
        Funciones.Input_Texto(self, By.XPATH, "//input[@name='nombre']", Sede)
        Funciones.captura_pantalla(self, "captura filtrarXNombreSede")

    def ConfirmarBajaSede(self):
        try:
            element2 = WebDriverWait(self.driver, timeout=5).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  "//h5[contains(text(),'Esta sede cuenta con servicios asociados, no puede ser borrada.')]"))
            ).text

            if element2 == "Esta sede cuenta con servicios asociados, no puede ser borrada.":
                print("No se pudo borrar la sede porque tiene servicios asociados")
                Funciones.captura_pantalla(self, "captura Sede baja fallo por tener servicios asociados")
        except:
            Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Borrar']")
            Funciones.captura_pantalla(self, "captura ConfirmarBajaSede")

    def ValidateToastBajaSede(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Sede eliminada exitosamente.":

            print("Sede eliminada exitosamente.")

            Funciones.captura_pantalla(self, "captura sede eliminada correctamente")
        else:
            print("No se pudo dar de baja la sede")

