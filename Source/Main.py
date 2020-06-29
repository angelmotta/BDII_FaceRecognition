from Extraccion import genCaracteristicas, genCaracPic
from KNNEuclidiano import knnSearchED
from KNNManhattan import knnSearchMD
from RTree import buildRTree


dirFotos = "fotos_bd_2"
resDB = genCaracteristicas(dirFotos)
q_pic = genCaracPic("fotos_query/britney_query_001.jpg")

result = knnSearchED(resDB, q_pic, 16)
print(result)
for index, score in result:
    print(resDB[index][0])
    print(score)

result = knnSearchMD(resDB, q_pic, 16)
print(result)
for index, score in result:
    print(resDB[index][0])
    print(score)

result = buildRTree(resDB)
indice = result[0]
print(indice)
hits = list(indice.nearest(tuple(q_pic), 16))
for i in hits:
    print(result[1][i])
