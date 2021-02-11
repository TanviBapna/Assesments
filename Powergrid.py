def find(parents, node):
    if parents[node] == -1:
        return node
    return find(parents, parents[node])


def union(parents, rank, x, y):
    xRoot, yRoot = find(parents, x), find(parents, y)
    if rank[xRoot] > rank[yRoot]:
        parents[yRoot] = xRoot
    elif rank[yRoot] > rank[xRoot]:
        parents[xRoot] = yRoot
    else:
        parents[yRoot] = xRoot
        rank[xRoot] += 1



def gridAnalysis(n, connections):
    lookup = {chr((ord('A') + i)) :i for i in range(n)}
    parents = [-1] * n
    rank = [0] * n
    numEdges, i = 0, 0
    mst = []

    connections.sort(key=lambda c:c[2])
    while numEdges < n - 1 and i < len(connections):
        sender, reciever, cost = connections[i]
        if find(parents, lookup[sender]) != find(parents, lookup[reciever]):
            union(parents, rank, lookup[sender], lookup[reciever])
            mst.append(connections[i])
            numEdges += 1
        i += 1
    return mst if len(mst) == n - 1 else "No MST can be made"
num = 5
connection =[['A','B',1],
            ['B','C',4], 
            ['B','D',6],
            ['D','E',5],
            ['C','E',1]]
print(gridAnalysis(num,connection))