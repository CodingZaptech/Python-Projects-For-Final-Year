# PasswordGenerator.py
# Main runner file for Password Generator project

from PasswordGeneratorBackend import PasswordGen
import input

def main():
    length = input.get_inputs()
    generator = PasswordGen()
    password = generator.generate(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
