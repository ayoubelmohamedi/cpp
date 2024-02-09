
from collections import defaultdict

#get sum of each path
#WISH to be done, return a list where each item is a list of fix suggestes
def dfs(graph, node, current_path, path_sums):
    current_path.append(node)
    #leaf
    print("working on node ",node)
    if not graph[node]:
        path_sum = sum(current_path)
        path_sums.append(path_sum)
    else:
        print(node," is not in graph")
        for neighbor in graph[node]:
            print(neighbor," is neighbor of ",node)
            dfs(graph, neighbor, current_path.copy(), path_sums)
    print("current path", current_path)
    print("--------------")

graph = defaultdict(list)

a = [10,-5,-13,2,3]
graph[a[0]].append(a[1])
graph[a[0]].append(a[2])
graph[a[1]].append(a[3])
graph[a[2]].append(a[4])

path = []
path_sums = []

dfs(graph, a[0],path,path_sums)
print("path sums", path_sums)
print(graph)

print("num of paths",len(graph[a[0]]))