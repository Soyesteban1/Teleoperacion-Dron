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

Tailscale es basicamente un red privada virtual lo que conocemos como VPN, esta red se va conectar a los dispositivos ya sea pc, servidor, raspberry pi, celular, etc. 
Basicamente es como si todos los dispositivos estuvieran en una misma red, aunque esten en diferentes ubiaciones en el mundo y esto es la gran ventaja para la teleoperacion en este proyecto.

 A diferencia de una VPN tradicional como la que conocemos, ejemplo:  Cisco AnyConnect.
  - No se tendra un serividor central como obligatorio para conectar nuestros dispositivos y mejorar la latencia entre ellos.
  - Cada dispositivo se conecta directamente con los otros (peer-to-peer) cuando es posible.

Una VPN como cisco se utiliza mucho en empresas grandes que necesitan que empleados de manera remota accedean a informacion o a la red interna, el orden de como sera esta consulta o acceso sera de la siguiente manera:
 - El usuario se conecta a un servidor VPN centralizado de la empresa.
 - Todo el tráfico se enruta por ese servidor, como si estuvieras físicamente dentro de la oficina

Con tailscale "la VPN de nueva generacion" estilo mesh network (red mallada, comunicacion en la que multiples dispositivos se conectan entre si), el uso que le damos a esta VPN es cuando necesitamos un conexion sencilla a dispositivos personales, equipos de trabajo o servidores en la nube sin necesidad de un servidor central.
Esta VPN se basa en WireGuard, es te protocolo es uno de los mas modernos de VPN diseñado especificamente para ser rapido, simple y seguro
Características principales:
- Usa criptografía de última generación (Curve25519, ChaCha20, Poly1305).
- Tiene un código muy pequeño y eficiente, lo que lo hace más fácil de auditar y mantener.
- Funciona a nivel de capa de red (como IPsec), pero con la simplicidad de OpenVPN.
- Ventaja:
- Mucho más rápido que protocolos antiguos como IPsec o OpenVPN.
- Fácil de configurar (pocas líneas de configuración).
- Ideal para redes modernas tipo mesh (como Tailscale).

NOTA: importante Tailscale es una herramienta muy potente pero no esta pensado para para reemplazar todas las funciones de un VPN corporativo tradicional (como acceso a redes internas muy grandes con políticas complejas).

---

##  Conceptos de Red

## IP VPN (Internet Protocol Virtual Private Network):
Una red privada virtual que usa el protocolo IP para crear un túnel seguro entre dispositivos o redes. Permite que el tráfico viaje cifrado sobre Internet como si estuviera en una red privada.
## NAT (Network Address Translation):
Técnica que traduce direcciones IP privadas a una dirección IP pública (y viceversa). Se usa en routers para que varios dispositivos en una red local compartan una sola IP pública.
## WireGuard:
Protocolo moderno de VPN, diseñado para ser rápido, seguro y sencillo. Utiliza criptografía avanzada y conexiones eficientes, ideal para redes peer-to-peer y soluciones como Tailscale.
## SSL (Secure Sockets Layer):
Protocolo de seguridad que cifra la comunicación entre cliente y servidor en Internet. Aunque hoy se usa más su sucesor TLS, todavía se habla de “SSL” para referirse al cifrado de páginas web (HTTPS).
## IPsec (Internet Protocol Security):
Conjunto de protocolos que aseguran las comunicaciones IP mediante cifrado y autenticación. Muy usado en VPN tradicionales corporativas.
## Mesh (Red mallada):
Arquitectura de red donde cada nodo (dispositivo) puede conectarse directamente con otros, formando una malla. Esto evita depender de un único servidor central y mejora la resiliencia.
## Criptografía:
Ciencia que estudia técnicas para proteger la información mediante el uso de algoritmos matemáticos. Se aplica en VPN, SSL/TLS, WireGuard, etc., para garantizar confidencialidad, integridad y autenticidad.

Relación entre ellos
- IPsec, SSL y WireGuard → Son protocolos de seguridad para crear VPN o cifrar comunicaciones.
- IP VPN → Es el concepto de usar IP + VPN para crear túneles seguros.
- NAT → No cifra, pero ayuda a enrutar y compartir direcciones IP.
- Mesh → Describe cómo se conectan los dispositivos (topología).
- Criptografía → Es la base matemática que hace posible todo lo anterior.

 En pocas palabras: IPsec y SSL son los clásicos protocolos de VPN; WireGuard es el moderno; NAT es la técnica de traducción de IP; Mesh es la forma de conectar nodos; y la criptografía es el corazón que da seguridad a todo.


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


Este proyecto es una base para poder escalar con el tiempo, se puede herramientas como IMUS, CAMARAS, IA, ETC.
si le gustan estas cosas hagamelo saber con sus comentarios

---

##  Enfoque Ingenieril

Este proyecto demuestra:

- Integración hardware-software
- Diseño de sistemas distribuidos
- Networking avanzado (VPN, NAT traversal)
- Separación de responsabilidades
