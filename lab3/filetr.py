import os
import json
import re
from package.module1 import TransLate, LangDetect
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

def load_config(config_path):
    try:
        with open(config_path, 'r') as config_file:
            settings = json.load(config_file)
        return settings
    except Exception as error:
        return f"Error reading config file: {error}"

def evaluate_text(text_content):
    character_count = len(text_content)
    word_count = len(re.findall(r'\w+', text_content))
    sentence_count = len(re.findall(r'[.!?]', text_content)) + text_content.count('\n')

    return character_count, word_count, sentence_count

def text_analysis():
    config_settings = load_config('config.json')
    if isinstance(config_settings, str):
        print(config_settings)
        return

    file_path = config_settings.get('text_file')
    destination_language = config_settings.get('target_language')
    display_mode = config_settings.get('output_mode')
    max_chars = config_settings.get('char_limit')
    max_words = config_settings.get('word_limit')
    max_sentences = config_settings.get('sentence_limit')

    if not os.path.isfile(file_path):
        print(f"File {file_path} not found.")
        return

    try:
        with open(file_path, 'r') as text_file:
            text_content = text_file.read()

        character_count, word_count, sentence_count = evaluate_text(text_content)

        print(f"File name: {file_path}")
        print(f"File size: {os.path.getsize(file_path)} bytes")
        print(f"Number of characters: {character_count}")
        print(f"Number of words: {word_count}")
        print(f"Number of sentences: {sentence_count}")

        detected_language = detect(text_content)
        print(f"Detected language: {detected_language}")

        # Зчитування тексту до виконання умов
        if (character_count > max_chars or word_count > max_words or sentence_count > max_sentences):
            text_content = text_content[:max_chars]

        translated_output = TransLate(text_content, detected_language, destination_language)

        if display_mode == 'screen':
            print(f"Translated text into '{destination_language}':")
            print(translated_output)
        elif display_mode == 'file':
            output_filename = f"{os.path.splitext(file_path)[0]}_{destination_language}.txt"
            try:
                with open(output_filename, 'w') as output_file:
                    output_file.write(translated_output)
                print("Translation saved successfully!")
            except Exception as error:
                print(f"Error writing to file: {error}")
        else:
            print("Invalid output mode specified!")

    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    text_analysis()
