# This file contains some specific graphs

import graphClass
# P is the Petersen graph
P = graphClass.Graph()
for i in range(1,11):
    P.addVertex(i)
p = P.vertList[1]
P.addEdge(1,2)
P.addEdge(1,5)
P.addEdge(1,6)
P.addEdge(2,3)
P.addEdge(2,7)
P.addEdge(3,4)
P.addEdge(3,8)
P.addEdge(4,5)
P.addEdge(4,9)
P.addEdge(5,10)
P.addEdge(6,8)
P.addEdge(6,9)
P.addEdge(7,9)
P.addEdge(7,10)
P.addEdge(8,10)

# prism3 is the 3-prism graph
prism3 = graphClass.Graph()
for i in range(1,7):
    prism3.addVertex(i)
prism3vert = prism3.vertList[1]
prism3.addEdge(1,2)
prism3.addEdge(1,3)
prism3.addEdge(1,5)
prism3.addEdge(2,3)
prism3.addEdge(2,6)
prism3.addEdge(3,4)
prism3.addEdge(4,5)
prism3.addEdge(4,6)
prism3.addEdge(5,6)


G = graphClass.Graph()
for i in range(1,16):
    G.addVertex(i)
G.addEdge(1,2)
G.addEdge(1,3)
G.addEdge(1,4)
G.addEdge(2,3)
G.addEdge(2,5)
G.addEdge(3,4)
G.addEdge(4,5)
G.addEdge(5,6)
G.addEdge(6,7)
G.addEdge(6,12)
G.addEdge(7,8)
G.addEdge(7,10)
G.addEdge(8,9)
G.addEdge(8,11)
G.addEdge(9,10)
G.addEdge(9,11)
G.addEdge(10,11)
G.addEdge(12,13)
G.addEdge(12,15)
G.addEdge(13,14)
G.addEdge(13,16)
G.addEdge(14,15)
G.addEdge(14,16)
G.addEdge(15,16)


# N is a graph
N = graphClass.Graph()
for i in range(1,11):
    N.addVertex(i)
n = N.vertList[1]
N.addEdge(1,6)
N.addEdge(1,9)
N.addEdge(1,10)
N.addEdge(2,10)
N.addEdge(3,4)
N.addEdge(4,6)
N.addEdge(4,8)
N.addEdge(4,10)
N.addEdge(5,10)
N.addEdge(6,7)
N.addEdge(6,9)

# B is a full, complete binary tree of height 3 with 15 vertices
B = graphClass.Graph()
for i in range(1,16):
    B.addVertex(i)
b = B.vertList[1]
B.addEdge(1,2)
B.addEdge(1,3)
B.addEdge(2,4)
B.addEdge(2,5)
B.addEdge(3,6)
B.addEdge(3,7)
B.addEdge(4,8)
B.addEdge(4,9)
B.addEdge(5,10)
B.addEdge(5,11)
B.addEdge(6,12)
B.addEdge(6,13)
B.addEdge(7,14)
B.addEdge(7,15)
