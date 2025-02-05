import socket
import select  # Para monitorear el socket y manejar interrupciones de forma limpia

def start_server(host="0.0.0.0", port=9527):
    try:
        print(f"Starting server on {host}:{port}...")
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(5)  # Escucha hasta 5 conexiones simultáneas
        
        print(f"Server listening on {host}:{port}")
        
        while True:
            readable, _, _ = select.select([server_socket], [], [], 1)  # Espera 1 segundo
            if server_socket in readable:
                client_socket, client_address = server_socket.accept()
                print(f"Connection from {client_address}")
                
                # Leer el mensaje del cliente
                data = client_socket.recv(1024)  # Lee hasta 1024 bytes
                if data:
                    print(f"Received message: {data}")
                    print(f"Size of message: {len(data)} bytes")
                    
                # Enviar el mensaje de confirmación b'\x01'
                confirmation_message = b'\x01'
                print(f"Sending confirmation message: {confirmation_message}")
                client_socket.sendall(confirmation_message)
                
                # Leer la respuesta del cliente después de enviar el mensaje
                response = client_socket.recv(1024)  # Lee hasta 1024 bytes de respuesta
                if response:
                    print(f"Received response: {response}")
                    print(f"Size of response: {len(response)} bytes")
                
                client_socket.close()
    
    except KeyboardInterrupt:
        print("\nServer shutting down (CTRL+C detected)...")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        server_socket.close()
        print("Socket closed.")

if __name__ == "__main__":
    start_server()
