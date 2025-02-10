import socket
import select

def process(data):
    print(f"Received message: {data}")
    
    # Extraer los primeros 2 bytes (4 caracteres hexadecimales)
    packet_length_hex = data[:4]
    packet_length = int(packet_length_hex, 16)
    print(f"Packet length = {packet_length} (0x{packet_length_hex})")
    
    # Extraer los siguientes 8 bytes (16 caracteres hexadecimales) para el IMEI
    imei_hex = data[4:20]
    imei = int(imei_hex, 16)
    print(f"IMEI = {imei} (0x{imei_hex})")
    
    # Extraer el Command ID (1 byte = 2 caracteres hexadecimales)
    command_id_hex = data[20:22]
    command_id = int(command_id_hex, 16)
    print(f"Command ID = {command_id} (0x{command_id_hex})")
    
    # Extraer el Data Storage Type (1 byte = 2 caracteres hexadecimales)
    data_storage_type_hex = data[22:24]
    data_storage_type = int(data_storage_type_hex, 16)
    print(f"Data Storage Type = {data_storage_type} (0x{data_storage_type_hex})")
    
    # Extraer el Data Size (4 bytes = 8 caracteres hexadecimales)
    data_size_hex = data[24:32]
    data_size = int(data_size_hex, 16)
    print(f"Data Size = {data_size} (0x{data_size_hex})")
    
    # Extraer el Data Read Timestamp (4 bytes = 8 caracteres hexadecimales)
    data_read_timestamp_hex = data[32:40]
    data_read_timestamp = int(data_read_timestamp_hex, 16)
    print(f"Data Read Timestamp = {data_read_timestamp} (0x{data_read_timestamp_hex})")
    
    # Extraer el Data Period Start (4 bytes = 8 caracteres hexadecimales)
    data_period_start_hex = data[40:48]
    data_period_start = int(data_period_start_hex, 16)
    print(f"Data Period Start = {data_period_start} (0x{data_period_start_hex})")
    
    # Extraer el Data Period End (4 bytes = 8 caracteres hexadecimales)
    data_period_end_hex = data[48:56]
    data_period_end = int(data_period_end_hex, 16)
    print(f"Data Period End = {data_period_end} (0x{data_period_end_hex})")
    
    # Extraer el CRC16 (2 bytes = 4 caracteres hexadecimales)
    crc16_hex = data[56:60]
    crc16 = int(crc16_hex, 16)
    print(f"CRC16 = {crc16} (0x{crc16_hex})")
    
    # Extraer el Packet Index (2 bytes = 4 caracteres hexadecimales)
    packet_index_hex = data[60:64]
    packet_index = int(packet_index_hex, 16)
    print(f"Packet Index = {packet_index} (0x{packet_index_hex})")
    
    # Extraer el segundo CRC16 (2 bytes = 4 caracteres hexadecimales)
    crc16_final_hex = data[64:68]
    crc16_final = int(crc16_final_hex, 16)
    print(f"Final CRC16 = {crc16_final} (0x{crc16_final_hex})")

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
                        process(data.hex())
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
