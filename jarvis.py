import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good morning")
    elif hour >=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am jarvis sir. How can i help you?")

def takeCommand():
    ''' it takes microphone input from the user and return output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold =1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please ...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('arronynstu18@gmail.com',"autosuggestion18")
    server.sendmail("arronynstu18@gmail.com",to,content)
    server.close()

if __name__ == "__main__":
    WishMe()
    # takeCommand()
    while True:
        query=takeCommand().lower()
        
        # logic for executing tasks based on query 
        if 'wikipedia' in query:
            speak('Searching Wikipedia ...')
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open prothom alo" in query:
            webbrowser.open("prothomalo.com")
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            musicdir="C:\\Users\\AR RONY\\Desktop\\musicDir"
            songs=os.listdir(musicdir)
            print(songs)
            os.startfile(os.path.join(musicdir,songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H%M%S")
            speak(f"sir ,the time is {strTime}")
        elif 'open code' in query:
            codepath="C:\\Users\\AR RONY\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "email to harry" in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to = "marrony92@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my frined,email can't send ")


