from Extraccion import genCaracteristicas, genCaracPic
from KNNEuclidiano import knnSearchED

resDB = genCaracteristicas()
q_pic = genCaracPic("fotos_test/vizcarraTest.jpg")
result = knnSearchED(resDB, q_pic, 5)
print(result)
for index, score in result:
    print(resDB[index][0])
    print(score)

<<<<<<< Updated upstream
=======
q_imagen_encoding = face_recognition.face_encodings(q_imagen)[0]

print(q_imagen_encoding)
>>>>>>> Stashed changes
