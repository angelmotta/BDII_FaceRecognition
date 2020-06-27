import os
import face_recognition


def genCaracteristicas():
    dataDB = []
    dirPics = 'fotos_bd'
    listPics = os.listdir(dirPics)
    for image in listPics:
        print(dirPics + "/" + image)
        q_imagen = face_recognition.load_image_file(dirPics+"/"+image)
        q_imagen_encoding = face_recognition.face_encodings(q_imagen)[0]
        print(q_imagen_encoding)
        dataDB.append((image, q_imagen_encoding))
    return dataDB


def genCaracPic(filePic):
    q_imagen = face_recognition.load_image_file(filePic)
    q_imagen_encoding = face_recognition.face_encodings(q_imagen)[0]
    return q_imagen_encoding
