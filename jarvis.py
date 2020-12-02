import pyttsx3
import datetime
import getpass
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
voices = engine.setProperty('voices',voices[1].id)
mail_address ={'example':'examples mail adress'}
#method to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    #before running this install the whl file by running command "pip install <filename with extension>"
    #I have attached the audio whl file also

#method to wish
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<4:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am Dwight, how can i help you?")

#it takes microphone input from user returns string as output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1 #seconds before the listening is stoppe
        audio = r.listen(source)
    try:
        print("Recogninzing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said {}\n".format(query) )
    except Exception as e:
        speak("Sorry, I didn't get you! come again")
        return "None"
    return query

def sendMail(to, content):
    print(to)
    content = content + "\n This is test mail from Jarvis \n\n Thank you"
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("yourmail-id","your password")
    server.sendmail("your mail-id",to,content)
    server.close()


if __name__ == "__main__":
    speak("welcome " + getpass.getuser())    
    wishMe()
    while(True):
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            res = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(res)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
        
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')

        elif 'play music' in query:
            mdir = "complete directory path where it contains music"
            songs = os.listdir(mdir)
            n = random.randint(0,len(songs))
            os.startfile(os.path.join(mdir, songs[n]))

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is"+time)
        
        elif 'the date' in query:
            date = datetime.date.today()
            speak("The date is "+str(date)) 
        
        elif 'open VS Code' in query:
            pat = "C:\\Users\\RavikiranArasur\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #Location of vscode
            os.startfile(pat)
    
        elif 'open chrome' in query:
            pat = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(pat)

        elif 'send email' in query:
            try:
                speak("What should i send?")
                content = takeCommand()
                speak("To Whom")
                to = takeCommand().lower()
                if to in mail_address:
                    sendMail(mail_address[to], content)
                    speak("Your E-mail has been sent successfully")
                else:
                    speak("user not found! try again")

            except Exception as e:
                speak("Sorry! Unable to send the mail try again later")
        
        elif 'stop' in query:
            speak("Adios amigo!! see you later")
            break

        else:
            speak("if you want to stop! say stop")
    
