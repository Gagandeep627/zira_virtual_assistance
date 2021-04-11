#ZIRA desktop voice assistant


import datetime
import pyttsx3
import webbrowser
import os
import random
import smtplib
import speech_recognition as sr

# Initialize the engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
  
# Function to convert text to
# speech
def SpeakText(command):
    engine.say(command) 
    engine.runAndWait()

def sendemail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("email", "pass")
    server.sendmail("email", to, content)
    server.close()

#taking input from user from audio
query = ""
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)
    
     
print("Recognizing...")    
query += r.recognize_google(audio, language='en-in') #Using google for voice recognition.
print(f"User said: {query}\n")  #User query will be printed.

#greeting acc to time done
if "wish me" in query:
    def wishme():
        time_now = datetime.datetime.now().hour
        if time_now >= 0 and time_now < 12:
            x = "morning"
        if time_now >= 12 and time_now < 18:
            x = "afternoon"
        if time_now >= 18:
            x = "evening"


        SpeakText("hello sir, im zira your virtual assistant " + " good " + "" + str(x))

    wishme()
      
#searching webbrowser:

if "open" in query:
    new_query = query.replace("open", "opening")
    SpeakText(new_query)
    query.replace("open", "")
    query.lower()
    new_query = str(query) + ".com"
    webbrowser.open(new_query)

# playing music:
if "play music" in query.lower():
    music_dir = "C:\\Users\\Singh\\Music"
    songs = os.listdir(music_dir)
    random_num = random.choice(songs)
    SpeakText("playing " + str(random_num))
    os.startfile(os.path.join(music_dir, random_num))
#time for instance
if "time" in query.lower():
    now_time = datetime.datetime.now().strftime("%H:%M;%S")
    SpeakText(f"sir the time is :{now_time}")

#opening code my defalut vs code using os module
if "open code" in query.lower():
    code_path = "C:\\Users\\Singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    SpeakText(str(query.replace("open", "opening")))
    os.startfile(code_path)

#send a mail 
if "send mail" in query:
    SpeakText("okay .. what do you want to say :")
    content = str(input("enter content :"))
    to = str(input("enter the mail address :"))
    sendemail(to, content)
    SpeakText("check your email. its sent.")




      