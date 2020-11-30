import heapq

def MD(A, B):
    resultado = 0
    for i in range(len(A)):
        resultado = resultado + abs(A[i] - B[i])
    return resultado


def knnSearchMD(data, Q, k):
    print("--- KnnSearchMD ---")
    resultado = []
    index = 0
    for row in data:
        distancia = MD(Q, row[1])
        heapq.heappush(resultado, (-distancia, index))
        if len(resultado) > k:
            heapq.heappop(resultado)
        index += 1
    resultado = [(i, -d) for d, i in resultado]
    resultado.sort(key=lambda tup: tup[1])
    return resultado
