import time
from Funciones.Funciones import Funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ServiciosPage(Funciones):

    def __init__(self, driver):
        super().__init__(driver)

    # alta servicio

    def IrAServicios(self):
        Funciones.Click_Field(self, By.XPATH, "//span[text()='Servicios']")
        time.sleep(1)
        Funciones.captura_pantalla(self, "captura IrAServicios")

    def ClickCrearServicio(self):
        Funciones.Click_Field(self, By.XPATH, "(//button[contains(@data-bs-toggle,'modal')])[1]")
        Funciones.captura_pantalla(self, "captura ClickCrearServicio")

    def SeleccionarOrganismo(self, organismo):
        Funciones.Click_Field(self, By.XPATH, "(//select[@id='organismo'])[1]")
        Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{organismo}']")

    def ingresarNombreServicio(self, Servicio):
        time.sleep(1)
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='nombre'])[1]", Servicio)

    def TurnosXCiudadano(self, cantMaximaTurnos):
        Funciones.Input_Texto(self, By.XPATH, "//input[@formcontrolname='cantidadDeTurnosPorCiudadano']", cantMaximaTurnos)

    def TiempoPreCancelacion(self, tiempoPreCancelacion):
        Funciones.Input_Texto(self, By.XPATH, "//input[@formcontrolname='tiempoPreCancelacionDeCita']", tiempoPreCancelacion)

    def EsperaTiempo(self, tiempoEspera):
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='tiempoDeEsperaTurno'])[1]", tiempoEspera)

    def IngresarURL(self, url):
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='urlDestinoFinalDelCiudadano'])[1]", url)

    def ServicioCancelacion(self):
        Funciones.Click_Field(self, By.XPATH, "//input[@formcontrolname='servicioEnviaMailCancelacion']")

    def LoginMiba(self):
        Funciones.Click_Field(self, By.XPATH, "//select[@formcontrolname='loginMiba']")
        Funciones.Click_Field(self, By.XPATH, "//option[normalize-space()='Si, sin nivel de seguridad']")

    def DocumentosAdmitidos(self):
        Funciones.Click_Field(self, By.XPATH, "//option[normalize-space()='PASAPORTE']")
        # time.sleep(0.5)

    def SeleccionOrdenPreferencia(self, lugar, fecha, proximo):
        time.sleep(0.5)
        Funciones.Click_Field(self, By.XPATH, "//select[@formcontrolname='ordenPreferencia1']")
        Funciones.Click_Field(self, By.XPATH, f"//option[@value='{fecha}']")

        Funciones.captura_pantalla(self, "Captura datos cargados en servicio")

        Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
        time.sleep(0.5)

    def GuardarServicio(self, Servicio):
        try:
            NameVariable = 0
            NameVariable += 1
            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[normalize-space()='El nombre ingresado ya existe.']").text
            ChangeNombre = Servicio + f'{NameVariable} '

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariable += 1
                ChangeNombre = Servicio + f'{NameVariable}'
                Funciones.Clear_Field(self, By.XPATH, "//input[@placeholder='Ingresar nombre']")
                Funciones.Input_Texto(self, By.XPATH, "//input[@placeholder='Ingresar nombre']", ChangeNombre)
                Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
        except:
            assert True
            Funciones.captura_pantalla(self, "captura Servicio guardado")

    def ValidateToastAltaServicio(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Servicio creada correctamente.":

            print("Se pudo crear el servicio correctamente")
            Funciones.captura_pantalla(self, "captura servicio creado correctamente")
        else:
            print("No se pudo dar de alta el servicio")

    # Edicion servicio

    def FiltrarXNombreServicio(self, nombreServicio):
        Funciones.Input_Texto(self, By.XPATH, "//input[@name='nombre']", nombreServicio)
        Funciones.captura_pantalla(self, "captura FiltrarXNombreServicio")

    def ClickBotonEditarServicio(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@title='Editar']")
        Funciones.captura_pantalla(self, "captura ClickBotonEditarServicio")

    def NuevoNombreServicio(self, nombreEditadoServicio):
        Funciones.Clear_Field(self, By.XPATH, "(//input[@placeholder='Ingresar nombre'])[2]")
        Funciones.Input_Texto(self, By.XPATH, "(//input[@placeholder='Ingresar nombre'])[2]", nombreEditadoServicio)
        Funciones.captura_pantalla(self, "captura NuevoNombreServicio")

    def NuevaCantMaximaDeTurnos(self, cantMaximaTurnos):
        Funciones.Clear_Field(self, By.XPATH, "(//input[@id='cantidadDeTurnosPorCiudadano'])[2]")
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='cantidadDeTurnosPorCiudadano'])[2]", cantMaximaTurnos)
        Funciones.captura_pantalla(self, "captura NuevaCantMaximaDeTurnos")
        Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space()='Guardar'])[2]")
        time.sleep(0.5)

    def GuardarEdicionServicio(self, nombreServicioEditado):
        # Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space()='Guardar'])[2]")
        try:
            NameVariable = 0
            NameVariable += 1
            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[normalize-space()='El nombre ingresado ya existe.']").text
            ChangeNombre = nombreServicioEditado + f'{NameVariable} '

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariable += 1
                ChangeNombre = nombreServicioEditado + f'{NameVariable}'
                Funciones.Clear_Field(self, By.XPATH, "(//input[@placeholder='Ingresar nombre'])[2]")
                Funciones.Input_Texto(self, By.XPATH, "(//input[@placeholder='Ingresar nombre'])[2]", ChangeNombre)
                Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space()='Guardar'])[2]")
        except:
            assert True
            Funciones.captura_pantalla(self, "captura GuardarEdicionServicio")

    def ValidateToastEdicionServicio(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Servicio Actualizado correctamente.":

            print("Se pudo editar el servicio correctamente")

            Funciones.captura_pantalla(self, "captura servicio editado correctamente")
        else:
            print("No se pudo editar el servicio")

    # Baja Servicio

    def ClickBotonEliminar(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@title='Borrar']")
        Funciones.captura_pantalla(self, "captura ClickBotonEliminar")

    def ConfirmarBaja(self):
        Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Borrar']")
        Funciones.captura_pantalla(self, "captura ConfirmarBaja")

    def ValidateToastBajaServicio(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Servicio eliminado exitosamente.":

            print("Se pudo Eliminar el servicio correctamente")

            Funciones.captura_pantalla(self, "captura servicio Eliminado correctamente")
        else:
            print("No se pudo Eliminar el servicio")