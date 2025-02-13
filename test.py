from datetime import datetime

data = "033500000C076B5C208F01011E5268CEF20000196E3A3A0AEF3E934F3E2D780000000007000000005268CEFD0000196E3A3A0AEF3E934F3E2D780000000007000000005268CF080000196E3A3A0AEF3E934F3E2D780000000007000000005268CF130000196E3A3A0AEF3E934F3E2D780000000007000000005268CF1E0000196E3A3A0AEF3E934F3E2D780000000007000000005268CF290000196E3A3A0AEF3E934F3E2D780000000007000000005268CF340000196E3A3A0AEF3E934F3E2D780000000007000000005268CF3F0000196E3A3A0AEF3E934F3E2D780000000007000000005268CF4A0000196E3A3A0AEF3E934F3E2D780000000007000000005268CF550000196E3A3A0AEF3E934F3E2D780000000007000000005268CF600000196E3A3A0AEF3E934F3E2D780000000007000000005268CF6B0000196E3A3A0AEF3E934F3E2D780000000007000000005268CF730000196E36630AEF42CE4F6D0BF40400022208000000005268CF7E0000196E36B60AEF42BE4F6D0BF40000000007000000005268CF890000196E36B60AEF42BE4F6D0BF40000000007000000005268CF940000196E36B60AEF42BE4F6D0BF40000000007000000005268CF9F0000196E36B60AEF42BE4F6D0BF40000000007000000005268CFAA0000196E36B60AEF42BE4F6D0BF40000000007000000005268CFB50000196E36B60AEF42BE4F6D0BF40000000007000000005268CFC00000196E36B60AEF42BE4F6D0BF40000000007000000005268CFCB0000196E36B60AEF42BE4F6D0BF40000000007000000005268CFD60000196E36B60AEF42BE4F6D0BF40000000007000000005268CFD70000196E3C710AEF5EFF4F690BF40400011708000000005268CFE20000196E3B980AEF601A4F690BF40000000007000000005268CFED0000196E3B980AEF601A4F690BF40000000007000000005268CFF80000196E3B980AEF601A4F690BF40000000007000000005268D0030000196E3B980AEF601A4F690BF40000000007000000005268D00E0000196E3B980AEF601A4F690BF40000000007000000005268D0190000196E3B980AEF601A4F690BF40000000007000000005268D0240000196E3B980AEF601A4F690BF400000000070000000046E2"

def process_io_elements(data, start, io_size):
    io_start = start
    io_data_size_map = {1: 4, 2: 6, 4: 10, 8: 18}
    print(f"\n--- IO Data Elements ({io_size} Byte) ---")
    
    # No. of IO data (1 byte = 2 caracteres hexadecimales)
    n_of_io_data_hex = data[io_start:io_start + 2]
    n_of_io_data = int(n_of_io_data_hex, 16)
    print(f"No. of IO data {io_size}Byte = {n_of_io_data} (0x{n_of_io_data_hex})")

    io_start += 2  # Saltar el byte que indica el número de elementos de este tamaño

    # Procesar los elementos IO
    for i in range(n_of_io_data):
        io_id_hex = data[io_start:io_start + 2]                 # ID del IO (1 byte)
        io_value_hex = data[io_start + 2:io_start + io_data_size_map[io_size]]  # Valor del IO
        io_id = int(io_id_hex, 16)
        io_value = int(io_value_hex, 16)
        print(f"  IO Element {i + 1}: ID = {io_id} (0x{io_id_hex}), Value = {io_value} (0x{io_value_hex})")
        io_start += io_data_size_map[io_size]
    
    return io_start
    
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
    readable_date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    print(f"Timestamp = {timestamp} (0x{timestamp_hex}),  Fecha legible = {readable_date}")
    
    # Timestamp extension (1 byte = 2 caracteres hexadecimales)
    timestamp_extension_hex = data[34:36]
    timestamp_extension = int(timestamp_extension_hex, 16)
    print(f"Timestamp extension = {timestamp_extension} (0x{timestamp_extension_hex})")
    
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
    
    io_start = 74
    io_start = process_io_elements(data, io_start, 1)
    io_start = process_io_elements(data, io_start, 2)
    io_start = process_io_elements(data, io_start, 4)
    io_start = process_io_elements(data, io_start, 8)
    
process3(data)