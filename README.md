# Tarea-Berkeley-GuiffreyLeandro

Implementación en Python del Algoritmo de Berkeley para sincronizar relojes entre tres computadoras (un maestro y dos esclavos) utilizando sockets.

## Archivos

- `master.py`: proceso maestro, inicia la sincronización y coordina los ajustes de reloj.
- `slave.py`: proceso esclavo, responde al maestro y ajusta su reloj en el puerto 10001.
- `slave2.py`: proceso esclavo, responde al maestro y ajusta su reloj en el puerto 10002.

## Ejecución

1. Abre 3 terminales.
2. En la primera terminal, ejecuta el primer esclavo (puerto 10001):
   ```bash
   python slave.py
   ```
3. En la segunda terminal, ejecuta el segundo esclavo (puerto 10002):
   ```bash
   python slave2.py
   ```
4. En la tercera terminal, ejecuta el maestro:
   ```bash
   python master.py
   ```

Cada proceso simula un reloj local y realiza la sincronización periódicamente.

---
**Importante:**  
Verifica que tienes Python instalado y los puertos 10000, 10001 y 10002 libres en tu equipo.
