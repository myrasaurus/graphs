from graphs import Graph
from traverse_bfs import traverse
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
                    q.enqueue(v)
        curr.setColor('black')

def bfs(y):
    x = y
    path = ''
    while (x.getPredecessor()):
        path = str(x.getKey()) + '->' + path 
        x = x.getPredecessor()
    print path.strip('->')


def create_word_puzzle_graph(fl):
    d = {}
    with open(fl, 'r') as f:
        for word in f:
            word = word[:-1]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if d.has_key(bucket):
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
    g = Graph()
    for start in d.keys():
        wordlist = d[start]
        if len(wordlist) <= 1:
            continue
        for word in wordlist[1:]:
            g.addEdge(wordlist[0], word)
    return g

def print_graph(g):
    for v in g:
        for to in v.getNeighbors():
            print '({0}, {1})'.format(v.getKey(), to.getKey())  

if __name__ == '__main__':
    g = create_word_puzzle_graph('./testdata/junk')
    v = g.getVertex('fool')
    traverse(g, v)
    for vertex in g:
        print "{0}\t{1}\t{2}".format(vertex.getKey(), vertex.getColor(), vertex.getDistance())
    bfs(g.getVertex('sage'))
