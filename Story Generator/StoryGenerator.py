# StoryGenerator.py
# Main runner file for Story Generator project

from StoryGeneratorBackend import StoryGen
import input

def main():
    words = input.get_inputs()
    generator = StoryGen()
    story = generator.create_story(words)
    print("\n--- Generated Story ---\n")
    print(story)

if __name__ == "__main__":
    main()
