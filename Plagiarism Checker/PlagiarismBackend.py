# PlagiarismBackend.py
# Backend logic for Plagiarism Checker

import re

class PlagiarismChecker:
    def clean_text(self, text: str) -> list:
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return text.lower().split()

    def check_similarity(self, text1: str, text2: str) -> float:
        words1 = set(self.clean_text(text1))
        words2 = set(self.clean_text(text2))
        if not words1 or not words2:
            return 0.0
        common = words1.intersection(words2)
        total = len(words1.union(words2))
        return (len(common) / total) * 100
