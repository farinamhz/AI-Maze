from collections import deque

ROW = 20
COL = 20
di = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ids_cnt = 0


# def a_star():


def bfs(matrix, source, destination):
    global ROW, COL, di
    if matrix[source[0]][source[1]] == 0 or matrix[destination[0]][destination[1]] == 0:
        return -1
    INF = int(1e9)

    dist = [[INF for j in range(COL)] for i in range(ROW)]
    parent = [[(-1, -1) for j in range(COL)] for i in range(ROW)]
    cnt = 0
    dist[source[0]][source[1]] = 0
    q = deque()
    q.append(source)
    while q:
        cur = q.popleft()
        cnt += 1
        if cur == destination:
            return dist[destination[0]][destination[1]], parent, cnt
        for k in range(4):
            nxt = (cur[0] + di[k][0], cur[1] + di[k][1])
            if 0 <= nxt[0] < ROW and 0 <= nxt[1] < COL and matrix[nxt[0]][nxt[1]] == 1 and dist[nxt[0]][nxt[1]] == INF:
                dist[nxt[0]][nxt[1]] = dist[cur[0]][cur[1]] + 1
                parent[nxt[0]][nxt[1]] = cur
                q.append(nxt)
    return -1


dfs_visited = [[False for j in range(20)] for i in range(20)]
dls_parent = [[(-1, -1) for j in range(COL)] for i in range(ROW)]


def ids(cur, dest, limit):
    global ROW, COL, ids_cnt, dfs_visited, dls_parent
    for i in range(limit):
        dfs_visited = [[False for j in range(20)] for i in range(20)]
        dls_parent = [[(-1, -1) for j in range(COL)] for i in range(ROW)]
        if dls(cur, i, dest):
            return i, dls_parent, ids_cnt
    return -1, dls_parent, ids_cnt


def dls(cur, depth, dest):
    global mat, di, ROW, COL, ids_cnt
    dfs_visited[cur[0]][cur[1]] = True
    ids_cnt += 1
    if cur == dest:
        return True
    if depth == 0:
        return False
    for k in range(4):
        nxt = (cur[0] + di[k][0], cur[1] + di[k][1])
        if 0 <= nxt[0] < ROW and 0 <= nxt[1] < COL and mat[nxt[0]][nxt[1]] != 0 and not dfs_visited[nxt[0]][nxt[1]]:
            if dls(nxt, depth-1, dest):
                dls_parent[nxt[0]][nxt[1]] = cur
                return True
    return False


mat = [list(map(int, input().split())) for i in range(20)]
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
for row in mat:
    for c in row:
        if c == 1:
            print('.\t', end=' ')
        else:
            print('#\t', end=' ')
    print()

src = (19-y1, x1)
dst = (19-y2, x2)
print("source is:\t", (x1, y1), ",\t", "destination is:\t", (x2, y2))

print("\nBFS ALGORITHM: ")
distance, parent_matrix, counter = bfs(mat, src, dst)
temp = (dst[0], dst[1])
# != source
path_list = []
while temp != (-1, -1):
    path_list.append(temp)
    temp = parent_matrix[temp[0]][temp[1]]

if distance != -1:
    print("path is:")
    for i in reversed(range(len(path_list))):
        print((path_list[i][1], 19-path_list[i][0]), end=" ")  # 1 has x and 0 has y
    print()
    print("cost of shortest path is:\t", distance)
    print("number of expanded node is:\t", counter)

    for x in path_list:
        mat[x[0]][x[1]] = 2
    for row in mat:
        for c in row:
            if c == 1:  # empty
                print(".\t", end=" ")
            if c == 2:  # path
                print("*\t", end=" ")
            if c == 0:  # barrier
                print("#\t", end=" ")
        print()

else:
    print("shortest path doesn't exist")


# for x in path_list:
#     mat[x[0]][x[1]] = 1

print("\nIDS ALGORITHM: ")
ids_distance, ids_parent_matrix, ids_counter = ids(src, dst, ROW * COL)
temp = (dst[0], dst[1])
# != source
ids_path_list = []
while temp != (-1, -1):
    ids_path_list.append(temp)
    temp = ids_parent_matrix[temp[0]][temp[1]]

if ids_distance != -1:
    print("path is:")
    for i in reversed(range(len(ids_path_list))):
        print((ids_path_list[i][1], 19-ids_path_list[i][0]), end=" ")
    print()
    print("cost of shortest path is:\t", ids_distance)
    print("number of expanded node is:\t", ids_counter)

    for x in ids_path_list:
        mat[x[0]][x[1]] = 3
    for row in mat:
        for c in row:
            if c == 1 or c == 2:  # empty
                print(".\t", end=" ")
            if c == 3:  # path
                print("*\t", end=" ")
            if c == 0:  # barrier
                print("#\t", end=" ")
        print()

else:
    print("shortest path doesn't exist")

