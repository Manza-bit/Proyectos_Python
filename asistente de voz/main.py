import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#escuchar nuestro microfono y debolver el audio
def tranformar_audio_en_texto():
    #almacenar recognizer en variable
    r= sr.Recognizer()

    #configurar el microfono
    with sr.Microphone() as origen:

        #Tiempo de espera
        r.pause_threshold = 0.8

        #informar que comenzo la grabacion
        print("Ya puedes hablar")

        # Guardar lo que escuches como audio
        audio = r.listen(origen)

        try:
            #Buscar en google

            pedido = r.recognize_google(audio, language="es-ES")
            print("dijiste: "+ pedido)

            #Prueba de que pudo ingresar

            return pedido
        #En caso que no pueda
        except sr.UnknownValueError:
            print("ups , no entendi")
            return"sigo esperando"
        except sr.RequestError:
            print("ups , no hay servicio")
            return "sigo esperando"
        except:
            print("ups , algo salio mal")
            return "sigo esperando"




#funcion para que el asistente pueda hablar
def hablar(mensaje):

    #encender el motor de pyttsx3
    engine = pyttsx3.init()
    #velocidad de lectura
    engine.setProperty('rate', 170)
    """
    engine.setProperty("voice" , id1)
    """
    engine.say(mensaje)
    engine.runAndWait()



#engine = pyttsx3.init()
#for voz in engine.getProperty("voices"):
#    print(voz)
#hablar("Estas ecuchando un bot automatizado para la prueba")



#id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

#hablar("hola manza espero que tengas un buen dia")

#informar dia de la semana
def pedir_dia():
    #crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    #crear variable dia semana
    dia_semana = dia.weekday()
    print(dia_semana)

    calendario =  {
        0:"Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo"}
    #decir dia de la semana
    hablar(f"..hoy es {calendario[dia_semana]} y la fecha completa es {dia}")
#pedir_dia()

#Informar hora
def pedir_hora():
    #crear primero una variable con datos de la hora
    hora=datetime.datetime.now()

    hora = (f"..En este momento son las {hora.hour} horas con {hora.minute} y {hora.second} segundos")
    hablar(hora)

#pedir_hora()

#tranformar_audio_en_texto()

#funcion saludo
def saludo_inicial():
    #crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches "
    elif  6 <= hora.hour <= 13:
        momento = "Buenos dias "
    else:
        momento = "Buenas tardes "

    #decir el saludo
    hablar(f" .. {momento}  Soy Elena, tu asistente personal. Por favor, dime en que te puedo ayudar")
#funcion central del asistente
def pedir_cosas():

    #Saludar
    saludo_inicial()
    comenzar = True
    while comenzar:

        #activar el micro y guardar el pedido
        pedido = tranformar_audio_en_texto().lower()
        if "abrir youtube" in pedido:
            hablar(".Con gusto, estoy abriendo YouTube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif "abrir navegador" in pedido:
            hablar("claro,  ahora lo hago")
            webbrowser.open("https://www.google.com")
            continue
        elif "qué día es hoy" in pedido:
            pedir_dia()
            continue
        elif "qué hora es" in pedido:
            pedir_hora()
        elif "busca en wikipedia" in pedido:
            hablar("Buscando eso en wikipedia")
            pedido = pedido.replace("wikipedia" , "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siquiente:')
            hablar(resultado)
        elif "busca en internet" in pedido:
            hablar("ahora lo hago")
            pedido = pedido.replace("busca en internet" , '')
            pywhatkit.search(pedido)
            hablar(".. esto es lo que he encontrado")
            continue
        elif "reproduce" in pedido:
            hablar(".. Okey")
            pedido = pedido.replace("reproduce" , '')
            pywhatkit.playonyt(pedido)
            continue
        elif "broma" in pedido:
            hablar(".. jeje")
            hablar(pyjokes.get_joke("es"))
            continue
        elif "precio de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera = {"apple" : "APPL",
                       "amazon": "AMZN",
                       "google" : "GOOGL"}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"La encontre, le precio de {accion} es {precio_actual}")
                continue
            except:
                hablar("Perdon pero no la he encontrado")
                continue

        elif "adiós" in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break
pedir_cosas()