# EmailGeneratorBackend.py
# Backend logic for Email Generator

class EmailGen:
    def create_email(self, name: str, domain: str) -> str:
        """
        Creates a simple email address from name and domain.
        :param name: username
        :param domain: domain name
        :return: email address
        """
        username = name.lower().replace(" ", ".")
        return f"{username}@{domain}"
