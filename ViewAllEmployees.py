import requests
import json

import tkinter as tk  # GUI module
from PIL import ImageTk  # Display background
import tkinter.font as font


def viewAllEmployees():
    # Will Display all the employees in the database in terminal

    headers = {
        "Content-Type": "application/json",
        "Connection": "keep-alive",
    }

    try:
        request = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employees")
        employeesFromResponse = request.json()["Items"]
        employees = []
        for emp in employeesFromResponse:
            print(emp)
    except requests.exceptions.HTTPError as err:
        print(err)


def main():
    # -----following code pertains to main user input
    # window--------------------------------------------------------------- creating object from Tkinter module
    root = tk.Tk()
    # renames the title of the window
    root.title("Admin Portal")
    # sets the dimensions of the window to measurement
    root.geometry('1200x800')
    # prevents user to resize the window
    root.resizable(width=False, height=False)

    # canvas function will create a background for the GUI
    my_canvas = tk.Canvas(root, width=800, height=400, bd=0, highlightthickness=0)
    my_canvas.pack(fill="both", expand=True)

    # using pillow's ImageTk class and PhotoImage function to display background photo
    bg = ImageTk.PhotoImage(file="addEmployee1.jpg")
    my_canvas.create_image(0, 0, image=bg, anchor="nw")

    # create_text function from tkinter will display text onto GUI
    my_canvas.create_text(600, 140, text="View All Employees?", font=("Helvetica", 40), fill="white")

    # We used the Button function in Tkinter which will call the function once clicked
    create_button = tk.Button(root, text="View", activeforeground='white', font=("Helvetica", 30),
                              width=15, height=20, borderwidth=2, command=lambda: viewAllEmployees())

    create_button_window = my_canvas.create_window(450, 200, height=35, anchor="nw", window=create_button)

    root.mainloop()


if __name__ == '__main__':
    main()

"""
    
"""
