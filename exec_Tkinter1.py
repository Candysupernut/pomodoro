import tkinter as tk
from tkinter import messagebox
import colorama
import pygame as pg
import sys

WHITE = (255, 255, 255)
DarkRed = (139, 0, 0)
Red = (255, 0, 0)
DarkOrange = (255, 140, 0)
Yellow = (255, 255, 0)
Lime = (0, 255, 0)
Green = (0, 128, 0)
Aqua = (127, 255, 212)
Pink = (255, 105, 180)
Navy = (0, 0, 128)
Indigo = (75, 0, 130)
Purple = (128, 0, 128)
DarkViolet=(238, 130, 238)

def read_text():
    content = text_entry.get("1.0", tk.END)
    root.after(1000, lambda: execute_code(content))

def execute_code(code):
    try:
        print('>>>')
        print('  ',end = '')
        exec(code)
    except Exception as e:
        print(colorama.Fore.RED + f"    ERROR :  {e}" + colorama.Style.RESET_ALL)
def ex():
   exit()
  
a='''
    -------------------------------------------------------------------
        eval і exec - це вбудовані функції в мові програмування Python,
    які дозволяють виконувати довільний код в рядковому вигляді.
    Однак ці функції мають різні призначення та використання.
    -------------------------------------------------------------------

        Функція eval використовується для вирахування виразів Python,
    які представлені у вигляді рядка.
                    ---------------------------------------------
                            Приклади
                    ---------------------------------------------
                    result = eval("2 + 3")
                    print(result)  # Виведе: 5
                    ---------------------------------------------
                    numbers = [10, 20, 30, 40, 50]
                    expression = f"sum({numbers}) / len({numbers})"
                    result = eval(expression)
                    print(result)  # Виведе: 30.0
                    ---------------------------------------------
        Плюси:
            Використовується для обчислення виразів у рядковому вигляді.
            Зручно використовувати для обчислень, якщо вхідні дані
            безпечні та контрольовані.
        
        Мінуси:
            Може бути небезпечним, якщо вхідні дані не перевірені,
            оскільки вона може виконати будь-який код.
    ----------------------------------------------------------------------

        Функція exec використовується для виконання фрагментів коду Python,
    представлених у вигляді рядка.
                        --------------------------
                                Приклади
                        --------------------------
                        code =
                        for i in range(5):
                        print(i)
                            
                        exec(code)
                        -------------------------
                        code = 
                        def add_numbers(a, b):
                            return a + b

                        result = add_numbers(3, 5)
                        print(result)
                        
                        exec(code)
                        -------------------------
        Плюси:
            Використовується для виконання довільного коду у вигляді рядка.
            Має широкі можливості для динамічного створення та виконання коду.
            
        Мінуси:
            Потенційно небезпечний, особливо якщо вхідні дані неперевірені,
            оскільки може виконати будь-який код.) '''
def info():
    global a
    root2=tk.Tk()
    root2.geometry('850x500+200+5')
    text2 = tk.Text(root2,height=100,width=100,bg='pink',font='Arial 18 ')
    text2.insert(tk.END,a)
    text2.place(x=1, y=1)
    scrollbar = tk.Scrollbar(root2, command=text2.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    # Приєднання скролбара до текстового поля
    text2.config(yscrollcommand=scrollbar.set)

def new_root (): 
        root.destroy()
def savefile():
    file_name = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()
    
def openn():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()
    
def colorDarkRED():
    text_entry.config(fg='DarkRed')
def colorRED():
    text_entry.config(fg='Red')
def colorDarkOrange():
    text_entry.config(fg='DarkOrange')
def colorRED():
    text_entry.config(fg='DarkRed')
    
def colorYellow():
    text_entry.config(fg='Yellow')
def colorLime():
    text_entry.config(fg='Lime')
def colorGreen():
    text_entry.config(fg='Green')
def colorAqua():
    text_entry.config(fg='Aqua')
def colorNavy():
    text_entry.config(fg='Navy')
def colorIndigo():
    text_entry.config(fg='Indigo')
def colorPurple():
    text_entry.config(fg='Purple')
def colorDarkViolet():
    text_entry.config(fg='DarkViolet')
    
def change():
    lab1.config( image=photo2)
    
root = tk.Tk()
root.title("EXEC")
root.geometry('850x500+200+5')

photo1=tk.PhotoImage(width=900,height=600,file='n.png')
photo2=tk.PhotoImage(width=900,height=600,file='d.png')
lab1 = tk.Label(root,height=500, image=photo1, width=850,fg='black',font='Arial 18 ')
lab1.place(x=1, y=1)

text_entry = tk.Text(root, height=20, width=70)
text_entry.place(x=30, y=30)


button = tk.Button(root, text="eval()",width=10, command=read_text)
button.place(x=660,y=40)
button1 = tk.Button(root, text="exec()", width=10, command=read_text)
button1.place(x=660,y=100)
button2 = tk.Button(root, text=" info ", width=10,command=info)
button2.place(x=660,y=160)
button3 = tk.Button(root, text=" exit ",  width=10,command=ex)
button3.place(x=660, y=210)


buttonsa = tk.Button(root, text=" save ",  width=10,command=savefile)
buttonsa.place(x=660, y=270)
buttonop = tk.Button(root, text=" open",  width=10,command=openn)
buttonop.place(x=660, y=330)

buttonop = tk.Button(root, text=" change theme",  width=10,command=change)
buttonop.place(x=660, y=430)

buttonDarkRED = tk.Button(root, width=5,bg='DarkRed', command=colorDarkRED)
buttonDarkRED.place(x=50,y=5)
buttonRed = tk.Button(root,bg='Red',width=5, command=colorRED)
buttonRed.place(x=100,y=5)
buttonDarkOrange = tk.Button(root,bg='DarkOrange',width=5, command=colorDarkOrange)
buttonDarkOrange.place(x=150,y=5)
buttonYellow = tk.Button(root,bg='Yellow',width=5, command=colorYellow)
buttonYellow.place(x=200,y=5)
buttonLime = tk.Button(root,bg='Lime',width=5, command=colorLime)
buttonLime.place(x=250,y=5)
buttonGreen = tk.Button(root,bg='Green',width=5, command=colorGreen)
buttonGreen.place(x=300,y=5)
buttonAqua = tk.Button(root,bg='Aqua',width=5, command=colorAqua)
buttonAqua.place(x=350,y=5)
buttonNavy = tk.Button(root,bg='Navy',width=5, command=colorNavy)
buttonNavy.place(x=400,y=5)
buttonIndigo = tk.Button(root,bg='Indigo',width=5, command=colorIndigo)
buttonIndigo.place(x=500,y=5)
buttonPurple = tk.Button(root,bg='Purple',width=5, command=colorPurple)
buttonPurple.place(x=550,y=5)
buttonDarkViolet = tk.Button(root,bg='DarkViolet',width=5, command=colorDarkViolet)
buttonDarkViolet.place(x=450,y=5)


root.mainloop()
