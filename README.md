# 🧮 Calculadora Remota TCP

Aplicación cliente-servidor que permite realizar operaciones matemáticas básicas (+, -, *, /) de forma remota utilizando sockets TCP en Python.

## 📋 Descripción

El servidor escucha conexiones en el puerto 5000 y procesa operaciones matemáticas. El cliente solicita dos números y un operador al usuario, envía la información al servidor, recibe el resultado y lo muestra en pantalla.

*Protocolo de comunicación:* El cliente envía los datos en formato operando1,operador,operando2 y el servidor responde con el resultado.

## 🚀 Cómo Ejecutar

### Requisitos Previos
- Python 3.7 o superior instalado en ambas máquinas
- Dos computadoras conectadas en la misma red local
- Puerto 5000 abierto en el firewall del servidor

### Paso 1: Obtener la IP del Servidor
En la máquina servidor, abrir CMD y ejecutar:
bash
ipconfig

Anotar la dirección IPv4 (ejemplo: 192.168.1.10)

### Paso 2: Configurar Firewall (Windows)
En la máquina servidor:
1. Presionar Windows + R, escribir wf.msc y Enter
2. Clic en "Reglas de entrada" → "Nueva regla"
3. Seleccionar "Puerto" → TCP → Puerto específico: 5000
4. "Permitir la conexión" → Siguiente → Marcar todo → Finalizar

### Paso 3: Iniciar el Servidor
En la máquina servidor:
bash
python servidor.py

Debe aparecer: [SERVIDOR] Escuchando en 0.0.0.0:5000

### Paso 4: Ejecutar el Cliente
En la máquina cliente:
bash
python cliente.py

Ingresar:
- IP del servidor (ejemplo: 192.168.1.10)
- Primer número
- Operador (+, -, *, /)
- Segundo número

El resultado se mostrará en pantalla.

## 📡 Operaciones Soportadas
- *Suma:* +
- *Resta:* -
- *Multiplicación:* *
- *División:* /

## 👥 Autores
- Kevin Lorenzo Madrid Neira 
- Erwin Jonner Jaime Lamus

## 📅 Fecha
Octubre 2025
