import socket
import struct

def calculate_crc16_kermit(data):
    """Calcula el CRC-16 utilizando el algoritmo CRC-CCITT (Kermit)."""
    crc = 0x0000
    polynomial = 0x1021

    for byte in data:
        crc ^= byte << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ polynomial
            else:
                crc <<= 1
            crc &= 0xFFFF  # Asegurarse de que el CRC sea de 16 bits
    return crc

def build_response(command_id, payload_data):
    """
    Construye un mensaje de respuesta según el protocolo:
    Packet length | Command ID | Payload data | CRC16
    """
    # Construir el mensaje sin CRC
    packet_length = 1 + len(payload_data)  # Command ID (1 byte) + Payload
    packet = struct.pack(">H", packet_length)  # Packet length (2 bytes, big-endian)
    packet += struct.pack(">B", command_id)   # Command ID (1 byte)
    packet += payload_data                    # Payload data

    # Calcular el CRC16 del paquete
    crc = calculate_crc16_kermit(packet)
    packet += struct.pack(">H", crc)         # CRC16 (2 bytes, big-endian)

    return packet

def start_server(host="0.0.0.0", port=9527):
    """Inicia un servidor TCP que recibe mensajes y responde según el protocolo."""
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

                        # Construir mensaje de respuesta
                        command_id = 0x01  # Por ejemplo, un comando de confirmación
                        payload_data = b"OK"  # Confirmación simple
                        response = build_response(command_id, payload_data)

                        # Enviar respuesta
                        client_socket.sendall(response)
                        print(f"Sent response: {response.hex()}")
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
