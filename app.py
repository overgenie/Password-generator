#imports
from random import *
import string
from tkinter import * #importing all elements of the package
title = "password generator"

#create window
window = Tk() #new instance of "Tk" class of tkinter

#create the function that will generate the password
def gen_password():
    password_min = 12
    password_max = 15
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars) for i in range(randint(password_min, password_max)))
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)

#personalization
window.title("password generator")
window.geometry("800x500")
#Disable window resize
window.minsize(800, 500)
window.maxsize(800, 500)
#define window icon
window.iconbitmap("lock.ico")
#changing background color
window.config(background='#41B77F') #Green

#create main frame
frame = Frame(window, bg="#41B77F")

#creating our canvas that will contain key image
height = 300
width = 300
image = PhotoImage(file="key.png").zoom(18).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#41B77F', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

#creating a subframe
right_frame = Frame(frame, bg="#41B77F")

#creating the label that will remind the context of the app
label_title = Label(right_frame, text="Password generator", font=("Helvetica",20), bg="#41B77F", fg="White")
label_title.pack()

#creating the input that will display the random password
pass_entry = Entry(right_frame, font=("Helvetica",20), bg="#41B77F", fg="White")
pass_entry.pack()

#creating the button that will generate the random password
butt = Button(right_frame, text="Generate", font=("Helvetica",20), bg="#41B77F", fg="White", command=gen_password)
butt.pack(fill=X)

#displaying subframe
right_frame.grid(row=0, column=1, sticky=W)

#display our frames
frame.pack(expand=YES)

#main loop of our program
window.mainloop()