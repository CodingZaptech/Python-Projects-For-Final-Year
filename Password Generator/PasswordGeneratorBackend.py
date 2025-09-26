# PasswordGeneratorBackend.py
# Backend logic for Password Generator

import random
import string

class PasswordGen:
    def generate(self, length: int) -> str:
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for _ in range(length))
        return password
