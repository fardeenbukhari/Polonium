import json
import pyttsx3
import speech_recognition as speech
from os.path import exists


sr = speech.Recognizer()
class Main:
    def Greet(self,command):
        pyttsx3.init()
        self.greetname = 'hello',command
        pyttsx3.speak(self.greetname)
        
        
    def Speak(self,command):
        pyttsx3.init()
        pyttsx3.speak(command)
        
        
    def MicInput(self):
            try:
                with speech.Microphone() as source:
                    print('listening')
                    self.audio = sr.listen(source)
                    self.result = sr.recognize_google(self.audio,language='eng-in')
                    self.result = self.result.lower()
                    print(self.result)
                        
            except Exception as e:
                Program.MicInput()
                
                
    def LogicEngine(self):
        
        if 'how' and 'are' and 'you' in Program.result:
            Program.Speak('Thanks for asking doing good')
            
        if 'what' and 'is' and 'my' and 'name' in Program.result:
            Program.Speak(Program.getProfile[0]['name'])
        

    def ConfigCheck(self):
        fileExist = exists('config.json')
        if fileExist == True:
            with open('config.json') as config:
                self.getProfile = json.load(config)
                Program.Greet(self.getProfile[0]['name'])
                Program.MicInput()


        else:
            Program.Speak('Please enter your name')
            self.input = input('name : ')
            Program.Greet(self.input)
            profile = [{'name':self.input}]
            with open('config.json','w') as config:
                json.dump(profile,config)
            Program.MicInput()





Program = Main()
Program.ConfigCheck()
Program.LogicEngine()