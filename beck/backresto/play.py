import pyaudio
import wave
import sys

file_path = "X2Download.app-Olha-Se-Você-Não-Me-Ama-_128-kbps_.wav"
wave_file = wave.open(file_path, 'rb')

p = pyaudio.PyAudio()

stream_out = p.open(format=p.get_format_from_width(wave_file.getsampwidth()),
                channels=wave_file.getnchannels(),
                rate=wave_file.getframerate(),
                output=True)

data = wave_file.readframes(1024)

print("Reproduzindo áudio na entrada do microfone...")
while data:
    stream_out.write(data)
    data = wave_file.readframes(1024)

stream_out.stop_stream()
stream_out.close()

wave_file.close()

p.terminate()