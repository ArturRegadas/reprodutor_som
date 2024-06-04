from pynput.keyboard import Key, Listener, KeyCode
start_stop_key = KeyCode(char="p")
stop_key = KeyCode(char="esc")

def on_press(key):
    #== -> in
    if key == start_stop_key:
        print("e")
        return True
        

def on_release(key):
    if key == stop_key:
        print("esc")
        return False
        

# Inicia o listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()