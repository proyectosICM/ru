import socket
import select
import struct

def parse_record(data):
    if len(data) < 23:
        print("Invalid record: Header is too short.")
        return None
    
    # Extraer la cabecera del registro (23 bytes)
    header = data[:23]
    
    # Desglosar los campos de la cabecera
    timestamp, timestamp_extension, priority, longitude, latitude, altitude, angle, satellites, speed, hdop, event_id = struct.unpack('>I B B I I H H B H B', header)
    
    # Convertir los valores a sus formas legibles
    timestamp = timestamp  # Ya está en formato Unix
    timestamp_extension = timestamp_extension
    priority = "High" if priority == 1 else "Low"
    
    # Convertir longitud y latitud a coordenadas reales
    longitude = longitude / 10000000.0
    latitude = latitude / 10000000.0
    
    altitude = altitude / 10.0  # Altitud en metros
    angle = angle / 100.0  # Ángulo en grados
    speed = speed / 10.0  # Velocidad en km/h
    hdop = hdop / 10.0  # HDOP
    
    # Imprimir los valores
    print(f"Timestamp: {timestamp} (Unix time)")
    print(f"Timestamp Extension: {timestamp_extension}")
    print(f"Priority: {priority}")
    print(f"Longitude: {longitude}°")
    print(f"Latitude: {latitude}°")
    print(f"Altitude: {altitude} meters")
    print(f"Angle: {angle}°")
    print(f"Satellites: {satellites}")
    print(f"Speed: {speed} km/h")
    print(f"HDOP: {hdop}")
    print(f"Event ID: {event_id}")
    
    # El cuerpo del mensaje es variable, si tienes más datos en 'data', deberías procesarlos aquí.

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
                    
                    # Procesar el mensaje y convertirlo a formato legible
                    parse_record(data)
                    
                # Responder con el mensaje de confirmación
                confirmation_message = b'\x01'
                client_socket.sendall(confirmation_message)
                
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
