from deep_translator import GoogleTranslator
tradutor = GoogleTranslator(source="en", target="ru")
text = "I agree"
tr = tradutor.translate(text)
print(tr)
