import warnings

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service


class Funciones_driver:
    def __init__(self, driver):
        self.driver = driver

    def driver_Firefox(self, ruta):  # NAVEGADOR FIREFOX RUTA DEL DRIVE
        self.driver = ruta
        s = Service(ruta)
        self.driver = webdriver.Firefox(service=s)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def driver_Chrome(self):  # NAVEGADOR FIREFOX RUTA DEL DRIVE
        self.driver = webdriver.Chrome("C:\drivers\chromedriver.exe")

