import graphClass
import random

def addRandomVertex(G):
    key = len(G.getVertices()) + 1
    neighbor = random.randint(1, key - 1)
    G.addEdge(key,neighbor)
    EdgesOut(G)
    return G

def randomGenTree(n):
    G = graphClass.Graph()
    for i in range (1,n+1):
        G = addRandomVertex(G)
    return G

def EdgesOut(G):
    output = []
    key = G.vertList
    for x in key:
        for y in key.get(x).adj:
            if x < y.id:
                output.append([x,y.id])
    print(output)
