# Plagiarism.py
# Main runner for Plagiarism Checker

from PlagiarismBackend import PlagiarismChecker
import input

def main():
    text1, text2 = input.get_inputs()
    checker = PlagiarismChecker()
    similarity = checker.check_similarity(text1, text2)
    print(f"Similarity: {similarity:.2f}%")

if __name__ == "__main__":
    main()
