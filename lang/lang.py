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
        self.id = id
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


def validationJson(f, data):

    checkLenElem = False

    for j in data:

        try:
            checkLenElem = False
            elem = TextFile(j["lang_name"], j["hello_name"], j["input_num_name"], j["input_dot_name"],
                        j["button_sqrt_name"], j["output_res_name"], j["settings_name"], j["change_lang_name"],
                        j["add_lang_name"], j["feedback_name"], j["readme_name"], j["button_save_name"])
            checkLenElem = len(j) == 12
        except:
            return False
        
        if checkLenElem:
            return False
        
    return True

def getJson(f : str):

    with open(f, "r", encoding="utf-8") as file:
        data = json.load(file)
#     if not(validationJson(f,data)):
#         return None
    return data 

def changeMark(data : dict, id : str, mark : bool):
    print(1)
    selected = data.pop(id)

    if (("A" in id and mark) or ("A" not in id and (not(mark)))):
        return None
    common_id = id

    mark_name = ""

    if (mark):
        mark_name = "A"
    else:
        common_id = id[1:]
    
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
    print(mark_name+common_id)
    return text

def primarySetLang(f : str):

    

    file_json = getJson(refFileJson)

    # if not(validationJson(f,file_json)):
    #     return None

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

    # if not(validationJson(f,data)):
    #     return None
    data.update(text)

    with open(f,"w", encoding="utf-8") as file:
        json.dump(data,file,indent=3,ensure_ascii=False)

def setLang(textFile : TextFile, current_id : str, new_id : str, f : str):
    
    if (int("A" in current_id) + int("A" in new_id)) != 1:
        print("A" in current_id + "A" in new_id)
        return None
    
    data = getJson(f)
    # if not(validationJson(f)):
    #     return None,None



    with open(f, "w", encoding="utf-8") as file:

        text = changeMark(data, current_id, False)
        if text == None:
            return None
        
        data.update(text)

        text = changeMark(data, new_id, True)
        if text == None:
            return None
        
        data.update(text)

        json.dump(data, file, indent=3, ensure_ascii=False)
        data = data[f"A{new_id}"]
        textFile.setTextFile(f"A{new_id}",data)
    # return f"A{new_id}", TextFile(data["lang_name"], data["hello_name"], data["input_num_name"], data["input_dot_name"],
    #                     data["button_sqrt_name"], data["output_res_name"], data["settings_name"], data["change_lang_name"],
    #                     data["add_lang_name"], data["feedback_name"], data["readme_name"], data["button_save_name"])