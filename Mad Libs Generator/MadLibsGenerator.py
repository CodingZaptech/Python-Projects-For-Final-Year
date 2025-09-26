# MadLibsGenerator.py
# Main runner file for Mad Libs Generator project

from MadLibsGeneratorBackend import MadLibsGenerator
import input

def main():
    # Create instance of MadLibsGenerator
    generator = MadLibsGenerator()
    
    # Get inputs from user
    words = input.get_inputs()
    
    # Generate story
    story = generator.create_story(words)
    
    # Display story
    print("\n--- Your Mad Libs Story ---\n")
    print(story)

if __name__ == "__main__":
    main()
