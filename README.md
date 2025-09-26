# Tarea-Berkeley-GuiffreyLeandro

Implementación en Python del Algoritmo de Berkeley para sincronizar relojes entre tres computadoras (un maestro y dos esclavos) utilizando sockets.

## Archivos

- master.py: proceso maestro, inicia la sincronización y coordina los ajustes de reloj.
- slave.py: proceso esclavo, responde al maestro y ajusta su reloj.

## Ejecución

1. Abre 3 terminales.
2. En la primera terminal, ejecuta el maestro:
   ```bash
   python master.py
   ```
3. En la segunda terminal, ejecuta el primer esclavo (puerto 10001):
   ```bash
   python slave.py
   ```
4. En la tercera terminal, ejecuta el segundo esclavo (cambia MY_PORT = 10001 a MY_PORT = 10002 en slave.py antes de ejecutar):
   ```bash
   python slave.py
   ```

Cada proceso simula un reloj local y realiza la sincronización periódicamente.