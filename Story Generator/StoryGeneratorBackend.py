# StoryGeneratorBackend.py
# Backend logic for Story Generator

class StoryGen:
    def __init__(self):
        self.template = (
            "Once upon a time in {place}, there was a {adjective} {character}. "
            "Every day, {character} loved to {activity}. "
            "One day, a {event} changed everything!"
        )

    def create_story(self, words: dict) -> str:
        try:
            return self.template.format(**words)
        except KeyError as e:
            return f"Error: Missing input for {e}"
