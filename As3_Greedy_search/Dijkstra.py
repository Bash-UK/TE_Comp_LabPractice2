
import heapq

def dkALgo(graph,start):
    distances = {node:float('inf') for node in graph}
    distances[start]=0

    heap = [(0,start)]
    while heap:
        curr_dist,curr_node = heapq.heappop(heap)

        if curr_dist > distances[curr_node]:
            continue
    
        for neighbour,wt in graph[curr_node].items():
            distance = curr_dist + wt
            if distance < distances[neighbour]:
                distances[neighbour]=distance
                heapq.heappush(heap,(distance,neighbour))
    return distances


graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 5, 'B': 1, 'D': 1, 'E': 3},
    'D': {'B': 4, 'C': 1, 'E': 1, 'F': 5},
    'E': {'C': 3, 'D': 1, 'F': 2},
    'F': {'D': 5, 'E': 2}
}
start_node = 'A'
end= 'C'
distances = dkALgo(graph,start_node)

print(f"Shortest path from {start_node}: ")
for node,dist in distances.items():
    print(f"{node}=> {dist}")