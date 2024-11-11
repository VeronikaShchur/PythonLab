from package.module1 import TransLate, LangDetect, CodeLang, LanguageList

def translation_program():
    input_text = "Hello, world!"
    source_language = "en"
    target_language = "es"
    translated_result = TransLate(input_text, source_language, target_language)
    print(f"Translated text from '{source_language}' to '{target_language}': {translated_result}")

    text_for_detection = "Bonjour tout le monde!"
    identified_language = LangDetect(text_for_detection, set="lang")
    print(f"Detected language: {identified_language}")

    language_identifier = CodeLang("French")
    print(f"Language code for 'French': {language_identifier}")

    language_output = LanguageList(out="screen", text="Good morning")
    print(f"Language list output: {language_output}")

if __name__ == "__main__":
    translation_program()
