import time
from selenium.webdriver.common.by import By
from Funciones.Funciones import Funciones


class FlujoCompletoAgendaPage(Funciones):

    def __init__(self, driver):
        super().__init__(driver)

    ##############################################################################

    def VolverAlHome(self):
        Funciones.Click_Field(self, By.XPATH, "(//span[normalize-space()='Mi cuenta'])[1]")

    def InputNombreOrganismo(self, organismo):
        global OrganismoAgenda
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='organismo'])[2]", organismo)
        Funciones.Click_Field(self, By.XPATH, "(//button[contains(.,'Guardar')])[2]")
        OrganismoAgenda = organismo
        # print(OrganismoAgenda)
        time.sleep(1)

    def ClickGuardarOrganismo(self, Organismo):
        global OrganismoAgendaFin, NameVariable
        try:
            NameVariable = 0
            NameVariable += 1
            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[normalize-space()='El nombre ingresado ya existe.']").text
            ChangeNombre = Organismo + f'{NameVariable}'

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariable += 1
                ChangeNombre = Organismo + f'{NameVariable}'
                Funciones.Clear_Field(self, By.XPATH, "(//input[@id='organismo'])[2]")
                Funciones.Input_Texto(self, By.XPATH, "(//input[@id='organismo'])[2]", ChangeNombre)
                Funciones.Click_Field(self, By.XPATH, "(//button[contains(.,'Guardar')])[2]")
                OrganismoAgendaFin = ChangeNombre
        except:
            assert True
            Funciones.captura_pantalla(self, "captura ClickGuardarOrganismo")

# """SELECCION CORRECTA A LA PRIMERA SOLUCION ACA"""
    def SeleccionarOrganismo(self):
        time.sleep(1)
        Funciones.Click_Field(self, By.XPATH, "(//select[@id='organismo'])[1]")
        time.sleep(1)
        if NameVariable < 2:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{OrganismoAgenda}']")
        else:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{OrganismoAgendaFin}']")

    def ingresarNombreServicio(self, Servicio):
        global ServicioAgenda
        time.sleep(1)
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='nombre'])[1]", Servicio)
        ServicioAgenda = Servicio

    def GuardarServicio(self, Servicio):
        global ServicioAgendaFin
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
                ServicioAgendaFin = ChangeNombre
        except:
            assert True

        Funciones.captura_pantalla(self, "captura Servicio guardado")

    def ingresarNombreSede(self, Sede):
        global SedeAgenda
        Funciones.Input_Texto(self, By.XPATH, "//input[@placeholder='Ingresar nombre']", Sede)
        Funciones.captura_pantalla(self, "captura ingresarNombreSede")
        SedeAgenda = Sede

    def GuardarSede(self, Sede):
        global SedeAgendaFin
        try:
            NameVariable = 0
            NameVariable += 1
            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[normalize-space()='El nombre ya fue ingresado anteriormente']").text
            ChangeNombre = Sede + f'{NameVariable}'

            while nombreYaExiste == "El nombre ya fue ingresado anteriormente":
                NameVariable += 1
                ChangeNombre = Sede + f'{NameVariable}'

                # Ingresar nuevo nombre sede
                Funciones.Clear_Field(self, By.XPATH, "//input[@placeholder='Ingresar nombre']")
                Funciones.Input_Texto(self, By.XPATH, "//input[@placeholder='Ingresar nombre']", ChangeNombre)
                Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
                SedeAgendaFin = ChangeNombre
        except:
            assert True
            Funciones.captura_pantalla(self, "captura GuardarSede")

    def SeleccionarSede(self):
        time.sleep(0.5)
        Funciones.Click_Field(self, By.XPATH, "//select[@id='sedeId']")
        time.sleep(0.5)
        if NameVariable < 2:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{SedeAgenda}']")
        else:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{SedeAgendaFin}']")

    def SeleccionarServicio(self):
        Funciones.Click_Field(self, By.XPATH, "//select[@id='servicioId']")
        # time.sleep(0.5)
        time.sleep(0.5)
        if NameVariable < 2:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{ServicioAgenda}']")
        else:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{ServicioAgendaFin}']")

    def EscribirNombreAgenda(self, nombreAgenda):
        global nombreAgenda1
        nombreAgenda1 = nombreAgenda
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", nombreAgenda)

    def SeleccionarOrganismo_Servicio_Sede(self):
        Funciones.Click_Field(self, By.XPATH, "//select[@id='organismo']")
        time.sleep(0.5)
        if NameVariable < 2:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{OrganismoAgenda}']")
        else:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{OrganismoAgendaFin}']")

        time.sleep(0.5)
        if NameVariable < 2:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{ServicioAgenda}']")
        else:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{ServicioAgendaFin}']")

        time.sleep(0.5)
        if NameVariable < 2:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{SedeAgenda}']")
        else:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{SedeAgendaFin}']")

        Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
        time.sleep(2)

    def GuardarAgenda(self, nombreAgenda):
        global nombreAgenda2
        try:
            NameVariable = 0
            NameVariable += 1

            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[normalize-space()='El nombre ingresado ya existe.']").text

            ChangeNombre = nombreAgenda + f'{NameVariable} '

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariable += 1
                ChangeNombre = nombreAgenda + f'{NameVariable}'

                # Cambiar Nombre
                Funciones.Clear_Field(self, By.XPATH, "//input[@id='nombre']")
                Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", ChangeNombre)

                Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
                time.sleep(0.5)
                nombreAgenda2 = ChangeNombre
        except:
            assert True

    def filtrarXNombreAgenda(self):
        time.sleep(0.5)
        if NameVariable < 2:
            Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']]", nombreAgenda1)
        else:
            Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", nombreAgenda2)

