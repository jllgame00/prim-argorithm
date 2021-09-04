INF = 999
adj_mat = [[0, 12, 5, 18, INF, INF, INF],
          [12, 0, INF, 1, 3, INF, INF],
          [5, INF, 0, 17, INF, 2, INF],
          [18, 1, 17, 0, 8, 10, 9],
          [INF, 3, INF, 8, 0, INF, 10],
          [INF, INF, 2, 10, INF, 0, 6],
          [INF, INF, INF, 9, 10, 6, 0]]

node_num = len(adj_mat)
visited = [False] * node_num
distances = [INF] * node_num


def get_min_node(node_num):
    for i in range(node_num):
        if not visited[i]:
            v = i
            break
    for i in range(node_num):
        if not visited[i] and distances[i] < distances[v]:
            v = i

    return v


def prim(start, node_num):
    # distances 배열과 visted 배열 초기화
    for i in range(node_num):
        visited[i] = False
        distances[i] = INF

    # 시작노드의 distance 값을 0으로 초기화
    distances[start] = 0
    for i in range(node_num):
        node = get_min_node(node_num)
        visited[node] = True    # node 를 방문했다 표시

        for j in range(node_num):
            if adj_mat[node][j] != INF:
                if not visited[j] and adj_mat[node][j] < distances[j]:
                    distances[j] = adj_mat[node][j]


print(prim(0, node_num))
print("distances: ", distances)
print("minimum cost: ", sum(distances))