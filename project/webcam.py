import requests
import cv2
import numpy as np
import imutils
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import random
from string import ascii_letters
import micro
from text_to_speech import text_to_speech
# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
'''url = "http://192.168.0.196:8080/shot.jpg"

ser = Service("/Users/kuanyshbakytuly/PycharmProjects/pythonProject4/chromedriver")
chrome_options = Options()
chrome_options.add_experimental_option('w3c', True)
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(service=ser, options=chrome_options, desired_capabilities=d)
driver.get("http://192.168.0.196:8080")
'''
# While loop to continuously fetching data from the Url
'''while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("Android_cam", img)

    # Press Esc key to exit
    if cv2.waitKey(1) == 27 & 0xFF == ord('y'):
        cv2.imwrite('images/c1.png', img)

    taking = True
    if taking:
        el = driver.find_element(By.XPATH, '/html/body/div[6]/div[4]/div[1]/form/div[5]/div/div[1]/a[1]')
        el.click()

        img_file = random.choices([i for i in ascii_letters])
        print(img_file)
        img = driver.find_element(By.XPATH, '//html/body/img')
        src = img.get_attribute('src')
        urllib.request.urlretrieve(src, f"{img_file}.png")

        driver.close()

cv2.destroyAllWindows()
'''

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

