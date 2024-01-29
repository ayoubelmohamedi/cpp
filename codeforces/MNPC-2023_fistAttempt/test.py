
from collections import defaultdict


def dfs(graph, visited, sum)
graph = defaultdict(list)

a = [10,-5,-13,2,3]
graph[a[0]].append(a[1])
graph[a[0]].append(a[2])
graph[a[1]].append(a[3])
graph[a[2]].append(a[4])

print(graph)
poss_ans = []

for i in graph:
    for neighbor in graph[i]:
        print("neighbor = ",i)