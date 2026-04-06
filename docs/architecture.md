#  Arquitectura del Sistema

##  Descripción General
Este proyecto implementa un sistema de teleoperación para un dron utilizando una arquitectura distribuida basada en sistemas embebidos y redes privadas.

El sistema está dividido en tres capas principales:

---

##  1. Capa de Control (Cliente - PC)

- El usuario envía comandos (adelante, atrás, izquierda, derecha)
- Se comunica con la Raspberry Pi a través de la red privada de Tailscale
- Puede ser implementado mediante HTTP, sockets o interfaz gráfica

---

##  2. Capa de Procesamiento (Raspberry Pi)

La Raspberry Pi actúa como nodo central del sistema:

Funciones:
- Recibir comandos remotos desde el cliente
- Procesar lógica de control
- Enviar instrucciones al ESP32 mediante comunicación serial (UART)

Ventajas:
- Permite desacoplar la lógica de red del control en tiempo real
- Facilita escalabilidad del sistema

---

##  3. Capa de Actuación (ESP32)

El ESP32 se encarga del control de bajo nivel:

Funciones:
- Generar señales PWM
- Controlar dirección y velocidad de motores
- Ejecutar comandos recibidos desde la Raspberry Pi

---

##  4. Etapa de Potencia (L298N)

- Recibe señales del ESP32
- Controla la alimentación de los motores
- Permite inversión de giro y control de velocidad

---
##  Flujo de Datos

Usuario (PC)
↓
Tailscale VPN
↓
Raspberry Pi
↓ (Serial UART)
ESP32
↓ (PWM)
L298N
↓
Motores

---

##  Decisiones de Diseño

### Separación de responsabilidades
- Raspberry Pi: Networking + lógica
- ESP32: Tiempo real + PWM

### Uso de Tailscale
- Evita NAT
- No requiere configuración de router
- Comunicación segura

### Comunicación Serial
- Baja latencia
- Implementación simple y robusta

---

##  Escalabilidad

Este sistema permite futuras mejoras como:

- Integración de sensores (IMU, GPS)
- Navegación autónoma
- Streaming de video
- Control mediante interfaz web