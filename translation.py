from googletrans import Translator
import googletrans
def eng_to_urdu(Text):
    translator = Translator()
    result = translator.translate(str(Text),dest='ur')
    return result.text

def languages():
    return googletrans.LANGUAGES


# print(list(googletrans.LANGUAGES.keys()))