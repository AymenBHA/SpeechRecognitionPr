
# coding: utf-8

import subprocess
import os


class commander:
    def __init__(self):
        self.confirm=["yes","affirmative","si","sure","do it","yeah","confirm"]
        self.cancel = ["no","negative","negative soldier","don't","wait","cancel"]
        
    def descover(self,text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.respond("you haven't told me your name yet")
            else:
                self.respond("my name is python commander , How are you ?")
   
    def respond(self,response):
        print(response)
        subprocess.call("say"+response,shell=True)

