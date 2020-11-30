from rtree import index


def toArray(row):
    temp = []
    flag = False
    for i in range(2):
        for a in row:
            if flag:
                temp.append(a)
            else:
                temp.append(a)
        flag = True
    return temp


def buildRTree(data):
    dict = {}
    prop = index.Property()
    prop.dimension = 128
    idx128 = index.Index(properties=prop, interleaved=True)
    count = 0
    for row in data:
        dict[count] = row[0]
        idx128.insert(count, tuple(toArray(row[1])))
        count += 1
    return [idx128, dict]
