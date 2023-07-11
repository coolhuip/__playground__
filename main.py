import tkinter as tk

def button_click():
    label.config(text="Button clicked!")

# Create the main window
window = tk.Tk()

# Create a label widget
label = tk.Label(window, text="Hello, GUI!")

# Create a button widget
button = tk.Button(window, text="Click me!", command=button_click)

# Pack the label and button widgets into the window
label.pack()
button.pack()

# Start the GUI event loop
window.mainloop()
