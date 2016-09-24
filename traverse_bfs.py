from graphs import Graph, Vertex
from queue import Queue

def traverse(g, start):
    start.setColor('gray')
    start.setDistance(0)
    start.setPredecessor()
    q = Queue()
    q.enqueue(start)
    while not q.isEmpty():
        curr = q.dequeue()
        if curr.getColor() is 'gray':
            for v in curr.getNeighbors():
                if v.getColor() is 'white':
                    v.setColor('gray')
                    v.setDistance(curr.getDistance()+1)
                    v.setPredecessor(curr)
        curr.setColor('black')
    
        
