import json
import random
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
        self.id = id * 10
refFileJson = "lang/json/languages.json"

def createJson(text_file : TextFile):
    text = {text_file.id : {
        "lang_name" : text_file.lang_name,
        "hello_name" : text_file.hello_name, 
        "input_num_name" : text_file.input_num_name,
        "input_dot_name" : text_file.input_dot_name,
        "button_sqrt_name" : text_file.button_sqrt_name,
        "output_res_name" : text_file.output_res_name,
        "settings_name" : text_file.settings_name,
        "change_lang_name" : text_file.change_lang_name, 
        "add_lang_name" : text_file.add_lang_name,
        "feedback_name" : text_file.feedback_name,
        "readme_name" : text_file.readme_name,
        "button_save_name" : text_file.button_save_name
    }}
    return text

def getJson(f : str):
    with open(f, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data 

def changeMark(data : dict, id : str, mark : bool):

    selected = data.pop(id)

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

    return text
# 
def addLang(text : dict, f : str):
    data = json.load(open(f,encoding="utf-8"))

    data.update(text)
    with open(f,"w", encoding="utf-8") as file:
        json.dump(data,file,indent=3,ensure_ascii=False)

def setLang(current_id : str, new_id : str, f : str):
    data_current = {}
    data_new = {}

    with open(f,"r",encoding="utf-8") as file:

        data = json.load(file)

    with open(f, "w", encoding="utf-8") as file:

        text = changeMark(data, current_id, False)
        data.update(text)

        text = changeMark(data, new_id, True)
        data.update(text)

        json.dump(data, file, indent=3, ensure_ascii=False)
        data = data[f"A{new_id}"]
    return f"A{new_id}", TextFile(data["lang_name"], data["hello_name"], data["input_num_name"], data["input_dot_name"],
                        data["button_sqrt_name"], data["output_res_name"], data["settings_name"], data["change_lang_name"],
                        data["add_lang_name"], data["feedback_name"], data["readme_name"], data["button_save_name"])