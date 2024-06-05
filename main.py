import customtkinter as ctk
import ttkthemes as ttk
import tkinter as tk
import beck.beckdomain.adicionarforlistbox as bba
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilename

janela=ctk.CTk()

janela.title("Silvio Maker")
janela.geometry("500x300")
janela.resizable(False, False)


list_audios=tk.Listbox(janela, bg="gray",highlightthickness = 0, bd = 0,)
list_audios.place(x=15, y=20, width=215, height=210)

botaoadd=ctk.CTkButton(janela,width=170, height=35, command=bba.thebutton)
botaoadd.place(x=35, y=245)


#saber posição
def clique(retorno):
    print(f'x:{retorno.x} / y : {retorno.y} geo :{janela.geometry()}')
janela.bind('<Button-3>', clique)


janela.mainloop()