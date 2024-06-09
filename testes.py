import customtkinter as ctk
import tkinter as tk
janela_da_config=ctk.CTk()

janela_da_config.title("Configurar Programa")
janela_da_config.geometry("300x150")
janela_da_config.resizable(False, False)

estado=ctk.IntVar()
check=ctk.CTkCheckBox(janela_da_config, text="Pedir Permissão?",variable=estado, onvalue=1, offvalue=0)
check.place(x=0, y=1)

entry=ctk.CTkEntry(janela_da_config)
entry.place(x=150, y=1)
entry.insert(0, "Tecla finalizar")

listacomtudo=tk.Listbox(janela_da_config, relief="flat", bg="slategray4",highlightthickness = 0, bd = 0)
listacomtudo.place(x=5,y=35, height=100, width=290)
listacomtudo.insert(0, "ENTRADAS DE AUDIO: ")



janela_da_config.mainloop()
print(check.get())