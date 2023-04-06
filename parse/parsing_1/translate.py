import googletrans

class Translate_word:
    def translate(text):
        translate = googletrans.Translator()
        translate_word = translate.translate(text=text, dest='en')
        return translate_word

