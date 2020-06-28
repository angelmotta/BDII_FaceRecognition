from rtree import index


def buildRTree(data):
    idx = index.Index(interleaved=True)
    for row in data:
        idx.insert(row[0], tuple(row[1]))
    return idx
