# CheckTheURL.py
# Main runner file for URL Checker

from CheckTheURLBackend import URLChecker
import input

def main():
    url = input.get_inputs()
    checker = URLChecker()
    checker.check_url(url)

if __name__ == "__main__":
    main()
