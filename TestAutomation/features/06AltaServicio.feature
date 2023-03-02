Feature: Alta Servicio automatizado.

  Background:
    Given Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

  Scenario Outline: Alta Servicio
    When Escribiendo campo CUIT "<cuit>"
    When Escribiendo password "<password>"
    When Click en boton ingresar
    When Click en servicios
    When Click en boton crear servicio
    When Seleccionar un organismo "<organismo>"
    When Ingresar un nombre de servicio "<Servicio>"
    When Ingresar cantidad maxima de turnos por ciudadano "<cantMaximaTurnos>"
    When Ingresar tiempo Pre-Cancelacion cita "<tiempoPreCancelacion>"
    When Ingresar tiempo espera para toma turno "<tiempoEspera>"
    When Ingresar URL "<url>"
    When Seleccionar servicio de cancelacion
    When Seleccionar si requiere Login Con Miba
    When Seleccionar Documento admitido
    When Seleccionar orden de preferencia "<lugar>" "<fecha>" "<proximo>"
    When Click en Guardar servicio "<Servicio>"
    Then Validar Alta servicio


    Examples:
      | cuit        | password | Servicio    | cantMaximaTurnos | tiempoPreCancelacion | tiempoEspera | url                       | organismo             | proximo | fecha | lugar |
      | 27395625123 | Troquel1 | ServicioAAT | 22               | 120                  | 22           | https://www.google.com.ar | OrganismoAutomatizado | Próximo | Fecha | Lugar |