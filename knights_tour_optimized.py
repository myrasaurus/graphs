from graphs import Graph

def validPos(pos, board_size):
    if pos < 0 or pos >= board_size:
        return False
    return True

def getNormalizedPos(x, y, board_size):
    return (x * board_size) + y

def getPossiblePositions(posX, posY, board_size):
    pos_offsets = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1, 2), (-2, 1)]
    newPosList = []
    for i in pos_offsets:
        newX = posX + i[0]
        newY = posY + i[1]
        if validPos(newX, board_size) and validPos(newY, board_size):
            newPosList.append(getNormalizedPos(newX, newY, board_size))
    return newPosList

def knightsGraph(board_size = 8):
    g = Graph()
    for row in range(board_size):
        for col in range(board_size):
            currPos = getNormalizedPos(row, col, board_size)
            newPos = getPossiblePositions(row, col, board_size)
            for pos in newPos:
                g.addEdge(currPos, pos)
    return g

def getOrderedNeighbors(v):
    neighbors = v.getNeighbors()
    l = []
    for n in neighbors:
        if n.getColor() == 'white':
            nn = n.getNeighbors()
            l.append((len(nn), n))
    l.sort(key = lambda x: x[0])
    newList = [y[1] for y in l]
    return newList

def knightsTour(n, v, path, limit):
    """Solve the knights tour problem
        Args:
        n: Depth of the current path
        v: current vertex to be explored
        path: path of explored vertices so far
        limit: number of steps in the knight's tour
               ex: limit = 63 for a 8x8 board
    """
    if n == limit:
        return True
    nlist = getOrderedNeighbors(v)
    v.setColor('gray')
    path.append(v)
    done = False
    i = 0
    while i < len(nlist) and not done:
        nlist_item = nlist[i]
        if nlist_item.getColor() == 'white':
            done = knightsTour(n+1, nlist_item, path, limit)
        i = i + 1
    if done is False:
        # backtrack here
        path.pop()
        v.setColor('white')
    return done

f = knightsGraph(8)
for i in f:
    print i

path = []
knightsTour(0, f.getVertex(0), path, 63)
pathstr = ''
for i in reversed(path):
    pathstr = str(i.getKey()) + '->' + pathstr
print pathstr.strip('->')
