#гугл форма
import lang.lang as l

lang_name = "english"
text1,text2,text3 = "aaasdaasd","aaasdaasd","aaasdaasd"

file_json = l.getJson(l.refFileJson)

for j in file_json:
    if file_json[j]["lang_name"] == lang_name:
        #очистка поля от текста и вывод окна ошибки юзеру, с сообщением о просьбе к повторному вводу 
        lang_name = input("Введите название языка повторно")
        print("Name is changed")

text_file = l.TextFile(lang_name, text1, text2, text3)

for j in l.getJson(l.refFileJson):
    if j == text_file.id:
        text_file.changeId()
        pass

lan = l.createJson(text_file)

l.addLang(lan,l.refFileJson)

data = l.setLang(text_file.id, l.refFileJson)

# lang = input("Введите язык: ")

# data = l.setLang(lang,l.refFileJson)

print(data.lang_name, data.text1)