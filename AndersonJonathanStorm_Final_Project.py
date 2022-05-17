# import all needed files and programs
import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

from PIL import Image, ImageTk
from translate import Translator

# create the Tkinter main window with title

Screen = Tk()
Screen.title("Language Translator")

# Define screen size

Screen.geometry("500x250")

# adding colors and pictures
label = ttk.Label(Screen)
img = Image.open(r"C:\\Users\\jonny\\PycharmProjects\\pythonProject\\translator1.jpg")
resizeImage = img.resize((500, 300))
label.img = ImageTk.PhotoImage(resizeImage)
label['image'] = label.img
label.place(x=0, y=0)

# define variables for dropdown list

inputLanguage = StringVar()
translatedLanguage = StringVar()

# designate choices for dropdown menu

languageChoices = {'', '', 'English', 'German', 'French', 'Japanese', 'Spanish'}
inputLanguage.set('English')
translatedLanguage.set('German')

# define outputVar data type

outputVar = StringVar()


# define Translate function

def Translate():
    translator = Translator(from_lang=inputLanguage.get(), to_lang=translatedLanguage.get())
    Translation = translator.translate(textVar.get())
    outputVar.set(Translation)


# create dropdown menus and set up grid location

inputLanguageMenu = OptionMenu(Screen, inputLanguage, *languageChoices)
Label(Screen, text="Choose a Language").grid(row=0, column=1)
inputLanguageMenu.grid(row=1, column=1)

translatedLanguageMenu = OptionMenu(Screen, translatedLanguage, *languageChoices)
Label(Screen, text="Translated to Language").grid(row=0, column=4)
translatedLanguageMenu.grid(row=1, column=4)


# defining functions to clear text and restart program
def clearText():
    textVar.set("")


def restartProgram():
    os.execl(sys.executable, sys.executable, *sys.argv)


# bringing the main screen back to the front when reset

Screen.lift()
Screen.attributes('-topmost', True)
Screen.after_idle(Screen.attributes, '-topmost', False)

# Create text box for user data entry

Label(Screen, text="Enter Text").grid(row=2, column=1)
textVar = StringVar()
Entry(Screen, textvariable=textVar).grid(row=2, column=2)

# Create buttons to clear and reset program and bind enter key to translate button

Button(Screen, text="Clear/Reset", command=lambda: [clearText(), restartProgram()]).grid(row=6,
                                                                                         column=2)

Button(Screen, text="Exit", command=Screen.destroy).grid(row=6, column=6)

Screen.bind('<Return>', lambda event: [openNewWindow(), Translate()])


# create and define openNewWindow function

def openNewWindow():
    newWindow = Toplevel(Screen)
    newWindow.title("Translation")

    # define window geometry

    newWindow.geometry("500x300")

# add image to the background of newWindow
    
    label2 = ttk.Label(newWindow)
    img2 = Image.open(r"C:\Users\jonny\PycharmProjects\pythonProject\interpretation-transcription-translation-569313.jpg")
    resizeImage2 = img2.resize((500, 300))
    label2.img = ImageTk.PhotoImage(resizeImage2)
    label2['image'] = label2.img
    label2.place(x=0, y=0)

    # create text and output for newWindow

    Label(newWindow,
          text="Here is your translations of " + str(inputLanguage.get()) + " to " + str(
              translatedLanguage.get())).grid(row=1, column=1)
    Entry(newWindow, textvariable=outputVar).grid(row=2, column=1)
    # create an exit button
    Button(newWindow, text="Exit", command=newWindow.destroy).grid(row=6, column=6)


# create a button to call both openNewWindow and Translate function

Button(Screen, text="Translate", command=lambda: [openNewWindow(), Translate()]).grid(row=2, column=3, columnspan=3)

Screen.mainloop()
