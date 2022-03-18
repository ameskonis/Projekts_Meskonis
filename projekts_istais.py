from tkinter import *
import base64


def encrypt1():
    text1 = text.get()
    keyy = key.get()
    result = ""
    for i in range(len(text1)):
        char = text1[i]
        result += chr(ord(char) + int(keyy))
    label4 = Label(window, text="Teksts tika nokopēts", font='arial', bg="ghost white")
    label4.place(x=35, y=170)
    window.clipboard_clear()
    window.clipboard_append(base64.urlsafe_b64encode("".join(result).encode()).decode())
    window.update()
    label4.after(1000, label4.destroy)


def clear_text():
    text.delete(0, 'end')


def clear_key():
    key.delete(0, 'end')


def decrypt1():
    text1 = text.get()
    text2 = base64.urlsafe_b64decode(text1).decode()
    key2 = key.get()
    result = ""
    for i in range(len(text2)):
        char = text2[i]
        result += chr(ord(char) - int(key2))
    label4 = Label(window, text=result, font='arial', bg="ghost white", wraplength=340)
    label4.place(x=35, y=170)
    label4.after(10000, label4.destroy)


window = Tk()
window.geometry("420x260")
window.resizable(0, 0)
window.configure(bg="ghost white")
window.title("teksta šifrētājs/atšifrētājs")
Label(window, text=" ", font='arial 10 bold', bg="ghost white").pack()
Label(window, text="Ievadi tekstu, kuru vēlies šifrēt/atšifrēt", font='arial 10 bold', bg="ghost white").pack()
text = Entry(window, font='arial 10', bg="ghost white")
text.pack()
Label(window, text=" ", font='arial 10 bold', bg="ghost white").pack()
Label(window, font='arial 10 bold', text='Ievadi šifra atslēgu (skaitļos)', bg="ghost white").pack()
key = Entry(window, font='arial 10', bg="ghost white")
key.pack()

Button(window, text="šifrēt", command=encrypt1, bg="ghost white").place(x=155, y=135)
Button(window, text="atšifrēt", command=decrypt1, bg="ghost white").place(x=215, y=135)
Button(window, text=" izdzēst ", command=clear_text, bg="ghost white").place(x=300, y=42)
Button(window, text=" izdzēst ", command=clear_key, bg="ghost white").place(x=300, y=104)
window.mainloop()
