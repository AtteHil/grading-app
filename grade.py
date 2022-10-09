import os
from tkinter import *
from PIL import ImageTk, Image


a_list=[] ## set to global so I can access it in different methods
root = Tk() ## root window set
root.title('Grade this')
root.geometry("500x600")


def main():
    
    global count

    path= os.getcwd()
    root.iconbitmap(path)
    Descritpion= Label(root, text="Grade product show with buttons below").grid(row=0, columnspan=2)
    makelists()
    count= len(list_images)
    imgLabel= Label(image=list_images[0])
    imgLabel.grid(row=1,columnspan=2)
        
    Goodbutton= Button(root, text="Good", fg='black', bg='green',padx=10, pady=5 , command=lambda: Good(2)).grid(row=2,column=0)

    badButton=Button(root, text="Bad", fg='white', bg='red', padx=10, pady=5,command=lambda: Bad(2)).grid(row=2,column=1)

def makelists():
    global list_images
    global small_images
    my_image1= ImageTk.PhotoImage(Image.open("pics/longdrink.jpg").resize((500,500), Image.Resampling.LANCZOS))

    my_image2=ImageTk.PhotoImage(Image.open("pics/banana.jpg").resize((500,500), Image.Resampling.LANCZOS))
    my_image3=ImageTk.PhotoImage(Image.open("pics/karhu.jfif").resize((500,500), Image.Resampling.LANCZOS))
    my_image4=ImageTk.PhotoImage(Image.open("pics/breezer.png").resize((500,500), Image.Resampling.LANCZOS))
    my_image5=ImageTk.PhotoImage(Image.open("pics/cider.jpg").resize((500,500), Image.Resampling.LANCZOS))
    my_image6=ImageTk.PhotoImage(Image.open("pics/sandels.jpg").resize((500,500), Image.Resampling.LANCZOS))
    my_image7=ImageTk.PhotoImage(Image.open("pics/longdrinkKoff.jpg").resize((500,500), Image.Resampling.LANCZOS))
    list_images = [my_image1,my_image2, my_image3, my_image4,my_image5,my_image6,my_image7]

    small_image2=ImageTk.PhotoImage(Image.open("pics/banana.jpg").resize((90,90), Image.Resampling.LANCZOS))
    small_image1= ImageTk.PhotoImage(Image.open("pics/longdrink.jpg").resize((90,90), Image.Resampling.LANCZOS))
    small_image3=ImageTk.PhotoImage(Image.open("pics/karhu.jfif").resize((90,90), Image.Resampling.LANCZOS))
    small_image4=ImageTk.PhotoImage(Image.open("pics/breezer.png").resize((90,90), Image.Resampling.LANCZOS))
    small_image5=ImageTk.PhotoImage(Image.open("pics/cider.jpg").resize((90,90), Image.Resampling.LANCZOS))
    small_image6=ImageTk.PhotoImage(Image.open("pics/sandels.jpg").resize((90,90), Image.Resampling.LANCZOS))
    small_image7=ImageTk.PhotoImage(Image.open("pics/longdrinkKoff.jpg").resize((90,90), Image.Resampling.LANCZOS))
    
    small_images= [small_image1, small_image2, small_image3, small_image4, small_image5, small_image6, small_image7]





def makeTopLevel(): ## opens new window and makes your chart
    top = Toplevel()
    top.geometry("500x460")
    top.title('Result')
    resultTitle= Label(top, text="Results are shown here").grid(row=0, columnspan=2)
    tierGood= Label(top, text="GOOD", background='green',padx=25, pady=100, font=12, fg='black',width=10).grid(row=1,rowspan=2, column=0)
    tierBad= Label(top, text="BAD", background='red',padx=25, pady=100, font=12, fg='white', width=10).grid(row=3, rowspan=2, column=0)
    a=1
    b=1
    c=3
    d=1
    for i in range(count):
        
        if a_list[i]==0:
            
            imgLabel= Label(top,image=small_images[i]).grid(row=c,column=a)
            
            if c==3:
                c=4
            else:
                c=3
            if c==3:
                a+=1

        else:
            imgLabel = Label(top, image=small_images[i]).grid(row=d, column=b)
            
            if d==1:
                d=2
            else:
                d=1
            if d==1:
                b+=1
        

    
    

def Good(number): ##Good button function
    global imgLabel
    
    if count == number-1:
        a_list.append(1)
        makeTopLevel()
        return
   
    imgLabel= Label(image=list_images[number-1]).grid(row=1,columnspan=2)
    
    Goodbutton= Button(root, text="Good", fg='black', bg='green',padx=10, pady=5 , command=lambda: Good(number+1)).grid(row=2,column=0)
    badButton=Button(root, text="Bad", fg='white', bg='red', padx=10, pady=5,command=lambda: Bad(number+1)).grid(row=2,column=1)
    a_list.append(1)
    
def Bad(number): ##bad button function
    global imgLabel
    global count
    if count == number-1:
        a_list.append(0)
        makeTopLevel()
        return

    imgLabel= Label(image=list_images[number-1]).grid(row=1,columnspan=2)
    
    Goodbutton= Button(root, text="Good", fg='black', bg='green',padx=10, pady=5 , command=lambda: Good(number+1)).grid(row=2,column=0)
    badButton=Button(root, text="Bad", fg='white', bg='red', padx=10, pady=5,command=lambda: Bad(number+1)).grid(row=2,column=1)
    a_list.append(0)
    




main()
root.mainloop()
