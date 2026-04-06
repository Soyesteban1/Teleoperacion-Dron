#include <Arduino.h> // Línea obligatoria en PlatformIO
// Pines
// Pines
// Pines
int IN1 = 25; int IN2 = 26;
int IN3 = 27; int IN4 = 14;
int ENA = 32; int ENB = 33;

// 1. Asegúrate de declarar los pines de Enable como Salida
void setup() {
  Serial.begin(115200);
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT);
  
  pinMode(ENA, OUTPUT); // Pin 32
  pinMode(ENB, OUTPUT); // Pin 33
}

void loop() {
  if (Serial.available()) {
    char cmd = Serial.read();

    if (cmd == 'w') { // Adelante
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      digitalWrite(IN3, HIGH);
      digitalWrite(IN4, LOW);
      
      // En lugar de ledcWrite, usa analogWrite para probar
      // 255 es el máximo (equivalente al jumper físico)
      analogWrite(ENA, 255); 
      analogWrite(ENB, 255);
      
      Serial.println("Movimiento: Adelante al 100%");
    }
    
    if (cmd == 'x') { // Stop
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, LOW);
      analogWrite(ENA, 0);
      analogWrite(ENB, 0);
    }
  }
}