from pages.MainPage import MainPage


@given(u'Iniciando Navegador "https://openai.com/blog/chatgpt"')
def step_impl(context):
    MainPage.OpenBrowser(context)
    
    
@When(u'Ingresar Al chat')
def step_impl(context):
    MainPage.IngresarAlChat()
    

