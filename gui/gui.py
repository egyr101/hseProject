from tkinter import *
from tkinter import ttk
import ctypes
import lang.lang as l
import random
import logic.logic as lg
import sys
flag=0
title='Root Calculator'
root = Tk()
root.title(title)
root.geometry("1200x720")
root.resizable(False, True)
root.tk.call('tk', 'scaling', 2.5)
def json_error():
    error=Toplevel(root)
    error.title("Error")
    error.geometry("800x290")
    error.configure(bg='red')
    ttk.Label(error, text='Json error, please, reinstall the program',background='red', foreground='white', font=('Segoe UI', 16, 'bold')).place(relx=0.5, rely=0.5, anchor='center')

    root.mainloop()
    sys.exit()

check, text_file = l.primarySetLang(l.refFileJson)
if check == False:
    json_error()

ctypes.windll.shcore.SetProcessDpiAwareness(1)

def on_show_text():  #работа с введенными числами
    global FULLBG
    first_value = entry1.get()
    second_value = entry2.get()
    output_var.set(lg.answer(first_value, second_value))
    if output_var.get() == 'error':
        output_var.set(text_file.readme_name)
    entry1.delete(0, END)
    entry2.delete(0, END)
    frame_output.configure(background=FULLBG)
    output_label.configure(background=FULLBG)

def show_input_error():   #вызов окна ошибки
    err = Toplevel(root)
    err.title(error_text.get())
    err.geometry("800x290")
    err.configure(bg='red')
    ttk.Label(err, textvariable=error_text,background='red', foreground='white', font=('Segoe UI', 16, 'bold')).place(relx=0.5, rely=0.5, anchor='center')
    err.after(3000, err.destroy)

def show_choice_window(): #Окно с изменением языка
    
    win = Toplevel(root)
    win.title(command1.get())
    win.geometry("500x800")
    win.configure(bg=BG)

    def radiobuttonReturn(textFile,current_language_id,new_language_id):
        global menu
        print(text_file, current_language_id, new_language_id)
        check = l.setLang(textFile, current_language_id, new_language_id, l.refFileJson)
        if not(check):
            json_error()
        if check != "no change":
            text_file.setTextFile(new_language_id,text_file.createJson()[text_file.id])
            setText(text_file, menu)
        win.after(1000, win.destroy)
    check, data = l.getJson(l.refFileJson)
    if not(check):
        json_error()
    for d in data:
        check, t = l.getJson(l.refFileJson)
        if check == False:
            json_error()
        ttk.Radiobutton(win, text=t[d]["lang_name"], value=d, 
                       command=lambda id=d: radiobuttonReturn(text_file,text_file.id,id), 
                       style='Dark.TRadiobutton').pack(anchor='w', padx=22, pady=(22,11))


def show_newlanguages_window(): #Окно с добавлением языка 
    add_language = Toplevel(root)
    add_language.title(command2.get())
    add_language.geometry("1000x1000")
    add_language.configure(bg=BG)
    

    
    ttk.Label(add_language, textvariable=language_name, style='Dark.TLabel').place(x=30, y=30)
    e_language_name = ttk.Entry(add_language, style='Dark.TEntry')
    e_language_name.place(x=30, y=60, width=620, height=36)

    ttk.Label(add_language, textvariable=title_on_screen, style='Dark.TLabel').place(x=30, y=110)
    e_title_on_screen = ttk.Entry(add_language, style='Dark.TEntry')
    e_title_on_screen.place(x=30, y=140, width=620, height=36)

    ttk.Label(add_language, textvariable=input_num, style='Dark.TLabel').place(x=30, y=190)
    e_input_num = ttk.Entry(add_language, style='Dark.TEntry')
    e_input_num.place(x=30, y=220, width=620, height=36)

    ttk.Label(add_language, textvariable=input_dot, style='Dark.TLabel').place(x=30, y=270)
    e_input_dot = ttk.Entry(add_language, style='Dark.TEntry')
    e_input_dot.place(x=30, y=300, width=620, height=36)

    ttk.Label(add_language, textvariable=button_text, style='Dark.TLabel').place(x=30, y=350)
    e_button_text = ttk.Entry(add_language, style='Dark.TEntry')
    e_button_text.place(x=30, y=380, width=620, height=36)

    ttk.Label(add_language, textvariable=output_var, style='Dark.TLabel').place(x=30, y=430)
    e_output_var = ttk.Entry(add_language, style='Dark.TEntry')
    e_output_var.place(x=30, y=460, width=620, height=36)

    ttk.Label(add_language, textvariable=settings_text, style='Dark.TLabel').place(x=30, y=510)
    e_settings_text = ttk.Entry(add_language, style='Dark.TEntry')
    e_settings_text.place(x=30, y=540, width=620, height=36)

    ttk.Label(add_language, textvariable=error_text, style='Dark.TLabel').place(x=30, y=590)
    e_error_text = ttk.Entry(add_language, style='Dark.TEntry')
    e_error_text.place(x=30, y=620, width=620, height=36)

    ttk.Label(add_language, textvariable=command1, style='Dark.TLabel').place(x=30, y=670)
    e_command1 = ttk.Entry(add_language, style='Dark.TEntry')
    e_command1.place(x=30, y=700, width=620, height=36)

    ttk.Label(add_language, textvariable=command2, style='Dark.TLabel').place(x=30, y=750)
    e_command2 = ttk.Entry(add_language, style='Dark.TEntry')
    e_command2.place(x=30, y=780, width=620, height=36)

    ttk.Label(add_language,textvariable=command3, style='Dark.TLabel').place(x=30, y=830)
    e_command3 = ttk.Entry(add_language, style='Dark.TEntry')
    e_command3.place(x=30, y=860, width=620, height=36)

    ttk.Label(add_language,textvariable=save_text, style='Dark.TLabel').place(x=30, y=910)
    e_save_text = ttk.Entry(add_language, style='Dark.TEntry')
    e_save_text.place(x=30, y=940, width=620, height=36)


    def _save_new_language(): 
        language_name_input = e_language_name.get()
        title_on_screen_input = e_title_on_screen.get()
        input_num_input = e_input_num.get()
        input_dot_input = e_input_dot.get()
        button_text_input = e_button_text.get()
        output_var_input = e_output_var.get()
        settings_text_input = e_settings_text.get()
        error_text_input = e_error_text.get()
        command1_input = e_command1.get()
        command2_input = e_command2.get()
        command3_input = e_command3.get()
        save_text_input = e_save_text.get()
        if language_name_input == "" or title_on_screen_input == "" or input_num_input == "" or input_dot_input == "" or button_text_input == "" or output_var_input == "" or settings_text_input == "" or error_text_input == "" or command1_input == "" or command2_input == "" or command3_input == "" or save_text_input == "":
            show_input_error()
            return
        else:
            t = {str(random.randint(1000000000,9999999999)) : {
                "lang_name" : language_name_input,
                "hello_name" : title_on_screen_input, 
                "input_num_name" : input_num_input,
                "input_dot_name" : input_dot_input,
                "button_sqrt_name" : button_text_input,
                "output_res_name" : output_var_input,
                "settings_name" : settings_text_input,
                "change_lang_name" : command1_input, 
                "add_lang_name" : command2_input,
                "feedback_name" : command3_input,
                "readme_name" : error_text_input,
                "button_save_name" : save_text_input
            }}
            if not(l.addLang(t,l.refFileJson)):
                json_error()
            add_language.after(1000, add_language.destroy)
        
    save_btn = ttk.Button(add_language, textvariable=save_text, style='Dark.TButton', command=_save_new_language)
    save_btn.place(x=800, y=120, width=170, height=60)


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

def setText (text_file : l.TextFile, menu_obj: Menu):
    global flag
    language_name.set(text_file.lang_name)
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
    
    
    if flag:
        menu_obj.delete(0)
        menu_obj.delete(0)
        menu_obj.delete(0)

    flag=1
    menu_obj.add_command(label=text_file.change_lang_name, command=show_choice_window)
    menu_obj.add_command(label=text_file.add_lang_name, command=show_newlanguages_window)
    menu_obj.add_command(label=text_file.feedback_name)




#Все переменные для языка
language_name = StringVar()
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

#Стили для кода
BG = '#240046' #основной бэк
FG = '#e0aaff' #светлый для шрифта
BBG='#5a189a' #Чуть светлее бэка для заливки полей
FULLBG='#10002b' #самый темный
initStyles(BG,FG,BBG,FULLBG)


menu_button = ttk.Menubutton(root, textvariable=settings_text, style='Dark.TMenubutton')
menu_button.pack(anchor='ne')
menu = Menu(menu_button, tearoff=0, bg=BG, fg=FG, activebackground=BBG, activeforeground=FG, relief='flat', bd=0)
menu.configure(font=('Segoe UI', 16))
menu_button['menu'] = menu


setText(text_file, menu)




title_label = ttk.Label(root, textvariable=title_on_screen, style='Title.TLabel')
title_label.place(relx=0.15, y=100)

label1 = ttk.Label(root, textvariable=input_num, style='Dark.TLabel')
label1.place(x=30, y=220)
 
entry1 = ttk.Entry(root, style='Dark.TEntry')
entry1.place(x=30, y=260, width=680, height=50)

entry2 = ttk.Entry(root, style='Dark.TEntry')
entry2.place(x=730, y=260, width=430, height=50)

label2 = ttk.Label(root, textvariable=input_dot, style='Dark.TLabel')
label2.place(x=730, y=220)

button = ttk.Button(root, textvariable=button_text, command=on_show_text, style='Dark.TButton')
button.place(relx=0.5, y=360, anchor='center')

frame_output = Frame(root, highlightthickness=3, highlightbackground=FULLBG, background=BG)
frame_output.place(x=3, y=430, relwidth=1, width=-10)
output_label = ttk.Label(frame_output, textvariable=output_var, wraplength=1150, style='Dark.TLabel')
output_label.pack(fill='both', expand=True, padx=30)

root.mainloop()