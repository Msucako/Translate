# Görev #3
import requests
from collections import defaultdict
from translate import Translator

# Görev #5
questions = {'adın ne?' : "ben süper havalı bir botum ve amacım size yardım etmek!",
             "kaç yaşındasın?" : "bu çok felsefi bir soru..."}

class TextAnalysis():   
    
    # Görev #1

    memory = defaultdict(list)
        

    def __init__(self, text, owner):

        # Görev #2

        TextAnalysis.memory[owner].append(self)
        self.text = text
        self.translation = self.__translate(self.text, "tr", "en")

        # Görev #6
        #self.response = self.get_answer()
        #if self.text.lower() in qwstions.keys():
            #self.response = self.getkey_(self.get_answer)
        #else:
            #self.response = self.get_answer()

    
    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "tr")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            # Görev #4
            cevirmen= Translator(from_lang=from_lang, to_lang=to_lang)
            ceviri= cevirmen.translate(text)
            return ceviri
        except:
            return "Çeviri girişimi başarısız oldu"


