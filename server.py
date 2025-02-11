import socket
import select

def process(data):
    packet_length_hex = data[:4]
    packet_length = int(packet_length_hex, 16)
    print(f"Packet length = {packet_length}")
    
    # Extraer los siguientes 16 bytes (32 caracteres hexadecimales)
    imei_hex = data[4:20]
    imei = int(imei_hex, 16)
    print(f"IMEI = {imei}")
    
    # Extraer el Command ID (1 byte = 2 caracteres hexadecimales)
    command_id_hex = data[20:22]
    command_id = int(command_id_hex, 16)
    print(f"Command ID = {command_id}")

    # Extraer el Payload data (variable)
    # Record size (1 byte = 2 caracteres hexadecimales)
    record_size_hex = data[22:24]
    record_size = int(record_size_hex, 16)
    print(f"Record size = {record_size}")
    
    # Record left (1 byte = 2 caracteres hexadecimales)
    record_left_hex = data[24:26]
    record_left = int(record_left_hex, 16)
    print(f"Record left = {record_left}")
    
    # Accident records (variable)
    
    # Timestamp (4 bytes = 8 caracteres hexadecimales)
    timestamp_hex = data[26:34]
    timestamp = int(timestamp_hex, 16)
    print(f"Timestamp = {timestamp}")
    
    # Latitude (4 bytes = 8 caracteres hexadecimales)
    latitude_hex = data[34:42]
    latitude = int(latitude_hex, 16) / 1e6  # Convertir a formato decimal estándar
    print(f"Latitude = {latitude:.6f} (0x{latitude_hex})")
    
    # Longitude (4 bytes = 8 caracteres hexadecimales)
    longitude_hex = data[42:50]
    longitude = int(longitude_hex, 16) / 1e6  # Convertir a formato decimal estándar
    print(f"Longitude = {longitude:.6f} (0x{longitude_hex})")
    
    # RPM (2 bytes = 4 caracteres hexadecimales)
    rpm_hex = data[50:54]
    rpm = int(rpm_hex, 16)
    print(f"RPM = {rpm}")
    
    # Speed (1 byte = 2 caracteres hexadecimales)
    speed_hex = data[54:56]
    speed = int(speed_hex, 16)
    print(f"Speed = {speed}")
    
    # Engine state (1 byte = 2 caracteres hexadecimales)
    engine_state_hex = data[56:58]
    engine_state = int(engine_state_hex, 16)
    print(f"Engine state = {engine_state}")
    
    # Brake pedal position (1 byte = 2 caracteres hexadecimales)
    brake_pedal_position_hex = data[58:60]
    brake_pedal_position = int(brake_pedal_position_hex, 16)
    print(f"Brake pedal position = {brake_pedal_position}")
    
    # Acceleration pedal position (1 byte = 2 caracteres hexadecimales)
    acceleration_pedal_position_hex = data[60:62]
    acceleration_pedal_position = int(acceleration_pedal_position_hex, 16)
    print(f"Acceleration pedal position = {acceleration_pedal_position}")
    
    
def process2(data):
    packet_length_hex = data[:4]
    packet_length = int(packet_length_hex, 16)
    print(f"Packet length = {packet_length}")
    
    # Extraer los siguientes 16 bytes (32 caracteres hexadecimales)
    imei_hex = data[4:20]
    imei = int(imei_hex, 16)
    print(f"IMEI = {imei}")
    
    # Extraer el Command ID (1 byte = 2 caracteres hexadecimales)
    command_id_hex = data[20:22]
    command_id = int(command_id_hex, 16)
    print(f"Command ID = {command_id}")

    # Extraer el Payload data (variable)
    # Record size (1 byte = 2 caracteres hexadecimales)
    record_size_hex = data[22:24]
    record_size = int(record_size_hex, 16)
    print(f"Record size = {record_size}")
    
    # Record left (1 byte = 2 caracteres hexadecimales)
    record_left_hex = data[24:26]   
    record_left = int(record_left_hex, 16)
    print(f"Record left = {record_left}")
    
    # Accident records (variable)
    
    # Timestamp (4 bytes = 8 caracteres hexadecimales)
    timestamp_hex = data[26:34]
    timestamp = int(timestamp_hex, 16)
    print(f"Timestamp = {timestamp}")
    
    # Timestamp extension (1 byte = 2 caracteres hexadecimales)
    timestamp_extension_hex = data[34:36]
    timestamp_extension = int(timestamp_extension_hex, 16)
    print(f"Timestamp extension = {timestamp_extension} (0x{timestamp_extension})")
    
    # Priority (1 byte = 2 caracteres hexadecimales)
    priority_hex = data[36:38]
    priority = int(priority_hex, 16)
    print(f"Priority = {priority} (0x{priority_hex})")
    
    # Longitude (4 bytes = 8 caracteres hexadecimales)
    longitude_hex = data[38:46]
    longitude = int(longitude_hex, 16) / 1e6  # Convertir a formato decimal estándar
    print(f"Longitude = {longitude:.6f} (0x{longitude_hex})")
    
    # Latitude (4 bytes = 8 caracteres hexadecimales)
    latitude_hex = data[46:54] 
    latitude = int(latitude_hex, 16) / 1e6  # Convertir a formato decimal estándar
    print(f"Latitude = {latitude:.6f} (0x{latitude_hex})")
    
    # Altitude (2 bytes = 4 caracteres hexadecimales)
    altitude_hex = data[54:58]
    altitude = int(altitude_hex, 16)
    print(f"Altitude = {altitude}")
    
    # Angle (2 bytes = 4 caracteres hexadecimales)
    angle_hex = data[58:62]
    angle = int(angle_hex, 16)
    print(f"Angle = {angle}")
    
    # Satellites (1 byte = 2 caracteres hexadecimales)
    satellites_hex = data[62:64]
    satellites = int(satellites_hex, 16)
    print(f"Satellites = {satellites}")
    
    # Speed (2 bytes = 4 caracteres hexadecimales)
    speed_hex = data[64:68]
    speed = int(speed_hex, 16)
    print(f"Speed = {speed}")
    
    
def start_server(host="0.0.0.0", port=9527):
    """Inicia un servidor TCP que recibe mensajes y envía una confirmación por cada mensaje recibido."""
    try:
        print(f"Starting server on {host}:{port}...")

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(5)

        print(f"Server listening on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            try:
                while True:  # Mantener la conexión abierta para recibir múltiples mensajes
                    data = client_socket.recv(1024)
                    if data:
                        print(f"Received message: {data.hex()}")
                        process2(data.hex())
                        # Enviar mensaje de confirmación
                        confirmation_message = b'OK'
                        client_socket.sendall(confirmation_message)
                        print("Confirmation sent.")
                    else:
                        print(f"Client disconnected: {client_address}")
                        break
            except Exception as e:
                print(f"Error receiving data: {e}")
            finally:
                client_socket.close()
                print(f"Connection closed with {client_address}")

    except KeyboardInterrupt:
        print("\nServer shutting down (CTRL+C detected)...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()
        print("Socket closed.")

if __name__ == "__main__":
    start_server()
