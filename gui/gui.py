from tkinter import *
from tkinter import ttk
import ctypes
import lang.lang as l

data = l.getJson(l.refFileJson)
text_file = l.primarySetLang(l.refFileJson)

ctypes.windll.shcore.SetProcessDpiAwareness(1)

def on_show_text():  #работа с введенными числами
    if number.get() == "1234":   
        show_input_error()
        return
    output_var.set(number.get())
    second_value = accuracy.get()
    number.set("")
    accuracy.set("")
    frame_output.configure(background=FULLBG)
    output_label.configure(background=FULLBG)

def show_input_error():   #вызов окна ошибки
    err = Toplevel(root)
    err.title(error_text)
    err.geometry("650x290")
    err.resizable(False, False)
    err.configure(bg='red')
    ttk.Label(err, textvariable=error_text, bg='red', fg='white', font=('Segoe UI', 20, 'bold')).pack(expand=True, fill='both')
    err.after(2000, err.destroy)

def show_choice_window(): #Окно с изменением языка
    
    win = Toplevel(root)
    win.title(command1.get())
    win.geometry("500x290")
    win.configure(bg=BG)

    def radiobuttonReturn(textFile,current_language_id,new_language_id):
        l.setLang(textFile, current_language_id, new_language_id, l.refFileJson)
        text_file.setTextFile(new_language_id,text_file.createJson()[text_file.id])
        setText(text_file)
        win.after(1000, win.destroy)

    for d in data:
        ttk.Radiobutton(win, text=data[d]["lang_name"], value=d, 
                       command=lambda id=d: radiobuttonReturn(text_file,text_file.id,id), 
                       style='Dark.TRadiobutton').pack(anchor='w', padx=22, pady=(22,11))


def show_newlanguages_window(): #Окно с добавлением языка 
    add_language = Toplevel(root)
    add_language.title(command2.get())
    add_language.geometry("720x450")
    add_language.configure(bg=BG)
    
    # Поля ввода для нового языка
    vFirst = StringVar()
    vSecond = StringVar()
    vThird = StringVar()
    vFourth = StringVar()
    
    ttk.Label(add_language, text="Название языка", style='Dark.TLabel').place(x=30, y=30)
    e_title = ttk.Entry(add_language, textvariable=vFirst, style='Dark.TEntry')
    e_title.place(x=30, y=60, width=420, height=36)

    ttk.Label(add_language, text="Текст приветствия", style='Dark.TLabel').place(x=30, y=110)
    e_welcome = ttk.Entry(add_language, textvariable=vSecond, style='Dark.TEntry')
    e_welcome.place(x=30, y=140, width=420, height=36)

    ttk.Label(add_language, text="Подпись настроек", style='Dark.TLabel').place(x=30, y=190)
    e_settings = ttk.Entry(add_language, textvariable=vThird, style='Dark.TEntry')
    e_settings.place(x=30, y=220, width=420, height=36)

    ttk.Label(add_language, text="Текст кнопки", style='Dark.TLabel').place(x=30, y=270)
    e_button = ttk.Entry(add_language, textvariable=vFourth, style='Dark.TEntry')
    e_button.place(x=30, y=300, width=420, height=36)

    def _save_new_language(): 
        global new_vFirst, new_vSecond, new_vThird, new_vFourth
        new_vFirst = vFirst.get()
        new_vSecond = vSecond.get()
        new_vThird = vThird.get()
        new_vFourth = vFourth.get()
        
        add_language.destroy()
        
    save_btn = ttk.Button(add_language, textvariable=save_text, style='Dark.TButton', command=_save_new_language)
    save_btn.place(x=500, y=120, width=170, height=60)


def initStyles(BG,FG,BBG,FULLBG):
    style = ttk.Style()
    style.theme_use('clam')
    root.configure(bg=BG)
    style.configure('Title.TLabel', font=('Segoe UI', 16, 'bold'), background=BG, foreground=FG)
    style.configure('Dark.TFrame', background=BG)
    style.configure('Dark.TLabel', background=BG, foreground=FG)
    style.configure('Dark.TButton', background=BBG, foreground=FG, bordercolor=FULLBG, focuscolor=FULLBG, lightcolor=FULLBG, darkcolor=FULLBG, highlightcolor=FULLBG)
    style.map('Dark.TButton', background=[('active', FULLBG), ('pressed', FULLBG)])
    style.configure('Dark.TEntry', fieldbackground=BBG, foreground=FG, background=BG,bordercolor=FULLBG, focuscolor=FULLBG, lightcolor=FULLBG, darkcolor=FULLBG, highlightcolor=FULLBG)
    style.configure('Dark.TMenubutton', background=BBG, foreground=FG,bordercolor=FULLBG, focuscolor=FULLBG, lightcolor=FULLBG, darkcolor=FULLBG, highlightcolor=FULLBG)
    style.map('Dark.TMenubutton', background=[('active', FULLBG), ('pressed', FULLBG)])
    style.configure('Dark.TRadiobutton', background=BG, foreground=FG)
    style.map('Dark.TRadiobutton', background=[('active', FULLBG), ('pressed', FULLBG)])

def setText (text_file : l.TextFile):
    title_on_screen.set(text_file.hello_name)
    settings_text.set(text_file.settings_name)
    output_var.set(text_file.output_res_name)
    input_num.set(text_file.input_num_name)
    input_dot.set(text_file.input_dot_name)
    button_text.set(text_file.button_sqrt_name)
    save_text.set(text_file.button_save_name)
    error_text.set(text_file.readme_name)
    command1.set(text_file.change_lang_name)
    command2.set(text_file.add_lang_name)
    command3.set(text_file.feedback_name)


title='Root Calculator'
root = Tk()
#Все переменные для языка
title_on_screen = StringVar()
settings_text = StringVar()
output_var = StringVar()
input_num = StringVar()
input_dot = StringVar()
button_text = StringVar()
save_text = StringVar()
error_text = StringVar()
number = StringVar()
accuracy = StringVar() 
command1=StringVar() 
command2=StringVar() 
command3=StringVar() 

setText(text_file)

root.title(title)
root.geometry("1200x720")
root.tk.call('tk', 'scaling', 2.5)

#Стили для кода
BG = '#240046' #основной бэк
FG = '#e0aaff' #светлый для шрифта
BBG='#5a189a' #Чуть светлее бэка для заливки полей
FULLBG='#10002b' #самый темный
initStyles(BG,FG,BBG,FULLBG)



title_label = ttk.Label(root, textvariable=title_on_screen, style='Title.TLabel')
title_label.place(relx=0.15, y=100)



#Настройки
frame = Frame(root, highlightthickness=2, highlightbackground=FULLBG, bg=BG)
frame.place(relx=0.83, y=13)

menu_button = ttk.Menubutton(frame, textvariable=settings_text, style='Dark.TMenubutton')
menu_button.pack()
menu = Menu(menu_button, tearoff=0, bg=BG, fg=FG, activebackground=BBG, activeforeground=FG)
menu.configure(font=('Segoe UI', 16))
menu_button['menu'] = menu



menu.add_command(label=command1.get(), command=show_choice_window)
menu.add_command(label=command2.get(), command=show_newlanguages_window)
menu.add_command(label=command3.get())

#Для нового языка
new_vFirst = ""
new_vSecond = ""
new_vThird = ""
new_vFourth = ""

#Кнопки взаимодействия на основном экране


 


label1 = ttk.Label(root, textvariable=input_num, style='Dark.TLabel')
label1.place(x=30, y=220)

number = StringVar()
accuracy = StringVar()
 
entry1 = ttk.Entry(root, textvariable=number, style='Dark.TEntry')
entry1.place(x=30, y=260, width=680, height=50)

entry2 = ttk.Entry(root, textvariable=accuracy, style='Dark.TEntry')
entry2.place(x=730, y=260, width=430, height=50)


label2 = ttk.Label(root, textvariable=input_dot, style='Dark.TLabel')
label2.place(x=730, y=220)



button = ttk.Button(root, textvariable=button_text, command=on_show_text, style='Dark.TButton')
button.place(relx=0.5, y=360, anchor='center')

frame_output = Frame(root, highlightthickness=3, highlightbackground=FULLBG, background=BG)
frame_output.place(x=3, y=430, relwidth=1, width=-10)
output_label = ttk.Label(frame_output, textvariable=output_var, wraplength=1000, style='Dark.TLabel')
output_label.pack(fill='both', expand=True, padx=30)

root.mainloop()