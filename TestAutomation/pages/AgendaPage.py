import time
from datetime import date, timedelta, datetime

from Funciones.Funciones import Funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AgendaPage(Funciones):

    def __init__(self, driver):
        super().__init__(driver)

    #########################################################################################
    # alta Agenda

    def VolverAlHome(self):
        Funciones.Click_Field(self, By.XPATH, "(//span[normalize-space()='Mi cuenta'])[1]")

    def IraAgenda(self):
        Funciones.Click_Field(self, By.XPATH, "//span[normalize-space()='Agenda']")

    def CrearAgenda(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@data-bs-target='#myModalNew']")

    def EscribirNombreAgenda(self, nombreAgenda):
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", nombreAgenda)

    def SeleccionarOrganismo_Servicio_Sede(self, organismoAutomatizado, servicioAutomatizado, sedeAutomatizada):
        Funciones.Click_Field(self, By.XPATH, "//select[@id='organismo']")
        Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{organismoAutomatizado}']")

        Funciones.Click_Field(self, By.XPATH, "//select[@id='servicio']")
        Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{servicioAutomatizado}']")

        Funciones.Click_Field(self, By.XPATH, "//select[@id='sede']")
        Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{sedeAutomatizada}']")
        # Funciones.Click_Field(self, By.XPATH, "(//option)[1]")

        Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
        time.sleep(2)

    def GuardarAgenda(self):
        # Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
        try:
            NameVariable = 0
            NameVariable += 1
            Nombre = "AltaAgendaAutomatizada"

            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[normalize-space()='El nombre ingresado ya existe.']").text

            ChangeNombre = Nombre + f'{NameVariable} '

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariable += 1
                ChangeNombre = Nombre + f'{NameVariable}'

                # Cambiar Nombre
                Funciones.Clear_Field(self, By.XPATH, "//input[@id='nombre']")
                Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", ChangeNombre)

                Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
                time.sleep(0.5)

                nombreYaExiste = self.driver.find_element(By.XPATH,
                                                          "//div[normalize-space()='El nombre ingresado ya existe.']").text
        except:
            assert True

    def ValidateToastAltaAGENDA(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Agenda creada correctamente.":

            print("Se pudo dar de alta la AGENDA correctamente")

            Funciones.captura_pantalla(self, "captura AGENDA dada de alta correctamente")
        else:
            print("No se pudo dar de alta la AGENDA")

    #########################################################################################
    # Edicion Agenda

    def FiltrarNombreAgenda(self, nombreAgenda):
        Funciones.Input_Texto(self, By.XPATH, "(//input[@name='nombre'])[1]", nombreAgenda)

    def NuevoNombreAgenda(self, nombreAgendaEditado):
        Funciones.Clear_Field(self, By.XPATH, "(//input[@id='nombre'])[2]")
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='nombre'])[2]", nombreAgendaEditado)

    def CambiarEstadoSwitch(self):
        Funciones.Click_Field(self, By.XPATH, "(//input[@id='publicoPrivado'])[2]")

    def GuardarEdicion(self):
        Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space()='Guardar'])[2]")

    def ValidateToastEdicionAGENDA(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Datos guardados correctamente.":

            print("Se pudo editar la AGENDA correctamente")

            Funciones.captura_pantalla(self, "captura AGENDA editada correctamente")
        else:
            print("No se pudo editar la AGENDA")

    # Baja agenda

    def BorrarAgenda(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@title='Borrar']")

    def ValidateToastBajaAGENDA(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Agenda eliminada exitosamente.":

            print("Se pudo dar de baja la AGENDA correctamente")

            Funciones.captura_pantalla(self, "captura AGENDA eliminada correctamente")
        else:
            print("No se pudo eliminar la AGENDA")

    #########################################################################################
    # configurar Agenda

    def FiltrarXComponenetesAgenda(self, Agenda, organismo, Servicio):
        Funciones.Input_Texto(self, By.XPATH, "(//input[contains(@name,'nombre')])[1]", Agenda)
        Funciones.Input_Texto(self, By.XPATH, "//input[@name='nombreOrganismo']", organismo)
        Funciones.Input_Texto(self, By.XPATH, "//input[@name='nombreServicio']", Servicio)

    def ConfiguracionAgenda(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@title='Configurar']")
        time.sleep(0.5)
        Funciones.Click_Field(self, By.XPATH, "//button[contains(.,'+ Configuración')]")

    def SeleccionarDias(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@id='marcarTodo']")

    def IngresarYConfirmarDuracionTurno(self, duracionTurno):
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='duracionTurno']", duracionTurno)
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='confirmacionDuracionTurno']", duracionTurno)

    def FechasDesdeYHasta(self):
        fechaDesde = date.today().strftime("%dd-%mm-%Y")

        fechaHasta = (datetime.today() + timedelta(days=365)).strftime("%dd-%mm-%Y")

        Funciones.Input_Texto(self, By.XPATH, "//input[@id='fechaVigenciaDesde']", fechaDesde)
        Funciones.Input_Texto(self, By.XPATH, "//input[@formcontrolname='fechaVigenciaHasta']", fechaHasta)

    def AgregarFranjaHoraria(self):
        Funciones.Click_Field(self, By.XPATH, "(//span[contains(text(),'+')])[2]")

    def IngresarPrimerYUltimoTurno(self, primerTurno, ultimoTurno):
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='primerTurno']", primerTurno)
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='ultimoTurno']", ultimoTurno)

    def TurnosSimultaneos(self, turnosSimultaneos):
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='turnosSimultaneos']", turnosSimultaneos)

    def AceptarYGuardar(self):
        Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Aceptar']")
        Funciones.Click_Field(self, By.XPATH, "(//button[@type='submit'][normalize-space()='Guardar'])[1]")

    def ValidateToastAltaConfiguracionAGENDA(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Configuración de agenda creada correctamente.":

            print("Se pudo dar de alta la configuracion correctamente")

            Funciones.captura_pantalla(self, "captura AGENDA configurada correctamente")
        else:
            print("Ocurrio un problema al configurar la agenda")

    #########################################################################################
    # Publicar agenda

    def publicarAgenda(self):
        Funciones.Click_Field(self, By.XPATH, "//button[@title='Despublicada']")

    def AceptarPublicacion(self):
        Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Publicar']")

    def ValidateToastPublicarAgenda(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Agenda publicada exitosamente.":

            print("Se pudo publicar la agenda correctamente")

            Funciones.captura_pantalla(self, "captura AGENDA publicada correctamente")
        else:
            print("No se pudo publicar la agenda")
