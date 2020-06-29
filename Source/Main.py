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

# indice = buildRTree(resDB)
# print(indice)
# hits = list(indice.nearest())
