import socket
import threading
import time
import random

# Este esclavo escucha en el puerto 10002
MY_PORT = 10002

# Simulamos reloj local con un offset aleatorio al inicio
local_time = int(time.time()) % 100000 + random.randint(-50, 50)
lock = threading.Lock()

def get_time():
    with lock:
        return local_time

def adjust_time(delta):
    global local_time
    with lock:
        local_time += delta

def time_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", MY_PORT))
    s.listen()
    print(f"[Slave@{MY_PORT}] Servidor escuchando en puerto {MY_PORT}")

    while True:
        conn, addr = s.accept()
        data = conn.recv(1024).decode()
        if data == "TIME?":
            # Envía la hora local
            conn.sendall(str(get_time()).encode())
        elif data.startswith("ADJUST"):
            # Recibe el ajuste y modifica el reloj
            _, delta = data.split()
            adjust_time(int(delta))
            print(f"[Slave@{MY_PORT}] Reloj ajustado por {delta}. Nueva hora: {get_time()}")
        conn.close()

def reloj_tictac():
    global local_time
    while True:
        time.sleep(1)
        with lock:
            local_time += 1

if __name__ == "__main__":
    threading.Thread(target=time_server, daemon=True).start()
    threading.Thread(target=reloj_tictac, daemon=True).start()
    while True:
        print(f"[Slave@{MY_PORT}] Hora local: {get_time()}")
        time.sleep(5)