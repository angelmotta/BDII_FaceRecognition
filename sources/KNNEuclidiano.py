import heapq


def ED(x, y):
    res = 0
    for i in range(len(x)):
        res += ((x[i] - y[i])**2)
    return res**0.5


def knnSearchED(dataDB, Q, k):
    print("--- KnnSearchED ---")
    result = []
    index = 0
    for row in dataDB:
        d = ED(Q, row[1])
        heapq.heappush(result, (-d, index))
        if len(result) > k:
            heapq.heappop(result)
        index += 1
    result = [(i, -d) for d, i in result]
    result.sort(key=lambda tup: tup[1])
    return result


