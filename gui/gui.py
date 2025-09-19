from tkinter import *
from tkinter import ttk
import ctypes
 
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
    err.title("Ошибка")
    err.geometry("650x290")
    err.resizable(False, False)
    err.configure(bg='red')
    Label(err, text="Ошибка ввода", bg='red', fg='white', font=('Segoe UI', 20, 'bold')).pack(expand=True, fill='both')
    err.after(2000, err.destroy)


def show_choice_window(): #Окно с изменением языка
    global language
    win = Toplevel(root)
    win.title(command1)
    win.geometry("500x290")
    try:
        win.configure(bg=BG)
    except Exception:
        pass


    choice_var = IntVar(value=language)

    def language_select():
        global title,language
        if choice_var.get() == 1:
            title = all_languages[1][0]
            root.title(title)
            title_on_screen.set(all_languages[0][1])
            settings_text.set(all_languages[0][2])
            menu.entryconfig(0, label=all_languages[0][3])
            menu.entryconfig(1, label=all_languages[0][4])
            menu.entryconfig(2, label=all_languages[0][5])
            output_var.set(all_languages[0][6])
            pole_text1.set(all_languages[0][7])
            pole_text2.set(all_languages[0][8])
            button_text.set(all_languages[0][9])
            language=1
        elif choice_var.get() == 2: 
            title = all_languages[1][0]
            root.title(title)
            title_on_screen.set(all_languages[1][1])
            settings_text.set(all_languages[1][2])
            menu.entryconfig(0, label=all_languages[1][3])
            menu.entryconfig(1, label=all_languages[1][4])
            menu.entryconfig(2, label=all_languages[1][5])
            output_var.set(all_languages[1][6])
            pole_text1.set(all_languages[1][7])
            pole_text2.set(all_languages[1][8])
            button_text.set(all_languages[1][9])
            language=2
        win.after(1000, win.destroy)

    ttk.Radiobutton(win, text="Русский язык", variable=choice_var, value=1, command=language_select, style='Dark.TRadiobutton').pack(anchor='w', padx=22, pady=(22,11))
    ttk.Radiobutton(win, text="Английский язык", variable=choice_var, value=2, command=language_select, style='Dark.TRadiobutton').pack(anchor='w', padx=22, pady=11)
    ttk.Radiobutton(win, text="Вариант 3", variable=choice_var, value=3, command=language_select, style='Dark.TRadiobutton').pack(anchor='w', padx=22, pady=11)

def show_newlanguages_window(): #Окно с добавлением языка
    add_language = Toplevel(root)
    add_language.title(command2)
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
        

    save_btn = ttk.Button(add_language, text="Сохранить", style='Dark.TButton', command=_save_new_language)
    save_btn.place(x=500, y=120, width=170, height=60)


all_languages=[["Калькулятор корней","Добро пожаловать в калькулятор корней",'Настройки','Выбрать язык','Создать свой язык','Что то еще',"Здесь появится ваш ответ","Введите число, из которого нужно извлечь корень:","Укажите точность знаков после запятой:",'Вычислить корень'],
["Root Calculator","Welcome to the Root Calculator","Settings","Choose language"," Create your language","Something else","Your answer will appear here","Enter the number to extract the root from:","Specify the number of decimal places:","Calculate root"]]

language=1
title=all_languages[0][0]
root = Tk()
root.title(title)
root.geometry("1200x720")
icon = PhotoImage(file ="C:/Users/Sokol/Desktop/pROOOOD/hseProject/gui/icon.png")
root.iconphoto(False, icon)
root.tk.call('tk', 'scaling', 2.5)

#Стили для кода
style = ttk.Style()
style.theme_use('clam')
BG = '#240046' #основной бэк
FG = '#e0aaff' #светлый для шрифта
BBG='#5a189a' #Чуть светлее бэка для заливки полей
FULLBG='#10002b' #самый темный
root.configure(bg=BG)
style.configure('Title.TLabel', font=('Segoe UI', 16, 'bold'), background=BG, foreground=FG)
style.configure('Dark.TFrame', background=BG)
style.configure('Dark.TLabel', background=BG, foreground=FG)
style.configure('Dark.TButton', background=BBG,foreground=FG, bordercolor=FULLBG, focuscolor=FULLBG, lightcolor=FULLBG, darkcolor=FULLBG, highlightcolor=FULLBG)
style.configure('Dark.TEntry', fieldbackground=BBG, foreground=FG, background=BG,bordercolor=FULLBG, focuscolor=FULLBG, lightcolor=FULLBG, darkcolor=FULLBG, highlightcolor=FULLBG)
style.configure('Dark.TMenubutton', background=BBG, foreground=FG,bordercolor=FULLBG, focuscolor=FULLBG, lightcolor=FULLBG, darkcolor=FULLBG, highlightcolor=FULLBG)
style.configure('Dark.TRadiobutton', background=BG, foreground=FG)
title_on_screen = StringVar(value=all_languages[0][1])
title_label = ttk.Label(root, textvariable=title_on_screen, style='Title.TLabel')
title_label.place(relx=0.15, y=100)

#Настройки
frame = Frame(root, highlightthickness=2, highlightbackground=FULLBG, bg=BG)
frame.place(relx=0.83, y=13)
settings_text=StringVar(value=all_languages[0][2])
menu_button = ttk.Menubutton(frame, textvariable=settings_text, style='Dark.TMenubutton')
menu_button.pack()
menu = Menu(menu_button, tearoff=0, bg=BG, fg=FG, activebackground='#2a0a62', activeforeground=FG)
menu.configure(font=('Segoe UI', 16))
menu_button['menu'] = menu

command1=all_languages[0][3]
command2=all_languages[0][4]
command3=all_languages[0][5]

menu_icon_plus = PhotoImage(file = 'C:/Users/Sokol/Desktop/pROOOOD/hseProject/gui/Plus.png').subsample(8, 8)
menu_icon_alpha = PhotoImage(file = 'C:/Users/Sokol/Desktop/pROOOOD/hseProject/gui/Alphabet.png').subsample(8, 8)
menu_icon_question = PhotoImage(file = 'C:/Users/Sokol/Desktop/pROOOOD/hseProject/gui/Question.png').subsample(25,25 )

menu.add_command(label=command1, command=show_choice_window, image=menu_icon_alpha, compound='right')
menu.add_command(label=command2, command=show_newlanguages_window, image=menu_icon_plus, compound='right')
menu.add_command(label=command3, image=menu_icon_question, compound='right')

#Для нового языка
new_vFirst = ""
new_vSecond = ""
new_vThird = ""
new_vFourth = ""




#Кнопки взаимодействия на основном экране
number = StringVar()
output_var = StringVar(value=all_languages[0][6])  
accuracy = StringVar()  

pole_text1=StringVar(value=all_languages[0][7])
label1 = ttk.Label(root, textvariable=pole_text1, style='Dark.TLabel')
label1.place(x=30, y=220)

entry1 = ttk.Entry(root, textvariable=number, style='Dark.TEntry')
entry1.place(x=30, y=260, width=680, height=50)

entry2 = ttk.Entry(root, textvariable=accuracy, style='Dark.TEntry')
entry2.place(x=730, y=260, width=430, height=50)

pole_text2=StringVar(value=all_languages[0][8])
label2 = ttk.Label(root, textvariable=pole_text2, style='Dark.TLabel')
label2.place(x=730, y=220)

button_text=StringVar(value=all_languages[0][9])
button = ttk.Button(root, textvariable=button_text, command=on_show_text, style='Dark.TButton')
button.place(relx=0.5, y=360, anchor='center')


frame_output = Frame(root, highlightthickness=3, highlightbackground=FULLBG, background=BG)
frame_output.place(x=3, y=430, relwidth=1, width=-10)
output_label = ttk.Label(frame_output, textvariable=output_var, wraplength=1000, style='Dark.TLabel')
output_label.pack(fill='both', expand=True, padx=30)



root.mainloop()