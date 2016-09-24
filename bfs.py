#from graphs import Graph
#from knights_tour import knightsGraph
from queue import Queue
from word_puzzle import create_word_puzzle_graph
from dfs import dfs

def bfs(g, key):
    for v in g:
        q = Queue()
        v.setColor('gray')
        v.setPredecessor()
        if v.getKey() == key:
            return v, True
        q.enqueue(v)
        while not q.isEmpty():
            v = q.dequeue()
            neighbors = v.getNeighbors()
            for i in neighbors:
                if i.getColor() == 'white':
                    i.setPredecessor(v)
                    if i.getKey() == key:
                        return i, True
                    i.setColor('gray')
                    q.enqueue(i)
    return None, False

def displaypath(g, v):
    path = ''
    if v not in g:
        return 'Error: vertex not found'
    if v.getPredecessor() is None:
        return v
    while v.getPredecessor():
        path = str(v.getKey()) + '->' + path
        v = v.getPredecessor()
    print path.strip('->')

if __name__ == '__main__':
    #g = knightsGraph(8)
    g = create_word_puzzle_graph('./testdata/junk')
    print '-----BFS-----'
    for key in ['pool', 'poll', 'sage', 'pull', 'pole']:
        g.reset()
        v, flag = bfs(g, key)
        if v:
            displaypath(g, v)
    print '-----DFS-----'
    paths = []
    for key in ['pool', 'poll', 'sage', 'pull', 'pole']:
        g.reset()
        path = []
        dfs(g.getVertex('fool'), key, path)
        pathstr = ''
        for i in reversed(path):
            pathstr = str(i.getKey()) + '->' + pathstr
        paths.append(pathstr.strip('->'))

