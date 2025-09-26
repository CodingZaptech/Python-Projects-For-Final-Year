# EmailGenerator.py
# Main runner file for Email Generator project

from EmailGeneratorBackend import EmailGen
import input

def main():
    name, domain = input.get_inputs()
    generator = EmailGen()
    email = generator.create_email(name, domain)
    print("Generated Email:", email)

if __name__ == "__main__":
    main()
