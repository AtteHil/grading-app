import os
from tkinter import *

from PIL import ImageTk, Image

root = Tk()
root.title('Grade this')
root.geometry("500x600")


Descritpion= Label(root, text="Grade product show with buttons below").grid(row=0, columnspan=2)


path= os.getcwd()
root.iconbitmap(path)
my_image1= ImageTk.PhotoImage(Image.open("pics/longdrink.jpg").resize((500,500), Image.Resampling.LANCZOS))

my_image2=ImageTk.PhotoImage(Image.open("pics/banana.jpg").resize((500,500), Image.Resampling.LANCZOS))

list_images = [my_image1,my_image2]
imgLabel= Label(image=my_image1)
imgLabel.grid(row=1,columnspan=2)

def Good(number):
    global imgLabel
    global button_good
    global button_bad
    imgLabel.grid_forget()
    imgLabel= Label(image=list_images[number-1]).grid(row=1,columnspan=2)
    
    
def Bad(number):
    global my_label
    global button_good
    global button_bad
    root.bell()


Goodbutton= Button(root, text="Good", fg='black', bg='green',padx=10, pady=5 , command=lambda: Good(2)).grid(row=2,column=0)

badButton=Button(root, text="Bad", fg='white', bg='red', padx=10, pady=5,command=lambda: Bad(2)).grid(row=2,column=1)



root.mainloop()

