import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("This is Millie. Please tell me what to do")

def takeCommand():
    # It takes microphone input from the user and returns string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}/n")

    except Exception as e:
       # print(e)

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'your password')
    server.sendmail('your email', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Opening Youtube")

        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Opening Google")

        elif 'open discord' in query:
            webbrowser.open_new_tab("https://www.discord.com")
            speak("Opening Discord")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'email to dad' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver's email"
                sendEmail(to,content)
                speak("The email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send the email.")


        elif 'open gmail' in query:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Opening Gmail")
            time.sleep(5)

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("Here are some headlines from the Times Of India")
            time.sleep(3)

        elif 'who made you' in query or 'who created you' in query:
            speak("I was built by the great Aaryan")
