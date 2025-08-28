import speech_recognition as sr
import sources
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    command = c.lower()

    if "open google" in command:
        speak("Launching Google.")
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        speak("Launching YouTube.")
        webbrowser.open("https://m.youtube.com")

    elif "open spotify" in command:
        speak("Launching Spotify.")
        webbrowser.open("https://www.spotify.com/")

    elif "open instagram" in command:  
        speak("Launching Instagram.")
        webbrowser.open("https://www.instagram.com")

    elif "open facebook" in command:
        speak("Launching Facebook.")
        webbrowser.open("https://m.facebook.com")

    elif command.startswith("play"):
        song = command.replace("play", "").strip()
        song_url = sources.musicLists.get(song)
        
        if song_url:
            speak(f"Playing {song} on YouTube.")
            webbrowser.open(song_url)
        else:
            speak("Sorry, I don't know that song.")

    else:
        speak("I don't know this command yet!")

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    try:
        while True:
            try:
                with sr.Microphone() as source:
                    print("Listening for wake word...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=3)  # more forgiving
                    wake_voice = r.recognize_google(audio)

                    if wake_voice.lower() == "hey jarvis":
                        speak("Hey, how are you sir!")
                        print("Active....")

                        with sr.Microphone() as source:
                            print("Recognising...")
                            audio = r.listen(source, phrase_time_limit=5)
                            command = r.recognize_google(audio)
                            processCommand(command)

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.WaitTimeoutError:
                speak("Sorry I didn't hear anything.")
                print("Listening timed out...")
            except sr.RequestError as e:
                speak("Sorry, I am having trouble connecting to the service.")
                print(f"API error: {e}")

    except Exception as e:
        speak("Goodbye Sir!")
        print(e)
