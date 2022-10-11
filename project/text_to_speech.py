import pyttsx3


class text_to_speech:
    """Speeches the text with its aspects: language, gender.
     Firstly, it checks if there is language that is supported by pyttsx3 and gender too.
      In possible ways, pyttsx3 can support 2 gender type(male, female) and 25 languages.
    """
    def __init__(self, language='English', gender='Male'):
        self.engine = pyttsx3.init()
        if self.change_voice(self.engine, language, gender):
            self.language = self.setting_lang(lang=language)
            self.gender = f'VoiceGender{gender}'

    def speech(self, text):
        return self.engine.say(text), self.engine.runAndWait()

    def change_voice(self, engine, lang, gender):
        for voice in engine.getProperty('voices'):
            if voice.languages == [lang] and voice.gender == gender:
                engine.setProperty('voice', voice.id)
                return True

    def setting_lang(self, lang):
        data_lang = {'English': 'en_US', 'Arabic': 'ar_AE', 'Chinese - Simplified': 'zh_CN',
                     'Chinese - Traditional': 'zh_TW', 'Czech': 'cs_CZ', 'Danish': 'da_DK', 'Indonesian': 'in_ID',
                     'Malaysian': 'ms_MY', 'Dutch': 'nl_NL', 'French': 'fr_FR', 'Finnish': 'fi_FI', 'German': 'de_DE',
                     'Italian': 'it_IT', 'Japanese': 'ja_JP', 'Korean': 'ko_KR', 'Norwegian': 'no_NO',
                     'Polish': 'pl_PL', 'Portuguese': 'pt_BR', 'Romanian': 'ro_RO', 'Russian': 'ru_RU',
                     'Spanish': 'es_ES', 'Swedish': 'sv_SE', 'Thai': 'th_TH', 'Filipino': 'tl_PH', 'Turkish': 'tr_TR'}
        try:
            return data_lang[lang]
        except KeyError:
            return data_lang['English']
