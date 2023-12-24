import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")
    print("hello")

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