import face_recognition

q_imagen = face_recognition.load_image_file("fotos_test/vizcarraTest.jpg")

q_imagen_encoding = face_recognition.face_encodings(q_imagen)[0]

print(q_imagen_encoding)