from googletrans import Translator

translator = Translator()


def translate(text, destination = 'en'):
    result = translator.translate(text, dest=destination).text
    
    return str(result)
