import tkinter as tk
from tkinter import ttk, messagebox
import urllib.parse

def url_encoder():
    url = entry_input.get()
    encoded_url = urllib.parse.quote(url)
    entry_output.delete(0, tk.END)
    entry_output.insert(0, encoded_url)
    

def url_decoder():
    encoded_url = entry_input.get()
    decoded_url = urllib.parse.unquote(encoded_url)
    entry_output.delete(0, tk.END)
    entry_output.insert(0, decoded_url)

root = tk.Tk()
root.title("URL Encoder/Decoder")
style = ttk.Style(root)
style.theme_use('classic')
style.configure('TLabel', font=('Anton', 12), padding=5)
style.configure('TEntry', font=('Impact', 12))
style.configure('TButton', font=('Helvetica', 12), padding=5, background='#193276', foreground='black')

label_input = ttk.Label(root, text="Enter URL:")
label_input.grid(row=0, column=0, padx=10, pady=10)
entry_input = ttk.Entry(root, width=50)
entry_input.grid(row=0, column=1, padx=10, pady=10)
label_output = ttk.Label(root, text="Output URL:")
label_output.grid(row=1, column=0, padx=10, pady=10)
entry_output = ttk.Entry(root, width=50)
entry_output.grid(row=1, column=1, padx=10, pady=10)

button_encode = ttk.Button(root, text="Encode", command=url_encoder)
button_encode.grid(row=2, column=0, padx=10, pady=10)
button_decode = ttk.Button(root, text="Decode", command=url_decoder)
button_decode.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
