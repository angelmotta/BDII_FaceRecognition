from Extraccion import genCaracteristicas, genCaracPic
from KNNEuclidiano import knnSearchED
from KNNManhattan import knnSearchMD
from RTree import buildRTree
import time


dirFotos = "fotos_n12800"
resDB = genCaracteristicas(dirFotos)
q_pic = genCaracPic("fotos_query/britney_query_001.jpg")
k = 16

"""result = knnSearchED(resDB, q_pic, k)
print(result)
for index, score in result:
    print(resDB[index][0])
    print(score)"""

time1 = time.time()
result = knnSearchMD(resDB, q_pic, k)
time2 = time.time()
print("Busqueda secuencial tomo:", (time2 - time1)*1000.0, "ms")
"""print(result)
for index, score in result:
    print(resDB[index][0])
    print(score)"""

resultado = buildRTree(resDB)
indice = resultado[0]
# print(indice)
time1 = time.time()
hits = list(indice.nearest(tuple(q_pic), k))
time2 = time.time()
print("Busqueda R Tree tomo:", (time2 - time1)*1000.0, "ms")
"""for i in hits:
    print(result[1][i])"""
