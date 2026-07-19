from collections import deque


def bfs(graph,start):
    visited = set([start])
    # deque actually is: a doubly-linked list of fixed blocks
    queue = deque([start])
    order=[]
    distance = 0

    while queue:
        node=queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor) 

        return order
