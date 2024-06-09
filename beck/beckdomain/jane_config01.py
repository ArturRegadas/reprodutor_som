import customtkinter as ctk
import tkinter as tk
import soundcard as sc

def listar():
    list_c_auds=[]
    input_devices = sc.all_microphones()
    for i, device in enumerate(input_devices):
        list_c_auds.append(f"0  {device}")

    output_devices = sc.all_speakers()
    for i, device in enumerate(output_devices):
        list_c_auds.append(f"1  {device}")
    c=1
    x=[]
    for i in list_c_auds:
        l=i.split("  ")
        if l[0] == "1":
            c+=1
    for i in list_c_auds:
        l=i.split("  ")
        if l[0] == "0":
            x.append(f"{c} {l[1]}")
            c+=1
    return x
def configurar():
    
    listacomosbgl=listar()

    janela_da_config=ctk.CTk()

    janela_da_config.title("Configurar Programa")
    janela_da_config.geometry("300x150")
    janela_da_config.resizable(False, False)

    label1=ctk.CTkLabel(text="Pedir Permissão?")
    label1.place(x=0, y=0)


    janela_da_config.mainloop()