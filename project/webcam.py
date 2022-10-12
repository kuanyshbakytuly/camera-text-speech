import requests
import cv2
import numpy as np
import imutils
import random
from string import ascii_letters
import micro
from text_to_speech import text_to_speech

class Camera:
    """Connects mobile camera to python and take a photo through it.
    To realise the program, it requires IP Adress of camera (you can find it in IP WebCam(PlayMarket)), language,
     and gender.
    """
    def __init__(self, ip, lang='English', gender='Male'):
        self.ip = ip
        self.name = f'{str(np.random.choice(6, 3, p=ascii_letters))}.png'
        self.lang = lang
        self.gender = gender

    def openning_camera(self):
        url = f'https://{self.ip}/shot.jpg'
        while True:
            img_resp = requests.get(url)
            img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
            img = cv2.imdecode(img_arr, -1)
            img = imutils.resize(img, width=1000, height=1800)
            cv2.imshow("camera", img)

            mic = micro.Response(lang='English')
            dialog = 'Say "True" to take a photo!'
            speech = text_to_speech(language=self.lang, gender=self.gender)
            speech.speech(dialog)
            print(dialog)
            if mic.request():
                return self.taking_photo()

        cv2.destroyAllWindows()

    def taking_photo(self):
        url_photo = ""
        response = requests.get(url_photo)
        if response.status_code == 200:
            return response

