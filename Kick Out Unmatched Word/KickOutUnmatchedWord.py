# KickOutUnmatchedWord.py
# Main runner for unmatched word remover

from KickOutUnmatchedWordBackend import WordFilter
import input

def main():
    sentence, valid_words = input.get_inputs()
    filtered = WordFilter().filter_words(sentence, valid_words)
    print("Filtered Sentence:", filtered)

if __name__ == "__main__":
    main()
