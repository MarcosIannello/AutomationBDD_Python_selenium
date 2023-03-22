import time
from selenium.webdriver.common.by import By
from Funciones.Funciones import Funciones


class FlujoCompletoAgendaPage(Funciones):

    def __init__(self, driver):
        super().__init__(driver)

    ##############################################################################

    def VolverAlHome(self):
        Funciones.Click_Field(self, By.XPATH, "(//a[@class='navbar-brand'])[1]")

    def InputNombreOrganismo(self, organismo):
        global OrganismoAgenda
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='organismo'])[2]", organismo)
        Funciones.Click_Field(self, By.XPATH, "(//button[contains(.,'Guardar')])[2]")
        OrganismoAgenda = organismo
        time.sleep(0.5)

    def ClickGuardarOrganismo(self, Organismo):
        global OrganismoAgendaFin, NameVariableOrg
        try:
            NameVariableOrg = 0
            NameVariableOrg += 1
            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[normalize-space()='El nombre ingresado ya existe.']").text
            ChangeNombre = Organismo + f'{NameVariableOrg}'

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariableOrg += 1
                ChangeNombre = Organismo + f'{NameVariableOrg}'
                Funciones.Clear_Field(self, By.XPATH, "(//input[@id='organismo'])[2]")
                Funciones.Input_Texto(self, By.XPATH, "(//input[@id='organismo'])[2]", ChangeNombre)
                Funciones.Click_Field(self, By.XPATH, "(//button[contains(.,'Guardar')])[2]")
                OrganismoAgendaFin = ChangeNombre
                time.sleep(0.5)
        except:
            assert True
            Funciones.captura_pantalla(self, "captura ClickGuardarOrganismo")

    def SeleccionarOrganismo(self):
        time.sleep(1)
        Funciones.Click_Field(self, By.XPATH, "(//select[@id='organismo'])[1]")
        time.sleep(1)

        if NameVariableOrg < 2:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{OrganismoAgenda}']")
        else:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{OrganismoAgendaFin}']")

    def ingresarNombreServicio(self, Servicio):
        global ServicioAgenda
        time.sleep(1)
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='nombre'])[1]", Servicio)
        ServicioAgenda = Servicio

    def GuardarServicio(self, Servicio):
        global ServicioAgendaFin, NameVariableSer
        try:
            NameVariableSer = 0
            NameVariableSer += 1
            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[normalize-space()='El nombre ingresado ya existe.']").text
            ChangeNombre = Servicio + f'{NameVariableSer} '

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariableSer += 1
                ChangeNombre = Servicio + f'{NameVariableSer}'
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
        global SedeAgendaFin, NameVariableSed

        try:
            NameVariableSed = 0
            NameVariableSed += 1
            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[normalize-space()='El nombre ya fue ingresado anteriormente']").text
            ChangeNombre = Sede + f'{NameVariableSed}'

            while nombreYaExiste == "El nombre ya fue ingresado anteriormente":
                NameVariableSed += 1
                ChangeNombre = Sede + f'{NameVariableSed}'

                # Ingresar nuevo nombre sede
                Funciones.Clear_Field(self, By.XPATH, "//input[@placeholder='Ingresar nombre']")
                Funciones.Input_Texto(self, By.XPATH, "//input[@placeholder='Ingresar nombre']", ChangeNombre)
                Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
                SedeAgendaFin = ChangeNombre
                time.sleep(1)
        except:
            assert True
            Funciones.captura_pantalla(self, "captura GuardarSede")

    def SeleccionarSede(self):
        time.sleep(0.5)
        Funciones.Click_Field(self, By.XPATH, "//select[@id='sedeId']")
        time.sleep(0.5)

        if NameVariableSed < 2:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{SedeAgenda}']")
        else:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{SedeAgendaFin}']")

    def SeleccionarServicio(self):
        time.sleep(0.5)
        Funciones.Click_Field(self, By.XPATH, "//select[@id='servicioId']")
        time.sleep(0.5)

        if NameVariableSer < 2:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{ServicioAgenda}']")
        else:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{ServicioAgendaFin}']")

    def EscribirNombreAgenda(self, nombreAgenda):
        global nombreAgenda1
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", nombreAgenda)
        nombreAgenda1 = nombreAgenda

    def SeleccionarOrganismo_Servicio_Sede(self):
        Funciones.Click_Field(self, By.XPATH, "//select[@id='organismo']")

        time.sleep(0.5)
        if NameVariableOrg < 2:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{OrganismoAgenda}']")
        else:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{OrganismoAgendaFin}']")

        time.sleep(0.5)
        if NameVariableSer < 2:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{ServicioAgenda}']")
        else:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{ServicioAgendaFin}']")

        time.sleep(0.5)
        if NameVariableSed < 2:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{SedeAgenda}']")
        else:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{SedeAgendaFin}']")

        Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
        time.sleep(0.5)

    def GuardarAgenda(self, Agenda):
        global nombreAgenda2, NameVariableAgenda
        time.sleep(1)
        try:
            NameVariableAgenda = 0
            NameVariableAgenda += 1

            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[normalize-space()='El nombre ingresado ya existe.']").text

            ChangeNombre = Agenda + f'{NameVariableAgenda}'

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariableAgenda += 1
                ChangeNombre = Agenda + f'{NameVariableAgenda}'

                Funciones.Clear_Field(self, By.XPATH, "//input[@id='nombre']")
                Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", ChangeNombre)
                Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
                nombreAgenda2 = ChangeNombre
        except:
            assert True
            Funciones.captura_pantalla(self, "Agenda guardada exitosamente")

    def filtrarXNombreAgenda(self):
        time.sleep(0.5)
        if NameVariableAgenda < 2:
            Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']]", nombreAgenda1)
        else:
            Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", nombreAgenda2)

