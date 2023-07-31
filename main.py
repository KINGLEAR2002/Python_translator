from tkinter import *
from tkinter import ttk
from googletrans import Translator

def translate_text():
    src_lang = comb_sor.get()
    dest_lang = comb_dest.get()
    text = source_text.get(1.0, END).strip()

    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang)

    dest_text.delete(1.0, END)
    dest_text.insert(END, translated_text.text)

root = Tk()
root.title("Text Translator")
root.geometry("500x400")
root.config(bg='black')

frame = Frame(root, bg='black')
frame.pack(pady=20)

lab_src = Label(frame, text="Source Language", font=("Times New Roman", 12, "bold"), fg="yellow", bg='black')
lab_src.grid(row=0, column=0, padx=10, pady=5)

supported_languages = ["en", "es", "fr", "de", "it", "pt", "nl", "zh-CN", "ja", "ko", "ru", "ar", "hi","ml"]

comb_sor = ttk.Combobox(frame, values=supported_languages, state="readonly")
comb_sor.grid(row=0, column=1, padx=10, pady=5)
comb_sor.set("en")

lab_dest = Label(frame, text="Destination Language", font=("Times New Roman", 12, "bold"), fg="yellow", bg='black')
lab_dest.grid(row=0, column=2, padx=10, pady=5)

comb_dest = ttk.Combobox(frame, values=supported_languages, state="readonly")
comb_dest.grid(row=0, column=3, padx=10, pady=5)
comb_dest.set("es")

source_text = Text(root, font=("Times New Roman", 14), wrap=WORD)
source_text.pack(pady=20, padx=10, fill=BOTH, expand=True)

translate_button = Button(root, text="Translate", relief=RAISED, command=translate_text)
translate_button.pack(pady=10)

dest_text = Text(root, font=("Times New Roman", 14), wrap=WORD)
dest_text.pack(pady=20, padx=10, fill=BOTH, expand=True)

root.mainloop()
