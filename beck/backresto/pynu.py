from pynput.keyboard import Key, Listener, KeyCode
start_stop_key = KeyCode(char="1")
stop_key = KeyCode(char="'")


def on_press(key):
    try:
        tecla_p=key.char
        print('Tecla pressionada: {0}'.format(tecla_p))
    except AttributeError:
        tecla_p=key
        print('Tecla especial pressionada: {0}'.format(tecla_p))

def on_release(key):
    if key == stop_key:
        print("esc")
        return False
        
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()