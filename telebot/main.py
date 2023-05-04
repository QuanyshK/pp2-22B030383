from googletrans import Translator


class Constructor:
    def __init__(self):
        pass

    def text_translator(self, message, to_lang):
        try:
            translator = Translator()
            return translator.translate(text=message, dest=to_lang)
        except Exception as ex:
            return str(ex)


if __name__ == '__main__':
    x = Constructor()
    r = x.text_translator(message="Guitar", to_lang="ru").text
    print(r)