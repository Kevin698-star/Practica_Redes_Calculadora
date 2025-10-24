import socket
import sys

def realizar_operacion(operando1, operando2, operador):
    """
    Esta función toma dos operandos y un operador, realiza la operación matemática correspondiente
    y devuelve el resultado. Si hay errores en los datos, devuelve un mensaje de error.
    """
    try:
        # Convertimos los operandos a números flotantes
        num1 = float(operando1)
        num2 = float(operando2)
        
        # Evaluamos el operador y realizamos la operación correspondiente
        if operador == '+':
            return num1 + num2
        elif operador == '-':
            return num1 - num2
        elif operador == '*':
            return num1 * num2
        elif operador == '/':
            # Validamos que no se divida por cero
            if num2 == 0:
                return "ERROR: División por cero"
            return num1 / num2
        else:
            # Si el operador no es válido
            return "ERROR: Operador no válido"
    except ValueError:
        # Si los operandos no pueden convertirse a número
        return "ERROR: Operandos no válidos"

def iniciar_servidor(host='0.0.0.0', puerto=5000):
    """
    Esta función inicia un servidor TCP que escucha conexiones entrantes en el puerto especificado.
    Al recibir datos, los interpreta como una operación matemática, la ejecuta y devuelve el resultado.
    """
    # Creamos el socket TCP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Permitimos reutilizar el puerto en caso de reinicio rápido del servidor
    servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        # Asociamos el socket al host y puerto
        servidor_socket.bind((host, puerto))
        
        # Ponemos el socket en modo escucha, permitiendo hasta 5 conexiones en cola
        servidor_socket.listen(5)
        
        print(f"[SERVIDOR] Iniciado en {host}:{puerto}")
        print(f"[SERVIDOR] Esperando conexiones de clientes...")
        
        while True:
            # Aceptamos una conexión entrante
            cliente_socket, direccion_cliente = servidor_socket.accept()
            print(f"\n[CONEXIÓN] Cliente conectado desde {direccion_cliente}")
            
            try:
                # Recibimos los datos enviados por el cliente (esperamos formato: "num1,operador,num2")
                datos = cliente_socket.recv(1024).decode('utf-8')
                
                if datos:
                    print(f"[RECIBIDO] {datos}")
                    
                    # Dividimos el string recibido en partes
                    partes = datos.split(',')
                    
                    if len(partes) == 3:
                        operando1, operador, operando2 = partes
                        
                        # Ejecutamos la operación solicitada
                        resultado = realizar_operacion(operando1, operando2, operador)
                        print(f"[RESULTADO] {resultado}")
                        
                        # Enviamos el resultado de vuelta al cliente
                        cliente_socket.send(str(resultado).encode('utf-8'))
                    else:
                        # Si el formato no es correcto, enviamos un mensaje de error
                        cliente_socket.send("ERROR: Formato incorrecto".encode('utf-8'))
            
            except Exception as e:
                # Si ocurre algún error durante el procesamiento, lo reportamos
                print(f"[ERROR] {e}")
                cliente_socket.send(f"ERROR: {str(e)}".encode('utf-8'))
            
            finally:
                # Cerramos la conexión con el cliente
                cliente_socket.close()
                print(f"[DESCONEXIÓN] Cliente {direccion_cliente} desconectado")
    
    except KeyboardInterrupt:
        # Si el usuario interrumpe el servidor (Ctrl+C), lo notificamos
        print("\n[SERVIDOR] Detenido por el usuario")
    
    finally:
        # Cerramos el socket del servidor al finalizar
        servidor_socket.close()
        print("[SERVIDOR] Socket cerrado")

# Punto de entrada principal del script
if __name__ == "__main__":
    iniciar_servidor()