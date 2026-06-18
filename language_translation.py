from tkinter import *
from googletrans import Translator

translator = Translator()

def translate_text():
    text = input_text.get("1.0", END)
    translated = translator.translate(text, dest=language.get())
    output_text.delete("1.0", END)
    output_text.insert(END, translated.text)

root = Tk()
root.title("Language Translation Tool")
root.geometry("600x500")

Label(root, text="Enter Text").pack()

input_text = Text(root, height=8)
input_text.pack()

language = StringVar()
language.set("ta")

Label(root, text="Target Language Code").pack()

Entry(root, textvariable=language).pack()

Button(root, text="Translate", command=translate_text).pack()

output_text = Text(root, height=8)
output_text.pack()

root.mainloop()
