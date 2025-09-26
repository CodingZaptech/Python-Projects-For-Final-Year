# MadLibsGeneratorBackend.py
# Backend processing logic for Mad Libs Generator

class MadLibsGenerator:
    def __init__(self):
        # Template with placeholders
        self.template = (
            "Today I went to the {place}. "
            "I saw a {adjective} {noun} jumping up and down in excitement. "
            "It {verb} through the crowd and made everyone laugh."
        )

    def create_story(self, words: dict) -> str:
        """
        Replaces placeholders with user-provided words
        :param words: Dictionary of words provided by the user
        :return: Final story string
        """
        try:
            return self.template.format(**words)
        except KeyError as e:
            return f"Error: Missing input for {e}"
