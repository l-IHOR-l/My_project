from tkinter import *
import random

def show_custom_dialog():
    dialog = Toplevel()
    dialog.title('Ответ')
    dialog.geometry('1000x300')
    dialog.resizable(width=False, height=False)

    label = Label(dialog, text='Да, ти даун!', font='Arial 100 bold')
    label.pack(pady=10)

    button = Button(dialog, text='Закрыть', command=lambda: [root.quit(), dialog.destroy()])
    button.pack(pady=5)

    # автоматическое закрытие окна
    dialog.after(10000, lambda: [root.quit(), dialog.destroy()])

def Yes():
    show_custom_dialog()


def motionMouse(event):
    btnNo.place(x=random.randint(0, 300), y=random.randint(0, 300))

root=Tk()
root.geometry('400x400')
root.title('Опрос')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text='Ты даун?', font='Arial 20 bold', bg='white')
label.pack()

btnYes = Button(root, text='Да', font='Arial 20 bold', command=Yes)
btnYes.place(x=160, y=100)

btnNo = Button(root, text='Нет', font='Arial 20 bold')
btnNo.place(x=250, y=100)
btnNo.bind('<Enter>', motionMouse)

root.mainloop()
