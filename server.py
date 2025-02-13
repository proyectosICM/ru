import socket
import select
import struct
from datetime import datetime

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
    print(f"Packet length = {packet_length} (0x{packet_length_hex})")
    
    # Extraer los siguientes 16 bytes (32 caracteres hexadecimales)
    imei_hex = data[4:20]
    imei = int(imei_hex, 16)
    print(f"IMEI = {imei} (0x{imei_hex})")
    
    # Extraer el Command ID (1 byte = 2 caracteres hexadecimales)
    command_id_hex = data[20:22]
    command_id = int(command_id_hex, 16)
    print(f"Command ID = {command_id} (0x{command_id_hex})")

    # Extraer el Payload data (variable)
    # Record left (1 byte = 2 caracteres hexadecimales)
    record_left_hex = data[22:24]
    record_left = int(record_left_hex, 16)
    print(f"Record left = {record_left} (0x{record_left_hex})")
    
    # Number of records (1 byte = 2 caracteres hexadecimales)
    number_records_hex = data[24:26]   
    number_records = int(number_records_hex, 16)
    print(f"Number of records = {number_records} (0x{number_records_hex})")
    
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
    
    
def process3(data):
    packet_length_hex = data[:4]
    packet_length = int(packet_length_hex, 16)
    print(f"Packet length = {packet_length} (0x{packet_length_hex})")
    
    # Extraer los siguientes 16 bytes (32 caracteres hexadecimales)
    imei_hex = data[4:20]
    imei = int(imei_hex, 16)
    print(f"IMEI = {imei} (0x{imei_hex})")
    
    # Extraer el Command ID (1 byte = 2 caracteres hexadecimales)
    command_id_hex = data[20:22]
    command_id = int(command_id_hex, 16)
    print(f"Command ID = {command_id} (0x{command_id_hex})")

    # Extraer el Payload data (variable)
    # Record left (1 byte = 2 caracteres hexadecimales)
    record_left_hex = data[22:24]
    record_left = int(record_left_hex, 16)
    print(f"Record left = {record_left} (0x{record_left_hex})")
    
    # Number of records (1 byte = 2 caracteres hexadecimales)
    number_records_hex = data[24:26]   
    number_records = int(number_records_hex, 16)
    print(f"Number of records = {number_records} (0x{number_records_hex})")
    
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
    
    # Record extension (1 byte = 2 caracteres hexadecimales)
    record_extension_hex = data[38:40]
    record_extension = int(record_extension_hex, 16)
    print(f"Record extension = {record_extension} (0x{record_extension_hex})")
    
    # Longitude (4 bytes = 8 caracteres hexadecimales)
    longitude_hex = data[40:48]
    longitude = int(longitude_hex, 16) / 1e7 
    print(f"Longitude = {longitude} (0x{longitude_hex})")
    
    # Latitude (4 bytes = 8 caracteres hexadecimales)
    latitude_hex = data[48:56]
    latitude = int(latitude_hex, 16) / 1e7  # Convertir a formato decimal estándar
    print(f"Latitude = {latitude:.7f} (0x{latitude_hex})")
    
    # Altitude (2 bytes = 4 caracteres hexadecimales)
    altitude_hex = data[56:60]
    altitude = int(altitude_hex, 16) / 10  # Convertir a metros reales
    print(f"Altitude = {altitude:.1f} m (0x{altitude_hex})")
    
    # Angle (2 bytes = 4 caracteres hexadecimales)
    angle_hex = data[60:64]
    angle = int(angle_hex, 16)
    print(f"Angle = {angle} (0x{angle_hex})")
    
    # Satellites (1 byte = 2 caracteres hexadecimales)
    satellites_hex = data[64:66]
    satellites = int(satellites_hex, 16)
    print(f"Satellites = {satellites} (0x{satellites_hex})")
    
    # Speed (2 bytes = 4 caracteres hexadecimales)
    speed_hex = data[66:70]
    speed = int(speed_hex, 16)
    print(f"Speed = {speed} (0x{speed_hex})")
    
    # HDOP (1 byte = 2 caracteres hexadecimales)
    hdop_hex = data[70:72]
    hdop = int(hdop_hex, 16) / 10  # Convertir a valor real
    print(f"HDOP = {hdop:.1f} (0x{hdop_hex})")
    
    # IO Data caused record  (1 byte = 2 caracteres hexadecimales)
    io_data_record_hex = data[72:74]
    io_data_record = int(io_data_record_hex, 16)
    print(f"IO Data caused record = {io_data_record} (0x{io_data_record_hex})")
    
    # IO Elements 
    
    # No. of IO data 1Byte (1 byte = 2 caracteres hexadecimales) 
    n_of_io_data_hex = data[74:76]
    n_of_io_data = int(io_data_record_hex, 16)
    print(f"No. of IO data 1Byte = {n_of_io_data} (0x{n_of_io_data_hex})")
    
def response_server(data):
    data_response = {} 
    packet_length = 0x00 
    
    comando_id = data.packet_length.hex()  
    payload_data = data.payload.hex()  
    crc16 = data.crc16.hex() 
    
    data_response['comando_id'] = comando_id
    data_response['payload_data'] = payload_data
    data_response['crc16'] = crc16
    
    return data_response
    
def calculate_crc16(data: bytes) -> int:
    """Calcula el CRC16-CCITT (modificado) del mensaje."""
    crc = 0xFFFF
    for byte in data:
        crc ^= byte << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ 0x1021
            else:
                crc <<= 1
            crc &= 0xFFFF
    return crc

def response_server2(data):
    """Construye la respuesta del servidor siguiendo el protocolo Server-to-Device."""
    command_id = 0x01  # Por ejemplo, un Command ID fijo para una respuesta básica
    payload_data = b"ACK"  # Payload de ejemplo (puede variar según tu lógica)

    # Calcular longitud total del paquete (2 bytes para longitud + 1 byte Command ID + tamaño del payload + 2 bytes CRC16)
    packet_length = 1 + len(payload_data) + 2  # No incluye los 2 bytes de la longitud

    # Construir el paquete sin CRC16
    packet = struct.pack(f">H B {len(payload_data)}s", packet_length, command_id, payload_data)

    # Calcular CRC16 y agregarlo al paquete
    crc16 = calculate_crc16(packet).to_bytes(2, byteorder="big")
    full_packet = packet + crc16

    return full_packet
    
    
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
                while True:
                    data = client_socket.recv(1024)
                    if data:
                        received_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        print(f"Received message: {data.hex()}")
                        print(f"Received at: {received_time}")
                        process3(data.hex())
                        confirmation_message = response_server2(data)
                        client_socket.sendall(confirmation_message)
                        print("Confirmation sent, waiting for the next message...")
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
