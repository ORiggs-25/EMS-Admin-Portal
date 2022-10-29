from tkinter import *
import tkinter as tk
import tk as tk
from PIL import ImageTk
from tkcalendar import * #for calender view
from tkinter import colorchooser

root = Tk()
# renames the title of the window
root.title('Calender_Admin_View')
# sets the dimensions of the window to measurement
root.geometry('1200x800')
# prevents user to resize the window
root.resizable(width=False, height=False)



'''
# using pillow's ImageTk class and PhotoImage function to display background photo
# canvas function will create a background for the GUI
my_canvas = tk.Canvas(root, width=1200, height=800, bd=0, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# using pillow's ImageTk class and PhotoImage function to display background photo
bg = ImageTk.PhotoImage(file="addEmployee1.jpg")
my_canvas.create_image(0, 0, image=bg, anchor="nw")
'''

cal = Calendar(root, selectmode="day", year=2022)
cal.pack(pady=20, fill="both", expand=True)

# function to view event in the date, in this case we want to view the list of the employees that work that date
def grab_date():
    my_label.config(text=cal.get_date())

my_button = Button(root, text='View Schedule', command=grab_date)
my_button.pack(pady=20)


#the label that we want to output the date
my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()

