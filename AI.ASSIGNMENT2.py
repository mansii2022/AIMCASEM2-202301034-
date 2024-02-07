#question1
"""
from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['D','G'],
    'D': ['F'],
    'E': ['B'],
    'F': ['G','H'],
    'G': []
}

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    visited.add(start)
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for adjacent_node in graph[node]:
            if adjacent_node not in visited:
                queue.append(path + [adjacent_node])
                visited.add(adjacent_node)
    return None

path = bfs(graph,'A','G')
if path:
    print("Path to final node G:")
    for node in path:
        print(node, end=" -> ")
    print("")
    print("Order of traversal: ")
    for i in range(len(path)-1):
        print(path[i], end=" > ")
    print(path[-1])
else:
    print("No path found from 'A' to 'G'") """


#question 2
from collections import deque
#adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['D','G'],
    'D': ['F'],
    'E': ['B'],
    'F': ['G','H'],
    'G': []
}
def dfs(graph, start, end):
    stack = deque([[start]])
    visited = set()
    visited.add(start)
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == end:
            return path
        for adjacent_node in graph[node]:
            if adjacent_node not in visited:
                stack.append(path + [adjacent_node])
                visited.add(adjacent_node)
    return None
path = dfs(graph,'A','G')
if path:
    print("Path to final node G:")
    for node in path:
        print(node, end=" -> ")
    print("")
    print("Order of traversal: ")
    for i in range(len(path)-1):
        print(path[i], end=" > ")
    print(path[-1])
else:
    print("No path found from 'A' to 'G'")