import tkinter as tk

window = tk.Tk()
window.title("Client")
window.geometry("600x300")

hello = tk.Label(text="Cliente")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()
button = tk.Button(text="Click me!")
button.pack()

tk.mainloop()