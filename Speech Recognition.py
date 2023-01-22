from tkinter import *
from tkinter import ttk
from google_trans import Translator

root = Tk()
root.title("Language Translator")
root.geometry("500x500")
root.config(bg = "#F2CCC3")

lbl_title = Label(root, text = "Language Translator", bg = "#F2CCC3", font = ("Curlz MT", 15, "italic"))
lbl_title.place(relx = 0.5, rely = 0.1, anchor = CENTER)

lbl_enter_text = Label(root, text = "Enter Text", bg = "#F2CCC3", font = ("Comic Sans MS", 10, "italic"))
lbl_enter_text.place(relx = 0.1, rely = 0.3, anchor = W)

entry_enter_text = Text(root, bg = "white", font = ("Comic Sans MS", 10, "italic"), height = 7, wrap = WORD, width = 55, padx = 3, pady = 3, bd = 0)
entry_enter_text.place(relx = 0.1, rely = 0.5, anchor = W)