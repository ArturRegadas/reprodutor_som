import pyaudio
import os

# Inicialize o PyAudio
p = pyaudio.PyAudio()

# Obtenha o número de dispositivos de áudio
num_devices = p.get_device_count()

print("Dispositivos de áudio disponíveis:")
for i in range(num_devices):
    device_info = p.get_device_info_by_index(i)
    if "input" in device_info['name']:
        print(f"{device_info['index']}: {device_info['name']}")

# Encerre o PyAudio
p.terminate()

# Substitua "Nome do Dispositivo" pelo nome do dispositivo que você deseja configurar como entrada padrão
device_name = input()

# Execute o comando do PowerShell para definir o dispositivo de áudio como entrada padrão
os.system(f"powershell -Command \"Set-DefaultAudioDevice -Name '{device_name}' -Role Multimedia\"")