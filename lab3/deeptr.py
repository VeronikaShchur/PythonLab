from package.module2 import TransLate, LangDetect, CodeLang, LanguageList

def language_tests():
    input_text = "Hello, world!"
    source_lang = "en"
    target_lang = "fr"
    translated_output = TransLate(input_text, source_lang, target_lang)
    print(f"Translated text from '{source_lang}' to '{target_lang}': {translated_output}")

    detection_text = "Hola, ¿cómo estás?"
    language_and_confidence = LangDetect(detection_text, set="all")
    print(f"Detected language and confidence: {language_and_confidence}")

    lang_name = CodeLang("es")
    print(f"Language name for code 'es': {lang_name}")

    language_list_result = LanguageList(out="screen", text="Good evening")
    print(f"Language list output: {language_list_result}")

if __name__ == "__main__":
    language_tests()
