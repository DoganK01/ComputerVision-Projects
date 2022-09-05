import cv2
import face_recognition
from playsound import playsound
from gtts import gTTS
import os
import random
import tkinter as tk

# !! face_distance() = verilen yüzler arasındaki mesafeyi ölçer. Daha sonra bunların indexlerini argmin() ile kaydettiğimiz listeden çekebiliriz. !! 


def face():
    def speak(string):
        tts=gTTS(string )
        rand =random.randint(1,10000)
        file='audio-'+str (rand)+'.mp3'
        tts.save(file)
        playsound(file)
        os.remove(file)

    camera = cv2.VideoCapture(0)
    return_value,image = camera.read()
    cv2.imwrite('yuz_fotografi.jpg',image)
    camera.release()
    cv2.destroyAllWindows()


    DoganPicure = face_recognition.load_image_file("d.jpg")

    DoganYuzKodları = face_recognition.face_encodings(DoganPicture)

    bilinenyuzler = [
        DoganYuzKodları
    ]

    gelenyuz = face_recognition.load_image_file("yuz_fotografi.jpg")

    gelenyuz_kodları = face_recognition.face_encodings(gelenyuz)

    if gelenyuz_kodları == []: # veya if len(face_encodings) == 0:
        speak("found no face")

for yeniyuz in gelenyuz_kodları :
    sonuclar = face_recognition.compare_faces(DoganYuzKodları, gelenyuz_kodları)
    name = ""
    if sonuclar[0]:
        name = "Doğan"
        speak(f" welcome {name} !")
    else:
        print("unknowned person")
def çıkış():
    etiket['text'] = 'EXITING'

    face()
    pencere.after(2000, pencere.destroy)

pencere = tk.Tk()
pencere.geometry("250x250+10+10");






etiket = tk.Label(text='PRESS THE FACE RECOGNITION')
etiket.pack()

düğme = tk.Button(text='Face_recogniton', command=çıkış)
düğme.pack()

pencere.protocol('WM_DELETE_WINDOW', çıkış)

pencere.mainloop()
