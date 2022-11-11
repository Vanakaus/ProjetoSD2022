import tkinter as tk

window = tk.Tk()
window.title("Servidor")
window.geometry("800x500")
window.configure(bg="#00c8ff")

lbl_titulo = tk.Label(text="Jogo da Memoria", bg="#00c8ff", font=("Arial", 32))
lbl_titulo.place(x=220, y = 30)

lbl_players = tk.Label(text="Players:", bg="#00c8ff", font=("arial", 22))
lbl_players.place(x=80, y=150)

lbl_listPlayers = tk.Label(text="João Vitor - 8 \nVinicius - 5", bg="#00c8ff", font=("arial", 18), justify="left")
lbl_listPlayers.place(x=40, y=220)



mesa = tk.Frame(window, width=500, height=380, bg="#fefefe")
mesa.place(x=250, y=100)

mesa2 = tk.Frame(mesa)
mesa2.place(x=75, y=7)



carta00 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta00.grid(column=1, row=1, padx=10, pady=10)
carta01 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta01.grid(column=2, row=1, padx=10, pady=10)
carta02 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta02.grid(column=3, row=1, padx=10, pady=10)
carta03 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta03.grid(column=4, row=1, padx=10, pady=10)
carta04 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta04.grid(column=5, row=1, padx=10, pady=10)
carta05 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta05.grid(column=6, row=1, padx=10, pady=10)

carta10 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta10.grid(column=1, row=2, padx=10, pady=10)
carta11 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta11.grid(column=2, row=2, padx=10, pady=10)
carta12 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta12.grid(column=3, row=2, padx=10, pady=10)
carta13 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta13.grid(column=4, row=2, padx=10, pady=10)
carta14 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta14.grid(column=5, row=2, padx=10, pady=10)
carta15 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta15.grid(column=6, row=2, padx=10, pady=10)

carta20 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta20.grid(column=1, row=3, padx=10, pady=10)
carta21 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta21.grid(column=2, row=3, padx=10, pady=10)
carta22 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta22.grid(column=3, row=3, padx=10, pady=10)
carta23 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta23.grid(column=4, row=3, padx=10, pady=10)
carta24 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta24.grid(column=5, row=3, padx=10, pady=10)
carta25 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta25.grid(column=6, row=3, padx=10, pady=10)

carta30 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta30.grid(column=1, row=4, padx=10, pady=10)
carta31 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta31.grid(column=2, row=4, padx=10, pady=10)
carta32 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta32.grid(column=3, row=4, padx=10, pady=10)
carta33 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta33.grid(column=4, row=4, padx=10, pady=10)
carta34 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta34.grid(column=5, row=4, padx=10, pady=10)
carta35 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta35.grid(column=6, row=4, padx=10, pady=10)

carta40 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta40.grid(column=1, row=5, padx=10, pady=10)
carta41 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta41.grid(column=2, row=5, padx=10, pady=10)
carta42 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta42.grid(column=3, row=5, padx=10, pady=10)
carta43 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta43.grid(column=4, row=5, padx=10, pady=10)
carta44 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta44.grid(column=5, row=5, padx=10, pady=10)
carta45 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta45.grid(column=6, row=5, padx=10, pady=10)

carta50 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta50.grid(column=1, row=6, padx=10, pady=10)
carta51 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta51.grid(column=2, row=6, padx=10, pady=10)
carta52 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta52.grid(column=3, row=6, padx=10, pady=10)
carta53 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta53.grid(column=4, row=6, padx=10, pady=10)
carta54 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta54.grid(column=5, row=6, padx=10, pady=10)
carta55 = tk.Button(mesa2, text="test", cursor="hand2", width=4, height=2)
carta55.grid(column=6, row=6, padx=10, pady=10)



# button = tk.Button(text="Click me!")
# button.place(x=20 , y=20)
# button = tk.Button(text="Click me!")
# button.pack()


window.mainloop()