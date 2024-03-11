import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia

#initialize the speech recognizer
listener = sr.Recognizer()

#initialize the text to speech engine
engine=pyttsx3.init()

#To change voice of voice assistant
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

#to convert text to speech
def speak(text):
   engine.say(text)
   engine.runAndWait()

#To process user command
def process_command(command):
   command=command.lower()
   if "hello" in command:
      speak("Hello! How can I assist You")

   elif "date" in command:
      date=datetime.datetime.now().strftime("%D %M %Y")
      speak("Today date is" + date)
      
   #open a webpage
   elif "open website" in command:
      speak("Sure, which website would you like me to open")
      website=listen() 
      webbrowser.open(website)

   elif "time" in command:
      time=datetime.datetime.now().strftime("%H:%M %p")
      speak("Now time is" + time)

   #know about information in wikipedia
   elif "open wikipedia" in command:
      speak("Sure, which information would you like me to tells")
      about=listen()
      info=wikipedia.summary(about,1)
      speak(info)

   elif "goodbye" in command:
      speak("GoodBye!")
   else:
      speak("I'm sorry, I didn't understand that command")
      
#listen to user voice input
def listen():
    try:
        with sr.Microphone() as source:
          print("Listening.......")
          voice=listener.listen(source)
          print("Processing....")
          command=listener.recognize_google(voice)
          print("You said:",command)
          return command
        
    except sr.UnknownValueError:
       print("Sorry, I couldn't understand your speech")
    except sr.RequestError:
       print("Sorry, There was an issuse with the speech recognition service")

#Vioce assistant
while True:
   speak("How can I assist you?")
   command=listen()
   if "goodbye" in command:   
      process_command(command)
      break
   else:
      process_command(command)

