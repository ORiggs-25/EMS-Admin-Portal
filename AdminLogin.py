import tkinter as tk  # GUI module
from tkinter import Canvas

from PIL import ImageTk  # Display background
import tkinter.font as font  # for bold font


def main():

#------ get functions will call get user's input, creates a new object------------------------------------------------
    def getUserName(user_ID):
       user_ID = entry_ID.get()

    def getPassword(user_password):
       user_password = entry_password.get()
# --------------------------------------------------------------------------------------------------------------------


#-----following code pertains to main user input window---------------------------------------------------------------
    # creating object from Tkinter module
    root = tk.Tk()
    # renames the title of the window
    root.title("Login Page")
    # sets the dimensions of the window to measurement
    root.geometry('1200x800')
    # prevents user to resize the window
    root.resizable(width=False, height=False)

   # canvas function will create a background for the GUI
    my_canvas: Canvas = tk.Canvas(root, width=1200, height=800, bd=0, highlightthickness=0)
    my_canvas.pack(fill="both", expand=True)

   # using pillow's ImageTk class and PhotoImage function to display background photo
    bg = ImageTk.PhotoImage(file="background.png")
    my_canvas.create_image(0, 0, image=bg, anchor="nw")

    # create_text function from tkinter will display text onto GUI
    my_canvas.create_text(600, 175, text="Employee Management System Admin Portal", font=("Helvetica", 18), fill="white")
    my_canvas.create_text(300, 290, text="User ID", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 340, text="Password", font=("Helvetica", 16), fill="white")

    # create Entry text boxes
    entry_ID = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    entry_password = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)

    entry_ID_window = my_canvas.create_window(375, 275, anchor="nw", window=entry_ID)
    entry_password_window = my_canvas.create_window(375, 325, anchor="nw", window=entry_password)


    # We used the Button function in Tkinter which will call the function once clicked
    create_button = tk.Button(root, text="Log in", activeforeground='white', font=("Helvetica", 15), \
                              width=15, height=20, borderwidth=2, command=lambda: getPassword(entry_password))

    create_button_window = my_canvas.create_window(500, 400, height=35, anchor="nw", window=create_button)

    root.mainloop()

if __name__ == '__main__':
    main()
