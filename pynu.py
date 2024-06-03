from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        print('Tecla {0} pressionada'.format(key.char))
    except AttributeError:
        print('Tecla especial {0} pressionada'.format(key))

def on_release(key):
    if key == Key.esc:
        return False

# Inicia o listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()