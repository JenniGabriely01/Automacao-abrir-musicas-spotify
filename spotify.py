import speech_recognition as sr
import webbrowser
import time
import pyautogui

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga o nome da música que deseja ouvir...")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse:", text)

        search_query = text.replace(" ", "+")
        spotify_url = f"https://open.spotify.com/search/{search_query}"

        webbrowser.open(spotify_url)
        time.sleep(7)  

        pyautogui.moveTo(744, 454, duration=1)  
        pyautogui.click()


    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError:
        print("Erro na requisição ao Google Speech API.")
