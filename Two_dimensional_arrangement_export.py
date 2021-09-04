INF = 999
h = [[0, 12, 5, 18, INF, INF, INF],
    [12, 0, INF, 1, 3, INF, INF],
    [5, INF, 0, 17, INF, 2, INF],
    [18, 1, 17, 0, 8, 10, 9],
    [INF, 3, INF, 8, 0, INF, 10],
    [INF, INF, 2, 10, INF, 0, 6],
    [INF, INF, INF, 9, 10, 6, 0]]
 
for a, b, c, d, e, f, g in h:
    print(a, b, c, d, e, f, g)