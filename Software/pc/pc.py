import socket
import msvcrt # Solo para Windows

# CONFIGURACIÓN: La IP de Tailscale de tu Raspi que vimos en la foto
IP_RASPI = "100.103.205.123" 
PUERTO = 5000

try:
    # Crear conexión
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((IP_RASPI, PUERTO))
    print(f"✅ CONECTADO A EL AMR (vía Tailscale)")
    print("Controles: W (Adelante), S (Atrás), A (Izquierda), D (Derecha), X (Stop)")
    print("Presiona 'q' para salir del programa.")

    while True:
        # Captura tecla sin esperar Enter
        if msvcrt.kbhit():
            tecla = msvcrt.getch().decode('utf-8').lower()
            
            if tecla == 'q':
                break
            
            # Enviar la tecla al servidor (Raspi)
            if tecla in ['w', 'a', 's', 'd', 'x']:
                cliente.send(tecla.encode())
                print(f"Enviado: {tecla}")

except Exception as e:
    print(f"❌ Error de conexión: {e}")
finally:
    cliente.close()
    print("Conexión cerrada.")