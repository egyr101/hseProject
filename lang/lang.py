import json
import random

refFileJson = "lang/json/languages.json" 

listFieldJson = ["lang_name","hello_name","input_num_name","input_dot_name","button_sqrt_name","output_res_name","settings_name",
                 "change_lang_name","add_lang_name","feedback_name","readme_name","button_save_name"]

class TextFile:
    def __init__(self, lang_name : str, hello_name : str, input_num_name : str, input_dot_name : str,
                 button_sqrt_name: str, output_res_name : str, settings_name : str, change_lang_name: str,
                add_lang_name : str, feedback_name : str, readme_name : str, button_save_name : str):
        self.id = str(random.randint(1000000000,9999999999))
        self.lang_name = lang_name
        self.hello_name = hello_name
        self.input_num_name = input_num_name
        self.input_dot_name = input_dot_name
        self.button_sqrt_name = button_sqrt_name
        self.output_res_name = output_res_name
        self.settings_name = settings_name
        self.change_lang_name = change_lang_name
        self.add_lang_name = add_lang_name
        self.feedback_name = feedback_name
        self.readme_name = readme_name
        self.button_save_name = button_save_name

    def changeId(self):
        self.id = str(int(id * 10))

    def createJson(self):
        text = {self.id : {
            "lang_name" : self.lang_name,
            "hello_name" : self.hello_name, 
            "input_num_name" : self.input_num_name,
            "input_dot_name" : self.input_dot_name,
            "button_sqrt_name" : self.button_sqrt_name,
            "output_res_name" : self.output_res_name,
            "settings_name" : self.settings_name,
            "change_lang_name" : self.change_lang_name, 
            "add_lang_name" : self.add_lang_name,
            "feedback_name" : self.feedback_name,
            "readme_name" : self.readme_name,
            "button_save_name" : self.button_save_name
        }}
        return text
    
    def validationId(data : dict, self, f : str ):
        for j in data:
            if self.id == j:
                self.changeId()
                break
    
    def setTextFile(self, id, text : dict):
        self.id = f"A{id}"
        self.lang_name = text["lang_name"]
        self.hello_name = text["hello_name"]
        self.input_num_name = text["input_num_name"]
        self.input_dot_name = text["input_dot_name"]
        self.button_sqrt_name = text["button_sqrt_name"]
        self.output_res_name = text["output_res_name"]
        self.settings_name = text["settings_name"]
        self.change_lang_name = text["change_lang_name"]
        self.add_lang_name = text["add_lang_name"]
        self.feedback_name = text["feedback_name"]
        self.readme_name = text["readme_name"]
        self.button_save_name = text["button_save_name"]

def getJson(f : str):

    with open(f, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def changeMark(data : dict, id : str, mark : bool):

    selected = data.pop(id)

    if (("A" in id and mark) or ("A" not in id and (not(mark)))):
        return None
    
    common_id = id

    if "A" in id:
        common_id = common_id[1:]

    mark_name = ""

    if (mark):
        mark_name = "A"
    
    text = {f"{mark_name}{common_id}" :  {
            "lang_name" : selected["lang_name"],
            "hello_name" : selected["hello_name"], 
            "input_num_name" : selected["input_num_name"],
            "input_dot_name" : selected["input_dot_name"],
            "button_sqrt_name" : selected["button_sqrt_name"],
            "output_res_name" : selected["output_res_name"],
            "settings_name" : selected["settings_name"],
            "change_lang_name" : selected["change_lang_name"], 
            "add_lang_name" : selected["add_lang_name"],
            "feedback_name" : selected["feedback_name"],
            "readme_name" : selected["readme_name"],
            "button_save_name" : selected["button_save_name"]
        }}
    return text

def primarySetLang(f : str):

    file_json = getJson(refFileJson)

    for j in file_json:
        if "A" in j:
            text = file_json[j]
            text_file = TextFile(text["lang_name"],text["hello_name"], text["input_num_name"],
                                text["input_dot_name"], text["button_sqrt_name"], text["output_res_name"],
                                text["settings_name"], text["change_lang_name"], text["add_lang_name"],
                                text["feedback_name"], text["readme_name"], text["button_save_name"] )
            text_file.id = j
                                
            break
    return text_file


def addLang(text : dict, f : str):

    data = getJson(f)
    data.update(text)

    with open(f,"w", encoding="utf-8") as file:
        json.dump(data,file,indent=3,ensure_ascii=False)


def setLang(textFile : TextFile, current_id : str, new_id : str, f : str):

    if (current_id == new_id):
        return False
    else:
        if (int("A" in current_id) + int("A" in new_id)) != 1:
            return False
        
        data = getJson(f)

        with open(f, "w", encoding="utf-8") as file:

            text = changeMark(data, current_id, False)
            if text == None:
                return False
            
            data.update(text)

            text = changeMark(data, new_id, True)
            if text == None:
                return False
            
            data.update(text)

            json.dump(data, file, indent=3, ensure_ascii=False)
            data = data[f"A{new_id}"]
            textFile.setTextFile(f"{new_id}",data)
        return True
