from text_to_speech import text_to_speech
import micro


class microphone():
    """Checks the readiness of microphone and sets connection with users
    """
    def checking_microphone(self):
        program_speech = 'Hello, we need to check microphone. Can you say Hello world?'
        speech = text_to_speech(language='English', gender='Male')
        f1 = micro.Response('en_US')
        result = False
        while not result:
            print(program_speech)
            speech.speech(program_speech)
            answer = f1.request()
            print(answer)
            if answer == "Hello world":
                result = True
        return True

    def checking_language(self):
        if True:
            program_speech = 'What language is your text in?'
            f2 = micro.Response('en_US')
            speech = text_to_speech(language='English', gender='Male')
            result = False
            while not result:
                speech.speech(program_speech)
                text = f2.request()
                print(program_speech)
                print(text)
                if text in ['Afrikaans', 'Albanian', 'Arabic', 'Bengali', 'Bulgarian', 'Catalan, Valencian',
                            'Croatian', 'Czech', 'Danish', 'Dutch, Flemish', 'English', 'Estonian', 'Finnish',
                            'French', 'German', 'Greek, Modern (1453–)', 'Gujarati', 'Hebrew', 'Hindi', 'Hungarian',
                            'Indonesian', 'Italian', 'Japanese', 'Kannada', 'Korean', 'Latvian', 'Lithuanian',
                            'Macedonian', 'Malayalam', 'Marathi', 'Nepali', 'Norwegian', 'Persian', 'Polish',
                            'Portuguese', 'Punjabi, Panjabi', 'Romanian, Moldavian, Moldovan', 'Russian', 'Slovak',
                            'Slovenian', 'Somali', 'Spanish, Castilian', 'Swahili', 'Swedish', 'Tagalog', 'Tamil',
                            'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese', 'Welsh']:
                    result = True
        return text

    def checking_gender(self):
        program_speech = "Which gender's voice?"
        f3 = micro.Response('en_US')
        speech = text_to_speech(language='English', gender='Male')
        result = False
        while not result:
            speech.speech(program_speech)
            text = f3.request()
            print(program_speech)
            print(text)
            if text in ['Male', 'Female', 'Woman', 'Man', "Boy", "Girl"]:
                if text in ['Female', 'Woman']:
                    text = 'Female'
                    result = True
                else:
                    text = 'Male'
                    result = True
        return text
