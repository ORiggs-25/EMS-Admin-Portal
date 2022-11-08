import tkinter
from tkinter.constants import LEFT
from tkinter.ttk import Label

import requests
import json

import tkinter as tk  # GUI module
from PIL import ImageTk  # Display background
import tkinter.font as font


def viewAllEmployees():
    global lastN, birthday, status, address, id, email, phone, firstN, roleId
    headers = {
        "Content-Type": "application/json",
        "Connection": "keep-alive",
    }

    try:

        root = tk.Tk()
        # renames the title of the window
        root.title("Admin Portal")
        # sets the dimensions of the window to measurement
        root.geometry('1200x800')
        # prevents user to resize the window
        root.resizable(width=False, height=False)

        # canvas function will create a background for the GUI
        my_canvas = tk.Canvas(root, width=400, height=200, bd=0, highlightthickness=0)
        my_canvas.pack(fill="both", expand=True)

        request = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employees")
        employeesFromResponse = request.json()["Items"]
        x = -100
        y = 200
        for emp in employeesFromResponse:
            if x > 1000:
                x = -100
                y += 200
            lastN = emp["lastName"]
            birthday = emp["dob"]
            status = emp["status"]
            address = emp["address"]
            id = emp["id"]
            email = emp["email"]
            phone = emp["phone"]
            firstN = emp["firstName"]
            roleId = emp["roleID"]
            x += 250

            for theEmp in range(9):

                if theEmp == 1:
                    print("debug")
                    my_canvas.create_text(x, y, text="Last Name: " + lastN, font=("Helvetica", 10), fill="black")
                elif theEmp == 2:
                    my_canvas.create_text(x, y-20, text="Birthday: " + birthday, font=("Helvetica", 10), fill="black")
                elif theEmp == 3:
                    my_canvas.create_text(x, y-40, text="Status : " + status, font=("Helvetica", 10), fill="black")
                elif theEmp == 4:
                    my_canvas.create_text(x, y-60, text="Address: " + address, font=("Helvetica", 10), fill="black")
                elif theEmp == 5:
                    my_canvas.create_text(x, y-80, text="ID: " + str(id), font=("Helvetica", 10), fill="black")
                elif theEmp == 6:
                    my_canvas.create_text(x, y-100, text="Email: " + email, font=("Helvetica", 10), fill="black")
                elif theEmp == 7:
                    my_canvas.create_text(x, y-120, text="Phone: " + phone, font=("Helvetica", 10), fill="black")
                elif theEmp == 8:
                    my_canvas.create_text(x, y-140, text="First Name: " + firstN, font=("Helvetica", 10), fill="black")
                elif theEmp == 9:
                    my_canvas.create_text(x, y-160, text="Role ID: " + str(roleId), font=("Helvetica", 10), fill="black")
    except requests.exceptions.HTTPError as err:
        print(err)


"""
            my_canvas.create_text(600, 500, text="Last Name: " + lastN, font=("Helvetica", 10), fill="black")
            my_canvas.create_text(600, 450, text="Birthday: " + birthday, font=("Helvetica", 10), fill="black")
            my_canvas.create_text(600, 400, text="Status : " + status, font=("Helvetica", 10), fill="black")
            my_canvas.create_text(600, 350, text="Address: " + address, font=("Helvetica", 10), fill="black")
            my_canvas.create_text(600, 300, text="ID: " + str(id), font=("Helvetica", 10), fill="black")
            my_canvas.create_text(600, 250, text="Email: " + email, font=("Helvetica", 10), fill="black")
            my_canvas.create_text(600, 200, text="Phone: " + phone, font=("Helvetica", 10), fill="black")
            my_canvas.create_text(600, 150, text="First Name: " + firstN, font=("Helvetica", 10), fill="black")
            my_canvas.create_text(600, 100, text="Role ID: " + str(roleId), font=("Helvetica", 20), fill="black")
"""


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
