from tkinter import *

#label = an area widget that holds text and/or an image within a window

window = Tk()


# if you want to see image
#photo = PhotoImage(file='abc.png')

# fg, text color bg, text background color relief, surround effect
# padx, pady, padidng
label = Label(window,
              text="Hello",
              font=('Arial', 40, 'bold'),
              fg = '#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20
              )
# image = photo <- you will see image, replace the text
# compount='bottom' <- you will see image and text, image is bottom


label.pack()
#label.place(x=100, y=100)


window.mainloop()


