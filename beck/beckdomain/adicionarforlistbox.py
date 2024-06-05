
def addddd ():
    print()

def thebutton():
    from tkinter.filedialog import askopenfilename
    from tkinter.messagebox import askyesno
    import customtkinter as cct
    import tkinter as tk
    from tkinter import messagebox
    def cert():
        preguntade1o0=askyesno(title="confirmação", message="Voce tem certeza?")
        print(preguntade1o0)
    arquivocomputer=askopenfilename(title="Selecione um arquivo .wav")
    if arquivocomputer!="":
        janela_tecla=cct.CTk()
        tecla21=cct.CTkEntry(janela_tecla)
        tecla21.insert(0, "Insira a tecla")
        tecla21.grid(column=0, row=0)

        botao21=cct.CTkButton(janela_tecla, command=cert)
        botao21.grid(column=0, row=1)

        janela_tecla.mainloop()
    else:
        messagebox.showerror(title="ERROR", message="mensagem")