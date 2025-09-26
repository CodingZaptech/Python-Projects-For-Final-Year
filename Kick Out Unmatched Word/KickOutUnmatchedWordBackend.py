# KickOutUnmatchedWordBackend.py
# Backend logic to remove words not in allowed list

class WordFilter:
    def filter_words(self, sentence: str, valid_words: list) -> str:
        words = sentence.split()
        filtered_words = [word for word in words if word.lower() in valid_words]
        return " ".join(filtered_words)
