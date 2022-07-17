import pyttsx3 #pip install pyttsx3 #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import operator
import time
import cv2
import numpy as np
from time import time
import email
import imaplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart



engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am kankkalla Sir. Please tell me how may I help you")

def takeCommand():
    global query
    try:
            username='anishyadav232000@gmail.com'
            password='anishyadav231'

            mail=imaplib.IMAP4_SSL('imap.gmail.com')

            mail.login(username, password)

            print(mail.select('inbox'))

            mail.list()

            result,data =mail.uid('search',None,"UNSEEN")
            print(result,data)

            inbox_item_list=data[0].split()
            most_recent=inbox_item_list[-1]
            oldest=inbox_item_list[0]

            print(most_recent)
            print(oldest)

            result2,email_data=mail.uid('fetch',most_recent,'(RFC822)')
            #print(result2,email_data)

            raw_email=email_data[0][1].decode("utf-8")

            email_message=email.message_from_string(raw_email)
            print(email_message)
            word=str(email_message['From'])
           # print(email_message['To'])
            rt = word.find('anishyadav231998@gmail.com')
            print(email_message['From'],rt)
           # print(email_message['Subject'])
           # query=email_message['Subject']
            
            if(rt>0):
               query=email_message['Subject']
               print('working')
                
            
    except Exception as e:
        print('no email') 
        query='no message'          #It takes microphone input from the user and returns string output
    return query
              
               

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anishyadav232000@gmail.com', 'anishyadav231')
    server.sendmail('anishyadav231998@gmail.com', to, content)
    server.close()




def calculator():

    speak("yes sir i will calculate for you")
    speak("sir tell your mathematical function")
    speak("such as plus divided multiplied  etc")

    query = takeCommand().lower()

    try:
        def get_operator_fn(op):
            return {
                '+' : operator.add,
                '-' : operator.sub,
                'x' : operator.mul,
                'divided' :operator.__truediv__,
                'Mod' : operator.mod,
                'mod' : operator.mod,
                '^' : operator.xor,
                }[op]
        def eval_binary_expr(op1, oper, op2):
            op1,op2 = int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)
        print(eval_binary_expr(*(query.split())))
        a=eval_binary_expr(*(query.split()))
        speak(a)

    except Exception as e:

               speak(e)

def capture_image():
        
            
        cap=cv2.VideoCapture(0)
        if cap.isOpened():

            ret,frame=cap.read()
            print(ret)
            print(frame)
            connection=smtplib.SMTP('smtp.gmail.com',587)
            connection.ehlo()
            connection.starttls()
            username='anishyadav232000@gmail.com'
            password='anishyadav231'
            connection.login(username,password)
            cv2.imwrite('output9.jpg', frame)
            message = MIMEMultipart("alternative")
            fp = open('output9.jpg', 'rb')
            image = MIMEImage(fp.read())
            fp.close()
            message.attach(image)# message.as_string()
            #img='C:/Users/ANISH YADAV/Desktop/sublimepython/email_assistance/output9.jpg'
            connection.sendmail('username','anishyadav231998@gmail.com', message.as_string())
            connection.quit()
            
        else:

            ret=False   







           
            #delete_email()         


if __name__ == "__main__":
        wishMe()

        while True:
                
            



            
            query = takeCommand().lower()
            if 'capture image'  in query:
                    
                    capture_image()
                               
            elif 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")


            elif 'play music' in query:
                music_dir = 'F:/PANJABI SONG FOLDER'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codePath = "C:/Users/ANISH YADAV/Desktop/sublimepython"
                os.startfile(codePath)

            elif 'email to Anish' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "anishyadav231998@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry. I am not able to send this email")

            elif 'who made you'  in query:

                  speak("i have been created by Anish yadav ")
            elif 'calculator' in   query:

                  calculator()
            elif 'close' in query:
                  print('close')                   
            elif 'you' in query:
                  print('all')            

            elif 'announcement' in query:
                 
                 for i in range(0,3):
                     speak(query)
      