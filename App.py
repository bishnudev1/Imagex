from distutils.log import Log
from tkinter import *
from PIL import ImageTk, Image
import cv2
from cv2 import COLOR_BGR2GRAY
from cv2 import invert

# App Init

root = Tk()
root.title('Imagex - Bishnudev Khutia')
root.geometry('800x480')
root.resizable(False, False)
root.configure(bg='#0f1a2b')

# icon
# Icon = PhotoImage(file="/ImpFiles/Logo.png")
# root.iconphoto(False, Icon)

# User Interface

Head_Text = Label(root, text='Image to Sketch Converter',bg='#0f1a2b', fg='white',font=('Arial 24')).pack(fill="x")

OriginalText = Label(root,text="Original",fg="white",bg="#0f1a2b").place(x=205,y=65)

image=Image.open('Original.png')
img=image.resize((250, 250))
my_img=ImageTk.PhotoImage(img)
label=Label(root, image=my_img).place(x=105,y=105)

image2=Image.open('Sketch.png')
img=image2.resize((250, 250))
my_img2=ImageTk.PhotoImage(img)

# App Functions

def convertIMG():

    image = cv2.imread("Original.png")
    gray = cv2.cvtColor(image, cv2.IMREAD_GRAYSCALE)
    invert = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    invertblur = cv2.bitwise_not(blur)

    Label(root,text="Sketch",fg="white",bg="#0f1a2b").place(x=541,y=65)
    sketch = cv2.divide(gray, invertblur, scale=260)
    cv2.imwrite("Sketch.png", sketch)
    Label(root, image=my_img2).place(x=435,y=105)
    root.update()

def ResetFunc():
    root.destroy()

# Button

ConvertImg = Button(root, text="Convert", fg="white",
                    bg="#0f1a2b", command=convertIMG).place(x=372, y=400)

ResetBtn = Button(root, text="Reset App", fg="white",
                    bg="#0f1a2b", command=ResetFunc).place(x=367, y=440)

root.mainloop()
