import tkinter as tk  # GUI module
from PIL import ImageTk  # Display background
import tkinter.font as font


def main():
    # ------ get functions will call get user's input, creates a new
    # object------------------------------------------------
    def getFirstName(first):
        # user input  is saved into variables
        first = first_entry.get()

    def getLastname(last):
        last = last_entry.get()

    def getDOB(dateOfBirth):
        dateOfBirth = dob_entry.get()

    def getEmail(email):
        email = email_entry.get()

    def getPhone(phone):
        phone = phone_entry.get()

    def getPosition(jobPosition):
        position_entry.get()

    def getSalary(salary):
        salary = salary_entry.get()

    # --------------------------------------------------------------------------------------------------------------------

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
    my_canvas = tk.Canvas(root, width=1200, height=800, bd=0, highlightthickness=0)
    my_canvas.pack(fill="both", expand=True)

    # using pillow's ImageTk class and PhotoImage function to display background photo
    bg = ImageTk.PhotoImage(file="addEmployee1.jpg")
    my_canvas.create_image(0, 0, image=bg, anchor="nw")

    # create_text function from tkinter will display text onto GUI
    my_canvas.create_text(575, 50, text="Create a new Employee", font=("Helvetica", 21), fill="white")
    my_canvas.create_text(300, 140, text="Firstname", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 190, text="Lastname", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 240, text="DOB", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 290, text="Email", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 340, text="Phone", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 390, text="Position", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 440, text="Salary", font=("Helvetica", 16), fill="white")

    # create Entry text boxes
    first_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    last_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    dob_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    email_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    phone_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    position_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    salary_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)

    first_entry_window = my_canvas.create_window(375, 125, anchor="nw", window=first_entry)
    last_entry_window = my_canvas.create_window(375, 175, anchor="nw", window=last_entry)
    dob_entry_window = my_canvas.create_window(375, 225, anchor="nw", window=dob_entry)
    email_entry_window = my_canvas.create_window(375, 275, anchor="nw", window=email_entry)
    phone_entry_window = my_canvas.create_window(375, 325, anchor="nw", window=phone_entry)
    position_entry_window = my_canvas.create_window(375, 375, anchor="nw", window=position_entry)
    salary_entry_window = my_canvas.create_window(375, 425, anchor="nw", window=salary_entry)

    # We used the Button function in Tkinter which will call the function once clicked
    create_button = tk.Button(root, text="Save", activeforeground='white', font=("Helvetica", 15),
                              width=15, height=20, borderwidth=2, command=lambda: getSalary(salary_entry))

    create_button_window = my_canvas.create_window(550, 550, height=35, anchor="nw", window=create_button)

    root.mainloop()


if __name__ == '__main__':
    main()
