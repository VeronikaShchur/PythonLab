from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(str, lang):
    try:
        translation = translator.translate(str, dest=lang)
        return translation.text
    except Exception as e:
        return f"Помилка: {e}"

def LangDetect(txt):
    try:
        detection = translator.detect(txt)
        return f"Detected(lang={detection.lang}, confidence={detection.confidence})"
    except Exception as e:
        return f"Помилка: {e}"

def CodeLang(lang):
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    else:
        for code, name in LANGUAGES.items():
            if name == lang:
                return code
        return "Помилка - не знайдено відповідного коду або назви мови!"

# Приклад
txt = "Доброгo дня. Як справи?"
lang = "en"

print(txt)
print(LangDetect(txt))
print(TransLate(txt, lang))
print(CodeLang(lang))
