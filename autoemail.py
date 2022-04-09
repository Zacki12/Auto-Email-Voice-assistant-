import speech_recognition as sr 
import yagmail

recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print("Clearing Background noise..")
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("waiting for you message...")
    recordedaudio=recognizer.listen(source)
    print("done recording...!")
try:
     print('Printing the message..')
     text=recognizer.recognize_google(recordedaudio,language='en-US')

     print('your message:{}'.format(text))
except Exception as ex:
    print(ex)


reciver='muzammil.idrees.bsse-2018b@cecosian.edu.pk' 
message=text
sender=yagmail.SMTP('xyz@gmail.com')
sender.send(to=reciver,subject='This ia as automated mail', contents=message)   

#Instagram: @zackkhan12
# Github: @zacki12 



