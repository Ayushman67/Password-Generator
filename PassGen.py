from tkinter import *
import random2, string
import pyperclip

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")

Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(root, text ='Ayushmans Project', font ='arial 15 bold').pack(side = BOTTOM)

pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = pass_len , width = 15).pack()

pass_str = StringVar()
def Generator():
    password = ''
    for x in range (0,4):
        password = random2.choice(string.ascii_uppercase) + random2.choice(string.ascii_lowercase) + random2.choice(string.digits) + random2.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password + random2.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)
Entry(root , textvariable = pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())
Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)
