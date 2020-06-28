import os
import face_recognition


def genCaracteristicas(dirPics):
    print("--- Get Caracteristicas from Pics ---")
    dataDB = []
    listPics = os.listdir(dirPics)
    for image in listPics:
        print(dirPics + "/" + image)
        q_imagen = face_recognition.load_image_file(dirPics+"/"+image)
        q_imagen_encoding = face_recognition.face_encodings(q_imagen)
        if len(q_imagen_encoding) > 0:
            q_imagen_encoding = q_imagen_encoding[0]
            #print(q_imagen_encoding)
            dataDB.append((image, q_imagen_encoding))
        else:
            print("No faces found in the image!")
    return dataDB


def genCaracPic(filePic):
    print("--- Get Caracteristicas from: ", filePic, "----")
    q_imagen = face_recognition.load_image_file(filePic)
    q_imagen_encoding = face_recognition.face_encodings(q_imagen)
    if len(q_imagen_encoding) > 0:
        q_imagen_encoding = q_imagen_encoding[0]
        return q_imagen_encoding
    else:
        print("No faces found in the image!")
        return []
