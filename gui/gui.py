from tkinter import *
from tkinter import ttk

def on_show_text():
    if number.get() == "1234":   
        show_input_error()
        return
    
    output_var.set(number.get())
    second_value = accuracy.get()
    number.set("")
    accuracy.set("")

def show_input_error():
    err = Toplevel(root)
    err.title("Ошибка")
    err.geometry("360x160")
    err.resizable(False, False)
    err.configure(bg='red')
    Label(err, text="Ошибка ввода", bg='red', fg='white', font=('Segoe UI', 20, 'bold')).pack(expand=True, fill='both')
    err.after(2000, err.destroy)


def show_choice_window():
    global language
    win = Toplevel(root)
    win.title(command1)
    win.geometry("280x160")
    win.resizable(False, False)

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
        elif choice_var.get() == 2:  # Английский
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
    for n in doc:
            ttk.Radiobutton(win, text="Русский язык", variable=choice_var, value=1, command=language_select).pack(anchor='w', padx=12, pady=(12,6))

    ttk.Radiobutton(win, text="Русский язык", variable=choice_var, value=1, command=language_select).pack(anchor='w', padx=12, pady=(12,6))
    ttk.Radiobutton(win, text="Английский язык", variable=choice_var, value=2, command=language_select).pack(anchor='w', padx=12, pady=6)
    ttk.Radiobutton(win, text="Вариант 3", variable=choice_var, value=3, command=language_select).pack(anchor='w', padx=12, pady=6)


all_languages=[["Калькулятор корней","Добро пожаловать в калькулятор корней",'Настройки','Выбрать язык','Создать свой язык','Что то еще',"Здесь появится ваш ответ","Введите число, из которого нужно извлечь корень:","Укажите точность знаков после запятой:",'Вычислить корень'],
["Root Calculator","Welcome to the Root Calculator","Settings","Choose language","Create your language","Something else","Your answer will appear here","Enter the number to extract the root from:","Specify the number of decimal places:","Calculate root"]]

language=1
title=all_languages[0][0]
root = Tk()
root.title(title)
root.geometry("650x400")
root.resizable(False, False)
#icon = PhotoImage(file = "icon")
#root.iconphoto(False, icon)

style = ttk.Style()
style.configure('Title.TLabel', font=('Segoe UI', 16, 'bold'))

title_on_screen = StringVar(value=all_languages[0][1])

title_label = ttk.Label(root, textvariable=title_on_screen, style='Title.TLabel')
title_label.place(relx=0.15, y=40)

frame = ttk.Frame(borderwidth=4, relief=SOLID)
frame.place(relx=0.83, y=7)
settings_text=StringVar(value=all_languages[0][2])
menu_button = ttk.Menubutton(frame, textvariable=settings_text)
menu_button.pack()
menu = Menu(menu_button, tearoff=0)
menu_button['menu'] = menu


command1=all_languages[0][3]
command2=all_languages[0][4]
command3=all_languages[0][5]


menu.add_command(label=command1, command=show_choice_window)
menu.add_command(label=command2)
menu.add_command(label=command3)


number = StringVar()
output_var = StringVar(value=all_languages[0][6])  
accuracy = StringVar()  

pole_text1=StringVar(value=all_languages[0][7])
label1 = ttk.Label(root, textvariable=pole_text1)
label1.place(x=16, y=100)

entry1 = ttk.Entry(root, textvariable=number)
entry1.place(x=16, y=124, width=380, height=25)

entry2 = ttk.Entry(root, textvariable=accuracy)
entry2.place(x=404, y=124, width=180, height=25)

pole_text2=StringVar(value=all_languages[0][8])
label2 = ttk.Label(root, textvariable=pole_text2)
label2.place(x=404, y=100)

button_text=StringVar(value=all_languages[0][9])
button = ttk.Button(root, textvariable=button_text, command=on_show_text)
button.place(relx=0.5, y=200, anchor='center')


output_label = ttk.Label(root, textvariable=output_var, wraplength=560)
output_label.place(x=16, y=240, width=568)


root.mainloop()