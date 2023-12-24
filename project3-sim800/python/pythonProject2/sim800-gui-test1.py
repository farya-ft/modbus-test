import tkinter as tk
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

def on_button_click():
    label.config(text="Button Clicked!")
    print("hello")
    send_sms(ser, "+491795228587", "hello")

# Create the main window
root = tk.Tk()
root.title("Tkinter Push Button Example")

# Create a label
label = tk.Label(root, text="Click the button!")

# Create a push button
button = tk.Button(root, text="Click me!", command=on_button_click)

# Pack the label and button into the window
label.pack(pady=10)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()