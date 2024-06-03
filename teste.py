import os
import ctypes
import sys

def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        # Executar novamente com permissões elevadas
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        return False

# Verificar se o script está sendo executado como administrador
if not run_as_admin():
    print("O script está sendo executado como administrador.")
    # O script será encerrado agora, pois foi relançado com permissões elevadas.
    sys.exit()
else:
    print("O script está sendo executado como administrador.")
    # O código do seu script Python continua aqui.
    # Insira aqui o código que você deseja executar como administrador.



    # Listar os dispositivos de entrada disponíveis
    os.system("powershell.exe Install-Module AudioDeviceCmdlets")
    os.system("powershell.exe Get-AudioDevice -list")
def change_audio_input(device_index):
    # Comando PowerShell para definir o dispositivo de entrada padrão
    powershell_command = f"Set-AudioDevice -Index {device_index}"
    os.system(f"powershell.exe -Command \"{powershell_command}\"")


    # Escolher o ID do dispositivo que você deseja usar como entrada de áudio
    # Normalmente, você pode obter esses IDs listando os dispositivos disponíveis
device_id = "5"

    # Mudar a entrada de áudio para o dispositivo selecionado
change_audio_input(device_id)
input()