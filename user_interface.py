```python
# Importing necessary modules
import tkinter as tk
from tkinter import messagebox
from quantum_key_distribution import QuantumKeyDistribution
from quantum_resistant_encryption import QuantumResistantEncryption

class UserInterface:
    def __init__(self):
        self.qkd = QuantumKeyDistribution()
        self.qre = QuantumResistantEncryption(self.qkd.get_key())
        self.window = tk.Tk()
        self.window.title("Quantum-AI Fusion for Secure Communication and Encryption")

    def start(self):
        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        # Create input field for message
        self.message_entry = tk.Entry(self.window, width=50)
        self.message_entry.pack()

        # Create send button
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack()

        # Create output field for encrypted message
        self.encrypted_message_label = tk.Label(self.window, text="")
        self.encrypted_message_label.pack()

    def send_message(self):
        # Get the message from the input field
        message = self.message_entry.get()

        # Encrypt the message
        encrypted_message = self.qre.encrypt(message)

        # Display the encrypted message
        self.encrypted_message_label.config(text="Encrypted Message: " + str(encrypted_message))

        # Clear the input field
        self.message_entry.delete(0, 'end')

        # Show a success message
        messagebox.showinfo("Success", "Message sent successfully!")
```
