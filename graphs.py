class Vertex():
    def __init__(self, key):
        self.key = key
        self.color = 'white'
        self.distance = 0
        self.predecessor = None
        self.connectedTo = {}
    def addNeighbor(self, vertTo, weight=0):
        self.connectedTo[vertTo] = weight
    def getNeighbors(self):
        return self.connectedTo.keys()
    def getKey(self):
        return self.key
    def __str__(self):
        return str(self.key) + ' connected to ' + str([x.key for x in self.connectedTo.keys()])
    def getWeight(self, vert):
        return self.connectedTo[vert]
    def setColor(self, color='white'):
        if color in ['white', 'gray', 'black']:
            self.color = color
    def getColor(self):
        return self.color
    def setPredecessor(self, pred=None):
        self.predecessor = pred
    def getPredecessor(self):
        return self.predecessor
    def setDistance(self, d=0):
        self.distance = d
    def getDistance(self):
        return self.distance
    def reset(self):
        self.color = 'white'
        self.distance = 0
        self.predecessor = None

class Graph():
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    def getVertices(self):
        return self.vertList.values()
    def getVertex(self, key):
        if key not in self.vertList.keys():
            return None
        return self.vertList[key]
    # fromVert and toVert are keys and not instances of Vertex()
    def addEdge(self, fromVertKey, toVertKey, weight=0):
        if fromVertKey not in self.vertList.keys():
            fromVert = self.addVertex(fromVertKey)
        if toVertKey not in self.vertList.keys():
           toVert = self.addVertex(toVertKey)
        self.vertList[fromVertKey].addNeighbor(self.vertList[toVertKey])
    def reset(self):
        for i in self.getVertices():
            i.reset()

    def __iter__(self):
        return iter(self.vertList.values())

if __name__ == "__main__":
    a = Graph()
    for i in xrange(6):
        a.addVertex(i)
    a.addEdge(0, 1, 5)
    a.addEdge(0, 5, 2)
    a.addEdge(1, 2, 4)
    a.addEdge(2, 3, 9)
    a.addEdge(3, 4, 7)
    a.addEdge(4, 0, 1)
    a.addEdge(5, 4, 8)
    a.addEdge(5, 2, 1)
    a.addEdge(3, 5, 3)
    for v in a:
        for to in v.getNeighbors():
            print '({0}, {1})'.format(v.getKey(), to.getKey())
