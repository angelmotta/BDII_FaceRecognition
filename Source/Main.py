from Extraccion import genCaracteristicas, genCaracPic
from KNNEuclidiano import knnSearchED

resDB = genCaracteristicas()
q_pic = genCaracPic("fotos_test/vizcarraTest.jpg")
result = knnSearchED(resDB, q_pic, 5)
print(result)
for index, score in result:
    print(resDB[index][0])
    print(score)

