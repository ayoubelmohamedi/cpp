from collections import defaultdict

def dfs(graph, node, current_path, path_sums):
    current_path.append(node)

    if not graph[node]:
        path_sum = sum(current_path)
        path_sums.append(path_sum)
    else:
        for neighbor in graph[node]:
            dfs(graph, neighbor, current_path.copy(), path_sums)
    
t = int(input())
n = int(input())
arr = str(input()).split()
i = 0

times = 0
while (times < t):
    graph = defaultdict(list)

    while (i < n-1):
        d = str(input()).split()
        a , b = int(d[0]), int(d[1])
        graph[arr[a -1]].append(arr[b -1])
        i += 1
    poss_ans = []
    sinks = [set() for _ in range(n - 1)]
    for startnode in graph:
        dfs(graph, startnode, [], poss_ans) 
    print(poss_ans)
    times += 1