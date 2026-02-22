import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random
duration = 5  # segundos de grabación
score= 0
errors=0
max_errors = 3 
sample_rate = 44100
palabra_español = "Manzana"
palabra_ingles = "Apple"
#lang = input("¿A qué idioma debo traducir? (ej., 'en' – inglés, 'it' – italiano): ")

words_by_level = {
    "facil": ["gato", "perro", "manzana", "leche", "sol"],
    "medio": ["banano", "escuela", "amigo", "ventana", "amarillo"],
    "dificil": ["tecnologia", "universidad", "informacion", "pronunciacion", "imaginacion"]}
print("elige tu nivel , tenemos 3 niveles :facil,medio y dificil")
level = input ("en que nivel quieres jugar:")

while level not in words_by_level:
    print ("nivel no encotrado.pon un nivel valido")
    level=input("En que nivel quieres jugar ")

word_list=words_by_level[level]
random.shuffle(word_list)
print(f"has escogido el nivel{level}")
print("veras una palabra en espanol,traducela al ingles")

recognizer = sr.Recognizer()
translator=Translator()

for word in word_list:
    print(f"la palabra es {word}")
    print("habla ahora")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="int16")
    sd.wait()
    wav.write("output.wav", sample_rate, recording)
    print("✅ Grabación completa, reconociendo...")
    try:
        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)
            recognised = recognizer.recognize_google(audio, language="en").lower()
            print("📝 Dijiste:", recognised)
            translation = translator.translate(word, src="es", dest="en").text.lower()
            print("🔤 Traducción:", translation)
            if recognised == translation:
                score += 1
                print("Correcto + 1 punto")
            else:
                errors += 1
                print(f"No esta bien se esperaba {translation}. Erroes {errors}/{max_errors}")
            if errors >= max_errors:
                print("Game over")
                break 
    except sr.UnknownValueError:
        errors += 1
        print(f"😕 No se pudo reconocer el habla. Errores: {errors}/{max_errors}")
        if errors >= max_errors:
            print("\n💀 Juego terminado. Cometiste 3 errores.")
            break
    except sr.RequestError as e:
        print(f"❗ Error del servicio: {e}")
        break
print(f"\n🏁 ¡Felicidades! Tu puntuación es: {score}")
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)
try:
    intento_usuario = recognizer.recognize_google(audio, language="en-US")
    print("📝 Dijiste:", intento_usuario)
    
    if intento_usuario.lower()== palabra_ingles.lower():
        print("exelente pronunciacion ")
    else:
        print(f"casi , pero no te equivocastes,no dijistes{intento_usuario} y era {palabra_español}")
except sr.UnknownValueError:
    print("😕 No se pudo reconocer la voz.")
except sr.RequestError as e:
    print(f"❗ Error del servicio: {e}")
