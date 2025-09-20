#гугл форма
import lang.lang as l

text1,text2,text3 = "aaasdaaрфыврфsd","dsssfdsfs","aaasdыфовфрaasd"
text4,text5,text6 = "aaasdaaрфыврфsd","dsssfdsfs","aaasdыфовфрaasd"
text7,text8,text9 = "aaasdaaрфыврфsd","dsssfdsfs","aaasdыфовфрaasd"
text10,text11,text12 = "aaasdaaрфыврфsd","dsssfdsfs","aaasdыфовфрaasd"

lang_name = input("Input name language")

data = l.getJson(l.refFileJson)

text_file = l.primarySetLang(l.refFileJson)
text_file_input = None



print(text_file.hello_name)

for j in data:

    if data[j]["lang_name"] == lang_name:
        while data[j]["lang_name"] == lang_name:
        #очистка поля от текста и вывод окна ошибки юзеру, с сообщением о просьбе к повторному вводу 
            lang_name = input("Язык с таким названием уже существует! Введите название языка: ")

text_file_input = l.TextFile(lang_name, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12)

text_file_input.validationId(data, l.refFileJson)

l.addLang(text_file_input.createJson(),l.refFileJson)

# id, data = l.setLang("A6211702782", "2511719659", l.refFileJson)

# print(data.lang_name, data.hello_name)