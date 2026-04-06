import socket
import serial
import time

# --- CONFIGURACIÓN ---
# Probamos con USB0 que es el más común, o USB1 según tu ls
SERIAL_PORT = '/dev/ttyUSB0' 
BAUD_RATE = 115200
HOST = "0.0.0.0"  # Escucha en todas las interfaces (WiFi y Tailscale)
PORT = 5000

def conectar_esp32():
    try:
        esp = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"✅ Conectado al ESP32 en {SERIAL_PORT}")
        return esp
    except Exception as e:
        print(f"⚠️ Alerta: No se detectó el ESP32 en {SERIAL_PORT}: {e}")
        print("El servidor seguirá activo para recibir comandos del PC.")
        return None

# --- INICIALIZACIÓN ---
esp = conectar_esp32()

# Crear el Socket del servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Reusable address para evitar el error "Address already in use" al reiniciar
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(1)

print(f"🚀 Servidor AMR listo. IP Tailscale: 100.103.205.123")
print("Esperando conexión del PC...")

try:
    while True:
        conn, addr = sock.accept()
        print(f"✨ PC conectado desde: {addr}")
        
        try:
            while True:
                # Recibimos datos del PC (Windows)
                data = conn.recv(1024).decode('utf-8')
                
                if not data:
                    print("⚠️ Conexión perdida con el PC.")
                    break
                
                # Procesamos cada caracter recibido (w, a, s, d, x)
                for char in data:
                    print(f"🕹️ Recibido: {char} -> Enviando al ESP32")
                    
                    # Verificamos si el ESP32 está conectado antes de escribir
                    if esp and esp.is_open:
                        esp.write(char.encode())
                    else:
                        # Intentamos reconectar el ESP32 si se desconectó físicamente
                        print("🔌 Intentando reconectar con el ESP32...")
                        esp = conectar_esp32()
                        
        except ConnectionResetError:
            print("! La conexión fue forzada a cerrarse.")
        finally:
            conn.close()
            print("🔄 Esperando nueva conexión...")

except KeyboardInterrupt:
    print("\n🛑 Servidor detenido por el usuario.")
finally:
    if esp and esp.is_open:
        esp.close()
    sock.close()