#  Sistema de Teleoperación de Drone con Tailscale

##  Descripción

Este proyecto implementa un sistema de teleoperación para un drone utilizando una arquitectura distribuida basada en sistemas embebidos y redes privadas seguras.

El sistema integra:

-  Raspberry Pi (nodo de control)
-  ESP32 (generación de PWM)
-  Driver L298N (control de motores)
-  Tailscale (VPN mesh para comunicación remota)

---

##  Objetivo

Permitir el control remoto de un drone a través de internet sin necesidad de:

- Configuración de puertos (port forwarding)
- IP pública fija
- Configuración compleja de red

---

##  ¿Qué es Tailscale?

Tailscale es una VPN basada en WireGuard que permite conectar dispositivos como si estuvieran en la misma red local.

Ventajas:
- Comunicación segura (encriptada)
- Evita NAT
- Conexión directa entre dispositivos
- Configuración simple

---

##  Conceptos de Red

### IP
- Local: dentro de la red (ej: 192.168.x.x)
- Pública: accesible desde internet

### NAT
Permite que múltiples dispositivos compartan una IP pública, pero bloquea conexiones entrantes.

### VPN
Crea un canal seguro entre dispositivos a través de internet.

---

##  Arquitectura del Sistema

PC (Usuario)
↓
Tailscale VPN
↓
Raspberry Pi
↓ (Serial)
ESP32
↓ (PWM)
L298N
↓
Motores

---

##  Flujo de Operación

1. El usuario envía un comando desde el PC
2. El comando viaja por la red Tailscale
3. La Raspberry Pi recibe y procesa el comando
4. Se envía al ESP32 por comunicación serial
5. El ESP32 genera señales PWM
6. El L298N acciona los motores

---

##  Tecnologías Utilizadas

- Python (Raspberry Pi)
- C++ / Arduino (ESP32)
- Tailscale (Networking)
- UART (Comunicación)
- PWM (Control de motores)

---

##  Aplicaciones

- Robótica teleoperada
- Vehículos autónomos
- Inspección remota
- Agricultura inteligente

---

##  Mejoras Futuras

- Streaming de video en tiempo real
- Control mediante app web
- Integración de sensores
- Navegación autónoma
- Machine Learning para control inteligente

---

##  Enfoque Ingenieril

Este proyecto demuestra:

- Integración hardware-software
- Diseño de sistemas distribuidos
- Networking avanzado (VPN, NAT traversal)
- Separación de responsabilidades