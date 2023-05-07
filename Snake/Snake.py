from tkinter import *

root = Tk()

root.title('PythomicWay Snake')

root.mainloop()

width = 800
height = 600
seg_size = 20
in_game = True

c = Canvas(root, width=width, height=height, bg = '#003300')


c.grid()
c.focus_set()

