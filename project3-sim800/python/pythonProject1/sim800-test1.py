import serial
import time


def send_command(serial_port, command):
    serial_port.write(command.encode('utf-8') + b'\r\n')
    time.sleep(1)
    response = serial_port.read(serial_port.in_waiting).decode('utf-8')
    print(response)


def send_sms(serial_port, phone_number, message):
    # Ensure the SIM800 module is ready
    send_command(serial_port, 'AT')

    # Set the SMS text mode
    send_command(serial_port, 'AT+CMGF=1')

    # Send SMS
    send_command(serial_port, f'AT+CMGS="{phone_number}"')
    send_command(serial_port, message + chr(26))  # Send message and Ctrl+Z


# Configure the serial port
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)  # Replace 'COMx' with your actual COM port

try:
    while True:
        print("1. Send SMS")
        print("2. Exit")
        choice = input("Select an option (1/2): ")

        if choice == '1':
            phone_number = input("Enter phone number: ")
            message = input("Enter message: ")
            send_sms(ser, phone_number, message)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

except KeyboardInterrupt:
    pass

finally:
    # Close the serial port
    ser.close()