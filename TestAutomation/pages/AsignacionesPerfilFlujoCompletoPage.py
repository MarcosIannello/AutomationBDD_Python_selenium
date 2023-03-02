import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Funciones.Funciones import Funciones


class AsignacionesPerfilFlujoCompletoPage(Funciones):

    def __init__(self, driver):
        super().__init__(driver)

    #########################################################

    def NombrePerfilFC(self, Perfil):
        global Perfil1
        Funciones.Input_Texto(self, By.XPATH, "(//input[@id='perfil'])[1]", Perfil)
        Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space()='Guardar'])[1]")
        Perfil1 = Perfil
        time.sleep(0.5)

    def GuardarPerfilFC(self, Perfil):
        global Perfil2, NameVariablePerfil
        try:
            NameVariablePerfil  = 0
            NameVariablePerfil += 1
            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[normalize-space()='El nombre ingresado ya existe.']").text

            ChangeNombre = Perfil + f'{NameVariablePerfil}'

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariablePerfil += 1
                ChangeNombre = Perfil + f'{NameVariablePerfil}'

                Funciones.Clear_Field(self, By.XPATH, "(//input[@id='perfil'])[1]")
                Funciones.Input_Texto(self, By.XPATH, "(//input[@id='perfil'])[1]", ChangeNombre)
                Funciones.Click_Field(self, By.XPATH, "(//button[normalize-space()='Guardar'])[1]")
                Perfil2 = ChangeNombre
        except:
            assert True
            Funciones.captura_pantalla(self, "captura ClickGuardarPerfil")

    #####################################################################################

    def IngresarNombreAgrupacion(self, AgrupacionSedes):
        global AgrupacionSedes1
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", AgrupacionSedes)
        AgrupacionSedes1 = AgrupacionSedes

    def GuardarAgrupacion(self, AgrupacionSedes):
        global AgrupacionSedes2, NameVariableSede
        try:
            NameVariableSede = 0
            NameVariableSede += 1

            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[contains(text(),'El nombre ya fue ingresado anteriormente.')]").text

            ChangeNombre = AgrupacionSedes + f'{NameVariableSede}'

            while nombreYaExiste == "El nombre ya fue ingresado anteriormente.":
                NameVariableSede += 1
                ChangeNombre = AgrupacionSedes + f'{NameVariableSede}'
                Funciones.Clear_Field(self, By.XPATH, "//input[@id='nombre']")
                Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", ChangeNombre)
                Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
                AgrupacionSedes2 = ChangeNombre

        except:
            assert True
            Funciones.captura_pantalla(self, "captura GuardarAgrupacionSede")

    #########################################################################

    def IngresarNombreAgrupacionServicios(self, AgrupacionServicios):
        global AgrupacionServicios1
        Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", AgrupacionServicios)
        AgrupacionServicios1 = AgrupacionServicios

    def GuardarAgrupacionServicio(self, AgrupacionServicios):
        global AgrupacionServicios2, NameVariableServicio
        try:
            NameVariableServicio = 0
            NameVariableServicio += 1
            nombreYaExiste = self.driver.find_element(By.XPATH,
                                                      "//div[contains(text(),'El nombre ingresado ya existe.')]").text

            ChangeNombre = AgrupacionServicios + f'{NameVariableServicio}'

            while nombreYaExiste == "El nombre ingresado ya existe.":
                NameVariableServicio += 1
                ChangeNombre = AgrupacionServicios + f'{NameVariableServicio}'

                Funciones.Clear_Field(self, By.XPATH, "//input[@id='nombre']")
                Funciones.Input_Texto(self, By.XPATH, "//input[@id='nombre']", ChangeNombre)
                Funciones.Click_Field(self, By.XPATH, "//button[normalize-space()='Guardar']")
                AgrupacionServicios2 = ChangeNombre
        except:
            assert True
            Funciones.captura_pantalla(self, "captura GuardarAgrupacionSede")

    ################################################################################

    def filtrarXNombre(self):
        time.sleep(1.5)
        if NameVariablePerfil < 2:
            Funciones.Input_Texto(self, By.XPATH, "//input[@id='name-perfil']", Perfil1)
        else:
            Funciones.Input_Texto(self, By.XPATH, "//input[@id='name-perfil']", Perfil2)

    def seleccionarAgrupacionSede(self):
        time.sleep(2)
        if NameVariableSede < 2:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{AgrupacionSedes1}']")
            Funciones.captura_pantalla(self, "SeleccionAgrupacionSede")
        else:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{AgrupacionSedes2}']")
            Funciones.captura_pantalla(self, "SeleccionAgrupacionSede")
        time.sleep(0.5)

    def guardarAsociacionSedeAPerfil(self):
        Funciones.Click_Field(self, By.XPATH, "(//button[@type='button'][normalize-space()='Guardar'])[1]")
        time.sleep(0.4)
        Funciones.captura_pantalla(self, "Asociacion de agrupacion de sedes a perfil")

    def seleccionarAgrupacionServicio(self):
        time.sleep(2)
        if NameVariableServicio < 2:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{AgrupacionServicios1}']")
            Funciones.captura_pantalla(self, "SeleccionAgrupacionServicio")
        else:
            Funciones.Click_Field(self, By.XPATH, f"//option[normalize-space()='{AgrupacionServicios2}']")
            Funciones.captura_pantalla(self, "SeleccionAgrupacionServicio")
        time.sleep(0.5)

    def guardarAsociacionServiciosAPerfil(self):
        Funciones.Click_Field(self, By.XPATH, "(//button[@type='button'][normalize-space()='Guardar'])[2]")
        Funciones.captura_pantalla(self, "Asociacion de agrupacion de servicios a perfil")

    def ValidateToastAsociacionAgrupacionServicioAPerfil(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))).text

        if element == "Servicios de perfil actualizados correctamente.":

            print("Se pudo asociar a el perfil una agrupacion correctamente")
            Funciones.captura_pantalla(self, "captura asociacion a perfil OK")
        else:
            print("No se pudo asociar la agrupacion al perfil")
            Funciones.captura_pantalla(self, "captura asociacion a perfil ERROR")
