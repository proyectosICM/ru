import socket
import struct
import crcmod.predefined

def calculate_crc16(data):
    """Calcula CRC16 usando el algoritmo CRC-CCITT (Kermit)."""
    crc16 = crcmod.predefined.Crc('kermit')
    crc16.update(data)
    return crc16.crcValue

def start_server(host="0.0.0.0", port=9527):
    """Inicia un servidor TCP que recibe mensajes estructurados y responde con una confirmación."""
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
                    header = client_socket.recv(2)  # Leer el campo de longitud (2 bytes)
                    if not header:
                        print(f"Client disconnected: {client_address}")
                        break
                    
                    packet_length = struct.unpack("!H", header)[0]  # Desempaquetar la longitud como entero sin signo
                    print(f"Packet length: {packet_length}")

                    data = client_socket.recv(packet_length + 2)  # Leer el resto del paquete (excepto los 2 bytes de longitud)
                    if len(data) < packet_length + 2:
                        print("Incomplete packet received")
                        break
                    
                    imei = data[:8]
                    command_id = data[8]
                    payload = data[9:-2]
                    received_crc = struct.unpack("!H", data[-2:])[0]

                    # Calcular CRC16 del paquete recibido (excepto los últimos 2 bytes del CRC)
                    calculated_crc = calculate_crc16(header + data[:-2])

                    print(f"IMEI: {imei.hex()} | Command ID: {command_id} | Payload: {payload.decode('utf-8')}")
                    print(f"Received CRC: {hex(received_crc)} | Calculated CRC: {hex(calculated_crc)}")

                    if received_crc == calculated_crc:
                        print("CRC check passed. Sending confirmation...")
                        confirmation_message = b'\x00\x02\x01\x00'  # Ejemplo de respuesta estructurada con CRC
                        confirmation_crc = calculate_crc16(confirmation_message[:-2])
                        confirmation_message = confirmation_message[:-2] + struct.pack("!H", confirmation_crc)
                        client_socket.sendall(confirmation_message)
                        print("Confirmation sent.")
                    else:
                        print("CRC check failed.")
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
