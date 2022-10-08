import os
from tkinter import *

from PIL import ImageTk, Image
a_list=[]
root = Tk()
root.title('Grade this')
root.geometry("500x600")


Descritpion= Label(root, text="Grade product show with buttons below").grid(row=0, columnspan=2)


path= os.getcwd()
root.iconbitmap(path)
my_image1= ImageTk.PhotoImage(Image.open("pics/longdrink.jpg").resize((500,500), Image.Resampling.LANCZOS))

my_image2=ImageTk.PhotoImage(Image.open("pics/banana.jpg").resize((500,500), Image.Resampling.LANCZOS))
my_image3=ImageTk.PhotoImage(Image.open("pics/karhu.jfif").resize((500,500), Image.Resampling.LANCZOS))

list_images = [my_image1,my_image2, my_image3]
count= len(list_images)
imgLabel= Label(image=my_image1)
imgLabel.grid(row=1,columnspan=2)
def makeTopLevel():
    top = Toplevel()
    top.geometry("500x600")
    top.title('Result')
    resultTitle= Label(top, text="Results are shown here").grid(row=0, columnspan=2)
    

def Good(number):
    global imgLabel
    global count
    if count == number-1:
        makeTopLevel()
        

        
   
    imgLabel= Label(image=list_images[number-1]).grid(row=1,columnspan=2)
    
    Goodbutton= Button(root, text="Good", fg='black', bg='green',padx=10, pady=5 , command=lambda: Good(number+1)).grid(row=2,column=0)
    badButton=Button(root, text="Bad", fg='white', bg='red', padx=10, pady=5,command=lambda: Bad(number+1)).grid(row=2,column=1)
    a_list.append(1)
    
def Bad(number):
    global imgLabel
    global count
    if count == number-1:
        makeTopLevel()

    imgLabel= Label(image=list_images[number-1]).grid(row=1,columnspan=2)
    
    Goodbutton= Button(root, text="Good", fg='black', bg='green',padx=10, pady=5 , command=lambda: Good(number+1)).grid(row=2,column=0)
    badButton=Button(root, text="Bad", fg='white', bg='red', padx=10, pady=5,command=lambda: Bad(number+1)).grid(row=2,column=1)
    a_list.append(0)
    



Goodbutton= Button(root, text="Good", fg='black', bg='green',padx=10, pady=5 , command=lambda: Good(2)).grid(row=2,column=0)

badButton=Button(root, text="Bad", fg='white', bg='red', padx=10, pady=5,command=lambda: Bad(2)).grid(row=2,column=1)



root.mainloop()

