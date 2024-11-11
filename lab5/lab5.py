import re
import string
import locale

def clean_word(word):
    return word.strip(string.punctuation)

def detect_language(word):
    if any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in word):
        return 'ukrainian'
    else:
        return 'english'

def process_words(words):
    cleaned_words = [clean_word(word) for word in words if word]

    unique_words = sorted(set(cleaned_words), key=lambda x: (x[0].islower(), x.lower()))

    return unique_words

def main():
    file_path = 'text.txt'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().strip()

            if not text:
                print("The file is empty!")
                return

            sentences = re.split(r'(?<=[.!?])\s+', text)
            first_sentence = sentences[0] if sentences else ""
            print("First sentence:")
            print(first_sentence)

            words = re.findall(r'\b\w+\b', text)

            sorted_words = process_words(words)

            ukrainian_words = [word for word in sorted_words if detect_language(word) == 'ukrainian']
            english_words = [word for word in sorted_words if detect_language(word) == 'english']

            locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')

            print("\nUkrainian words (sorted alphabetically):")
            for word in sorted(ukrainian_words, key=lambda x: (x[0].islower(), locale.strxfrm(x))):
                print(word)

            print("\nEnglish words (sorted alphabetically):")
            for word in sorted(english_words, key=lambda x: (x[0].islower(), locale.strxfrm(x))):
                print(word)

            print(f"\nTotal word count: {len(words)}")

    except FileNotFoundError:
        print(f"File {file_path} not found!")
    except Exception as e:
        print(f"Error reading the file: {e}")

if __name__ == "__main__":
    main()
