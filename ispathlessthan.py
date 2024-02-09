


graph = {2: [3,4],3: [6],4: [5]}

def dfs(graph, node , curr_path,all_path):
    
    curr_path.append(node)

    if not graph[node]:
        all_path.append(curr_path)
    else:
        for neighbor in graph[node]:
            dfs(graph,neighbor,path.copy())

path = []
dfs(graph,graph[0],path)