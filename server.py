import socket
import struct

def start_server(host="0.0.0.0", port=9527):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Evitar el error "Address already in use"
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Configuración del SO_LINGER para liberar el puerto inmediatamente después de cerrar el socket.
    linger_struct = struct.pack('ii', 1, 0)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, linger_struct)
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")
        
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            client_socket.close()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server_socket.close()
