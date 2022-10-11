import numpy as np
import pytesseract
import cv2
from langdetect import detect_langs
from text_to_speech import text_to_speech
import Dialog
from webcam import Camera

def convert_to_array(image):
    """Thresholds and separate the foreground from the background
    to conveniently predict the text"""

    im_pattern = np.asarray(image)
    grey = cv2.cvtColor(im_pattern, cv2.COLOR_BGR2GRAY)
    result = cv2.threshold(src=grey, thresh=0, maxval=255, type=cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)[1]
    return result


def language_from_detect_langs(lang):
    '''The dataset of languages in the types pf ISO 639_1
     https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
     https://pypi.org/project/langdetect/'''
    dataset = {'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic', 'bn': 'Bengali', 'bg': 'Bulgarian',
               'ca': 'Catalan, Valencian', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch, Flemish',
               'en': 'English', 'et': 'Estonian', 'fi': 'Finnish', 'fr': 'French', 'de': 'German',
               'el': 'Greek, Modern (1453–)', 'gu': 'Gujarati', 'he': 'Hebrew', 'hi': 'Hindi', 'hu': 'Hungarian',
               'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada', 'ko': 'Korean', 'lv': 'Latvian',
               'lt': 'Lithuanian', 'mk': 'Macedonian', 'ml': 'Malayalam', 'mr': 'Marathi', 'ne': 'Nepali',
               'no': 'Norwegian', 'fa': 'Persian', 'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi, Panjabi',
               'ro': 'Romanian, Moldavian, Moldovan', 'ru': 'Russian', 'sk': 'Slovak', 'sl': 'Slovenian',
               'so': 'Somali', 'es': 'Spanish, Castilian', 'sw': 'Swahili', 'sv': 'Swedish', 'tl': 'Tagalog',
               'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu',
               'vi': 'Vietnamese', 'cy': 'Welsh'}

    return dataset[lang]


def language_from_tesseract(lang):
    """The dataset of languages available to predict with tesseract
    https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html
    """
    dataset = {'Afrikaans': 'afr', 'Amharic': 'amh', 'Arabic': 'ara', 'Assamese': 'asm', 'Azerbaijani': 'aze',
               'Azerbaijani - Cyrilic': 'aze_cyrl', 'Belarusian': 'bel', 'Bengali': 'ben', 'Tibetan': 'bod',
               'Bosnian': 'bos', 'Breton': 'bre', 'Bulgarian': 'bul', 'Catalan; Valencian': 'cat', 'Cebuano': 'ceb',
               'Czech': 'ces', 'Chinese - Simplified': 'chi_sim', 'Chinese - Traditional': 'chi_tra', 'Cherokee': 'chr',
               'Corsican': 'cos', 'Welsh': 'cym', 'Danish': 'dan', 'Danish - Fraktur (contrib)': 'dan_frak',
               'German': 'deu', 'German - Fraktur (contrib)': 'deu_frak', 'Dzongkha': 'dzo',
               'Greek, Modern (1453-)': 'ell', 'English': 'eng', 'English, Middle (1100-1500)': 'enm',
               'Esperanto': 'epo', 'Math / equation detection module': 'equ', 'Estonian': 'est', 'Basque': 'eus',
               'Faroese': 'fao', 'Persian': 'fas', 'Filipino (old - Tagalog)': 'fil', 'Finnish': 'fin', 'French': 'fra',
               'German - Fraktur': 'frk', 'French, Middle (ca.1400-1600)': 'frm', 'Western Frisian': 'fry',
               'Scottish Gaelic': 'gla', 'Irish': 'gle', 'Galician': 'glg', 'Greek, Ancient (to 1453) (contrib)': 'grc',
               'Gujarati': 'guj', 'Haitian; Haitian Creole': 'hat', 'Hebrew': 'heb', 'Hindi': 'hin', 'Croatian': 'hrv',
               'Hungarian': 'hun', 'Armenian': 'hye', 'Inuktitut': 'iku', 'Indonesian': 'ind', 'Icelandic': 'isl',
               'Italian': 'ita', 'Italian - Old': 'ita_old', 'Javanese': 'jav', 'Japanese': 'jpn', 'Kannada': 'kan',
               'Georgian': 'kat', 'Georgian - Old': 'kat_old', 'Kazakh': 'kaz', 'Central Khmer': 'khm',
               'Kirghiz; Kyrgyz': 'kir', 'Kurmanji (Kurdish - Latin Script)': 'kmr', 'Korean': 'kor',
               'Korean (vertical)': 'kor_vert', 'Kurdish (Arabic Script)': 'kur', 'Lao': 'lao', 'Latin': 'lat',
               'Latvian': 'lav', 'Lithuanian': 'lit', 'Luxembourgish': 'ltz', 'Malayalam': 'mal', 'Marathi': 'mar',
               'Macedonian': 'mkd', 'Maltese': 'mlt', 'Mongolian': 'mon', 'Maori': 'mri', 'Malay': 'msa',
               'Burmese': 'mya', 'Nepali': 'nep', 'Dutch; Flemish': 'nld', 'Norwegian': 'nor',
               'Occitan (post 1500)': 'oci', 'Oriya': 'ori', 'Orientation and script detection module': 'osd',
               'Panjabi; Punjabi': 'pan', 'Polish': 'pol', 'Portuguese': 'por', 'Pushto; Pashto': 'pus',
               'Quechua': 'que', 'Romanian; Moldavian; Moldovan': 'ron', 'Russian': 'rus', 'Sanskrit': 'san',
               'Sinhala; Sinhalese': 'sin', 'Slovak': 'slk', 'Slovak - Fraktur (contrib)': 'slk_frak',
               'Slovenian': 'slv', 'Sindhi': 'snd', 'Spanish; Castilian': 'spa', 'Spanish; Castilian - Old': 'spa_old',
               'Albanian': 'sqi', 'Serbian': 'srp', 'Serbian - Latin': 'srp_latn', 'Sundanese': 'sun', 'Swahili': 'swa',
               'Swedish': 'swe', 'Syriac': 'syr', 'Tamil': 'tam', 'Tatar': 'tat', 'Telugu': 'tel', 'Tajik': 'tgk',
               'Tagalog (new - Filipino)': 'tgl', 'Thai': 'tha', 'Tigrinya': 'tir', 'Tonga': 'ton', 'Turkish': 'tur',
               'Uighur; Uyghur': 'uig', 'Ukrainian': 'ukr', 'Urdu': 'urd', 'Uzbek': 'uzb',
               'Uzbek - Cyrilic': 'uzb_cyrl', 'Vietnamese': 'vie', 'Yiddish': 'yid', 'Yoruba': 'yor'}
    return dataset[lang]

# path/reference to image
'''image_path = "/Users/kuanyshbakytuly/Desktop/Screen Shot 2022-10-10 at 17.25.37.png"
image = cv2.imread(image_path)
image_array = convert_to_array(image)'''

dialog = Dialog.microphone()

# question language
lang = dialog.checking_language()

# question gender
gender = dialog.checking_gender()

#taking a photo from mobile camera with IP Adress
camera = Camera(ip="", lang=lang, gender=gender)
taking_photo = camera.openning_camera()
image = cv2.imread(taking_photo)
image_array = convert_to_array(image)


# predicting with setup language: English
predict = pytesseract.image_to_string(image_array, lang=language_from_tesseract(lang))

# predicting language in the image
languages = detect_langs(predict)
predicted_language = str(languages[0])[:2]


pre = text_to_speech(language=language_from_detect_langs(predicted_language), gender=gender)
pre.speech(predict)
print('success')