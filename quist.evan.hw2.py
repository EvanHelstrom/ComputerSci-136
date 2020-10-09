import graphClass
import random

def addRandomVertex(G):
    neighbor = 5
    key = len(G.getVertices()) + 1
    neighbor = random.randint(1, key - 1)
    neighbor = G.vertList[neighbor]
    vertex = G.addVertex(key)
    vertex.addNeighbor(neighbor)
    print(G)

def randomGenTree(n):
    G = graphClass.Graph()
    for i in range (1,n+1):
        G = addRandomVertex(G)
    print(G)

def EdgesOut(G):
    vertList = G.getVertices()
    dictionary = {}
    for item in vertList:
        friends = []
        for each in item.adj:
            friends.append(each.id)
        dictionary[item.id] = friends
    output = []
    for item in dictionary:
        for each in dictionary[item]:
            thing = [item,each]
            thing.sort()
            if thing not in output:
                output.append(thing)
    print(output)
