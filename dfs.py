from graphs import Graph
from knights_tour import knightsGraph


def dfs(start, key, path):
    if start.getKey() == key:
        return start, True
    found = False
    path.append(start)
    start.setColor('gray')
    neighbors = start.getNeighbors()
    i = 0
    while i < len(neighbors) and not found:
        n = neighbors[i]
        if n.getColor() == 'white':
            n.setPredecessor(start)
            target, found = dfs(n, key, path)
            if found:
                return target, found
        i = i + 1
    if not found:
        # backtrack
        path.pop()
        start.setColor('white')
    return None, found

if __name__ == "__main__":
    path = []
    g = knightsGraph(5)
    dfs(g.getVertex(0), 24, path)
    pathstr = ''
    for i in reversed(path):
        pathstr = str(i.getKey()) + '->' + pathstr
    #print pathstr.strip('->')

