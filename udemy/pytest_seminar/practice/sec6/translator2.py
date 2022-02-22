from googletrans import Translator

class GoogleTranslator():
    def __init__(self):
        self.translator = Translator()

    def get_language_id(self, language_name):
        languages = {
            '日本語': 'ja',
            '英語': 'en',
            '中国語': 'zh-cn',
            'フランス語': 'fr',
            'ドイツ語': 'de',
            'ヒンディー語': 'hi',
            'イタリア語': 'it',
            '韓国語': 'ko',
            'ロシア語': 'ru',
            'スペイン語': 'es'
        }
        return languages[language_name]

    def convert(self, text_original, language_original_name, language_translated_name):
        pass
