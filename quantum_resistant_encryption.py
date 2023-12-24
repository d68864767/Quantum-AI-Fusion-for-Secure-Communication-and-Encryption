```python
# Importing necessary modules
from sympy import randprime
from sympy.ntheory import discrete_log
from sympy.ntheory.residue_ntheory import primitive_root

class QuantumResistantEncryption:
    def __init__(self, key):
        self.key = key
        self.prime = randprime(1 << 20, 1 << 21)  # Generate a large prime number
        self.generator = primitive_root(self.prime)  # Find a primitive root modulo the prime
        self.public_key = pow(self.generator, self.key, self.prime)  # Generate the public key

    def encrypt(self, message):
        # Convert the message to a number
        message_number = int.from_bytes(message.encode(), 'big')

        # Generate a random key for this message
        message_key = randprime(1, self.prime - 1)

        # Calculate the cipher text
        cipher_text = (pow(self.generator, message_key, self.prime),
                       message_number * pow(self.public_key, message_key, self.prime) % self.prime)

        return cipher_text

    def decrypt(self, cipher_text):
        # Extract the cipher text components
        cipher_text1, cipher_text2 = cipher_text

        # Calculate the original message number
        message_number = (cipher_text2 * pow(cipher_text1, self.prime - 1 - self.key, self.prime)) % self.prime

        # Convert the message number back to a string
        message = message_number.to_bytes((message_number.bit_length() + 7) // 8, 'big').decode()

        return message
```
