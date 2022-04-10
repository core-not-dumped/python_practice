# button = you click it, then it does stuff

from tkinter import *

window = Tk()

count = 0

def click():
    global count
    count += 1
    print(count)

# photo = PhotoImage(file='like.png')

# activeforeground -> when you are click the button
# state = DISABLE -> not active, you cannot click the button
button= Button(window,
               text="click me!",
               command=click,
               font=("Comic Sans", 30),
               fg="00FF00",
               bg="black",
               activeforeground="00FF00",
               activebackground="black",
               state=ACTIVE
               )

# image = photo
# compound = 'bottom'

button.pack()

window.mainloop()

