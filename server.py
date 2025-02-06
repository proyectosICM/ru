import socket
import select
import struct

def get_recv_buffer_size(sock):
    """Obtiene el tamaño del buffer de recepción del socket."""
    buffer_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print(f"Receive buffer size: {buffer_size} bytes")
    return buffer_size

def parse_record(data):
    if len(data) < 23:
        print("Invalid record: Header is too short.")
        return None
        
    # Extraer la cabecera del registro (23 bytes)
    header = data[:23]
    
    # Desglosar los campos de la cabecera
    try:
        timestamp, timestamp_extension, priority, longitude, latitude, altitude, angle, satellites, speed, hdop, event_id = struct.unpack('>I B B I I H H B H B', header)
        
        # Convertir longitud y latitud a coordenadas reales
        longitude = longitude / 10000000.0
        latitude = latitude / 10000000.0
        altitude = altitude / 10.0  # Altitud en metros
        angle = angle / 100.0  # Ángulo en grados
        speed = speed / 10.0  # Velocidad en km/h
        hdop = hdop / 10.0  # HDOP

        # Imprimir los valores
        print(f"Timestamp: {timestamp} (Unix time)")
        print(f"Longitude: {longitude}°")
        print(f"Latitude: {latitude}°")
        print(f"Altitude: {altitude} meters")
        print(f"Angle: {angle}°")
        print(f"Satellites: {satellites}")
        print(f"Speed: {speed} km/h")
        print(f"HDOP: {hdop}")
        print(f"Event ID: {event_id}")
    except struct.error as e:
        print(f"Failed to parse record: {e}")

def start_server(host="0.0.0.0", port=9527):
    try:
        print(f"Starting server on {host}:{port}...")
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(5)  # Escucha hasta 5 conexiones simultáneas
        
        print(f"Server listening on {host}:{port}")
        sockets_list = [server_socket]

        while True:
            readable, _, _ = select.select(sockets_list, [], [])
            
            for notified_socket in readable:
                if notified_socket == server_socket:
                    # Nueva conexión
                    client_socket, client_address = server_socket.accept()
                    print(f"Connection from {client_address}")
                    
                    # Mostrar el tamaño del buffer de recepción
                    get_recv_buffer_size(client_socket)
                    
                    # Enviar mensaje de confirmación inicial
                    confirmation_message = b'\x01'
                    client_socket.sendall(confirmation_message)
                    
                    sockets_list.append(client_socket)
                
                else:
                    # Recibir datos del cliente existente
                    try:
                        data = notified_socket.recv(1024)
                        if not data:
                            print(f"Client disconnected: {notified_socket.getpeername()}")
                            sockets_list.remove(notified_socket)
                            notified_socket.close()
                        else:
                            print(f"Received message: {data}")
                            parse_record(data)
                    except Exception as e:
                        print(f"Error receiving data: {e}")
                        sockets_list.remove(notified_socket)
                        notified_socket.close()
    except KeyboardInterrupt:
        print("\nServer shutting down (CTRL+C detected)...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()
        print("Socket closed.")

if __name__ == "__main__":
    start_server()
