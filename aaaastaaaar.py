import heapq
counter = 0
visited = {}


def heuristic(i, j):
    return abs(dst[0] - i) + abs(dst[1] - j)


def astar(mat):
    global counter, visited
    counter = 0

    width = len(mat[0])
    height = len(mat)

    # small variation for easier code, state is (coord_tuple, previous, path_cost, heuristic_cost)
    frontier = [(heuristic(src[0], src[1]), (src[0], src[1]), list(), 0, heuristic(src[0], src[1]))]
    heapq.heapify(frontier)
    visited = {}
    state = 0
    path = []

    while len(frontier):
        # get first state (least cost)
        state = heapq.heappop(frontier)

        # goal check
        (i, j) = state[1]
        if (i, j) == (dst[0], dst[1]):
            path = [state[1]] + state[2]
            path.reverse()
            return path
        # set the cost (path is enough since the heuristic won't change)
        visited[(i, j)] = state[3]
        # explore neighbor
        neighbor = list()
        if i > 0 and mat[i - 1][j] > 0:  # top
            neighbor.append((i-1, j))
        if i < height-1 and mat[i + 1][j] > 0:
            neighbor.append((i+1, j))
        if j > 0 and mat[i][j - 1] > 0:
            neighbor.append((i, j-1))
        if j < width-1 and mat[i][j + 1] > 0:
            neighbor.append((i, j+1))

        for n in neighbor:
            next_cost = state[3] + 1
            if n in visited and visited[n] < next_cost:
                continue
            heapq.heappush(frontier, (heuristic(n[0], n[1])+next_cost, n, [state[1]] + state[2], next_cost, heuristic(n[0], n[1])))
            counter += 1

    if state[0] != dst:
        return path


mat = [list(map(int, input().split())) for i in range(20)]
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
src = (19-y1, x1)
dst = (19-y2, x2)

print("\nA* ALGORITHM: \n")
path = astar(mat)

if len(path) != 0:
    print("path is:")
    print(path, "\n")
    print("cost of shortest path is:\t", len(path))
    print("number of expanded node is:\t", counter)

    for x in path:
        mat[x[0]][x[1]] = 2
    mat[src[0]][src[1]] = 3
    mat[dst[0]][dst[1]] = 4
    for row in mat:
        for c in row:
            if c == 1:  # empty
                print(".\t", end=" ")
            if c == 2:  # path
                print("*\t", end=" ")
            if c == 0:  # barrier
                print("#\t", end=" ")
            if c == 3:
                print("S\t", end=" ")
            if c == 4:
                print("E\t", end=" ")
        print()

else:
    print("shortest path doesn't exist")
