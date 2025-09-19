#гугл форма
import lang.lang as l

# text1,text2,text3 = "aaasdaaрфыврфsd","dsssfdsfs","aaasdыфовфрaasd"
# text4,text5,text6 = "aaasdaaрфыврфsd","dsssfdsfs","aaasdыфовфрaasd"
# text7,text8,text9 = "aaasdaaрфыврфsd","dsssfdsfs","aaasdыфовфрaasd"
# text10,text11,text12 = "aaasdaaрфыврфsd","dsssfdsfs","aaasdыфовфрaasd"

file_json = l.getJson(l.refFileJson)

text_file = None
text_file_input = None

for j in file_json:
    if "A" in j:
        text = file_json[j]
        text_file = l.TextFile(text["lang_name"],text["hello_name"], text["input_num_name"],
                            text["input_dot_name"], text["button_sqrt_name"], text["output_res_name"],
                            text["settings_name"], text["change_lang_name"], text["add_lang_name"],
                            text["feedback_name"], text["readme_name"], text["button_save_name"] )
        break
print(text_file.hello_name)
# for j in file_json:

#     if file_json[j]["lang_name"] == lang_name:
#         #очистка поля от текста и вывод окна ошибки юзеру, с сообщением о просьбе к повторному вводу 
#         lang_name = input("Введите название языка повторно")
#         print("Name is changed")

# text_file_input = l.TextFile(text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12)

# for j in l.getJson(l.refFileJson):
#     if j == text_file.id:
#         text_file.changeId()
#         pass

# lan = l.createJson(text_file)

# l.addLang(lan,l.refFileJson)

# id, data = l.setLang("A6211702782", "2511719659", l.refFileJson)

# print(data.lang_name, data.hello_name)