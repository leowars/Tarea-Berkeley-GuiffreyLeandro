import socket
import time

SLAVES = [("localhost", 10001), ("localhost", 10002)]
MY_PORT = 10000

def get_time():
    # Simulamos el reloj local del maestro
    return int(time.time()) % 100000  # Solo los últimos dígitos para fácil lectura

def main():
    print("[Master] Iniciando servidor maestro...")

    while True:
        print("\n[Master] Iniciando nueva ronda de sincronización...")
        local_time = get_time()
        print(f"[Master] Mi hora local: {local_time}")

        # 1. Consulta las horas de los esclavos
        slave_times = []
        for host, port in SLAVES:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.connect((host, port))
                    s.sendall(b"TIME?")
                    slave_time = int(s.recv(1024).decode())
                    slave_times.append(slave_time)
                    print(f"[Master] Recibido de esclavo en {port}: {slave_time}")
                except Exception as e:
                    print(f"[Master] Error comunicando con {port}: {e}")

        # 2. Calcula el promedio
        all_times = [local_time] + slave_times
        avg_time = sum(all_times) // len(all_times)
        print(f"[Master] Promedio calculado: {avg_time}")

        # 3. Calcula el ajuste y lo envía a cada esclavo
        for idx, (host, port) in enumerate(SLAVES):
            correction = avg_time - slave_times[idx]
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.connect((host, port))
                    s.sendall(f"ADJUST {correction}".encode())
                    print(f"[Master] Ajuste enviado a esclavo en {port}: {correction}")
                except Exception as e:
                    print(f"[Master] Error enviando ajuste a {port}: {e}")

        # 4. Ajusta su propio reloj (simulado, solo muestra)
        my_correction = avg_time - local_time
        print(f"[Master] Mi ajuste local: {my_correction}")
        print("[Master] Esperando 10 segundos para la próxima sincronización...\n")
        time.sleep(10)

if __name__ == "__main__":
    main()