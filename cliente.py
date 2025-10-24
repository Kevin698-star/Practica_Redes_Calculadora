import socket
import sys

def conectar_servidor(host, puerto, operando1, operador, operando2):
    """
    Establece una conexión TCP con un servidor en la dirección y puerto especificados,
    envía una operación aritmética en formato "operando1,operador,operando2" y
    devuelve la respuesta recibida del servidor.

    Args:
        host (str): Dirección IP del servidor.
        puerto (int): Puerto TCP del servidor.
        operando1 (str): Primer operando de la operación.
        operador (str): Operador aritmético (+, -, *, /).
        operando2 (str): Segundo operando de la operación.

    Returns:
        str | None: Resultado de la operación devuelto por el servidor, o None si ocurre un error.

    Raises:
        ConnectionRefusedError: Si el servidor no acepta la conexión.
        Exception: Para cualquier otro error durante la comunicación.
    """
    # Crear socket TCP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        print(f"\n[CLIENTE] Conectando al servidor {host}:{puerto}...")
        
        # Conectar con el servidor
        cliente_socket.connect((host, puerto))
        print(f"[CLIENTE] Conectado exitosamente")
        
        # Preparar los datos a enviar (formato: "num1,operador,num2")
        mensaje = f"{operando1},{operador},{operando2}"
        print(f"[CLIENTE] Enviando: {operando1} {operador} {operando2}")
        
        # Enviar datos al servidor
        cliente_socket.send(mensaje.encode('utf-8'))
        
        # Recibir respuesta del servidor
        respuesta = cliente_socket.recv(1024).decode('utf-8')
        
        print(f"\n{'='*50}")
        print(f"RESULTADO: {operando1} {operador} {operando2} = {respuesta}")
        print(f"{'='*50}\n")
        
        return respuesta
    
    except ConnectionRefusedError:
        print("[ERROR] No se pudo conectar al servidor. Verifica que esté ejecutándose.")
    except Exception as e:
        print(f"[ERROR] {e}")
    
    finally:
        cliente_socket.close()
        print("[CLIENTE] Conexión cerrada")

def main():
    """
    Punto de entrada del programa. Solicita al usuario los datos de la operación,
    valida el operador y llama a conectar_servidor para realizar la operación remota.
    """
    print("="*50)
    print("  CALCULADORA REMOTA TCP - CLIENTE")
    print("="*50)
    
    # Solicitar IP del servidor
    host = input("\nIngrese la IP del servidor: ").strip()
    if not host:
        host = "127.0.0.1"  # localhost por defecto
    
    # Puerto del servidor
    puerto = 5000
    
    # Solicitar operandos y operador
    try:
        operando1 = input("Ingrese el primer número: ").strip()
        operador = input("Ingrese el operador (+, -, *, /): ").strip()
        operando2 = input("Ingrese el segundo número: ").strip()
        
        # Validar operador
        if operador not in ['+', '-', '*', '/']:
            print("ERROR: Operador no válido. Use +, -, * o /")
            return
        
        # Conectar y enviar
        conectar_servidor(host, puerto, operando1, operador, operando2)
    
    except KeyboardInterrupt:
        print("\n[CLIENTE] Operación cancelada por el usuario")

if __name__ == "__main__":
    main()