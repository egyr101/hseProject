import json
import random
class TextFile:
    def __init__(self,lang_name : str, text1 : str, text2 : str, text3 : str):
        self.id = random.randint(1000000000,9999999999)
        self.lang_name = lang_name
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
    def changeId(self):
        self.id = id * 10
refFileJson = "lang/json/languages.json"

def createJson(text_file : TextFile):
    text = {text_file.id : {
        "lang_name" : text_file.lang_name,
        "text1" : text_file.text1,
        "text2" : text_file.text2,
        "text3" : text_file.text3
    }}
    return text

def getJson(f : str):
    with open(f, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data 

def addLang(text : dict, f : str):
    data = json.load(open(f,encoding="utf-8"))

    data.update(text)
    with open(f,"w", encoding="utf-8") as file:
        json.dump(data,file,indent=3,ensure_ascii= False)

def setLang(id : int, f : str):
    with open(f,"r",encoding="utf-8") as file:
        data = json.load(file)[str(id)]
        return TextFile(data["lang_name"], data["text1"], data["text2"], data["text3"])