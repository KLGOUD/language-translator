from deep_translator import GoogleTranslator

def translate_to_multiple_languages(text, target_languages):
    translations = {}
    for lang in target_languages:
        try:
            translated = GoogleTranslator(source='auto', target=lang).translate(text)
            translations[lang] = translated
        except Exception as e:
            translations[lang] = f"Error: {str(e)}"
    return translations

# Languages: Indian + Foreign
languages = {
    "hi": "Hindi",
    "ta": "Tamil",
    "te": "Telugu",
    "ml": "Malayalam",
    "bn": "Bengali",
    "gu": "Gujarati",
    "kn": "Kannada",
    "mr": "Marathi",
    "ur": "Urdu",
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-CN": "Chinese (Simplified)",
    "ru": "Russian",
    "ar": "Arabic"
}

# Example input
text_to_translate = "Life is beautiful"

results = translate_to_multiple_languages(text_to_translate, target_languages=languages.keys())

# Display results
print(f"\nOriginal Text: {text_to_translate}\n")
for lang_code, translation in results.items():
    print(f"{languages[lang_code]} ({lang_code}): {translation}")


