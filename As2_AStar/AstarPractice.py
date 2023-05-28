from heapq import heappop, heappush

def a_star(graph, start, goal, heuristic):
    # Initialize the open and closed lists
    open_list = [(0, start)]  # (f_score, node)
    closed_set = set()
    
    # Initialize the g_score dictionary
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    # Initialize the f_score dictionary
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]
    
    # Initialize the came_from dictionary for path reconstruction
    came_from = {}
    
    while open_list:
        # Get the node with the lowest f_score from the open list
        current_f_score, current_node = heappop(open_list)
        
        if current_node == goal:
            # Goal reached, reconstruct and return the path
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path
        
        closed_set.add(current_node)
        
        # Explore neighbors
        for neighbor in graph[current_node]:
            if neighbor in closed_set:
                continue
            
            # Calculate the tentative g_score
            tentative_g_score = g_score[current_node] + graph[current_node][neighbor]
            
            if tentative_g_score < g_score[neighbor]:
                # Update the g_score and f_score
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                
                # Add the neighbor to the open list
                heappush(open_list, (f_score[neighbor], neighbor))
                
                # Update the came_from dictionary
                came_from[neighbor] = current_node
    
    # No path found
    return None


heuristic= {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0
    }


# Describe your graph here
Graph_nodes = {'A': {'B': 2,'E': 3},
               'B': {'A':2 ,'C': 1,'G': 9},
               'C': {'B':1},
               'E': {'A':3,'D': 6},
               'D': {'E':6,'G': 1},
               'G': {'B':9,'D':1}
               }

path = a_star(Graph_nodes,'A', 'G',heuristic)

print (path)
'''def euclidean_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def dynamic_heuristic(node, goal):
    # Define the coordinates of nodes in a 2D coordinate system
    coordinates = {
        'A': (1, 2),
        'B': (3, 4),
        'C': (5, 6),
        'D': (7, 8),
        'E': (9, 10),
        'F': (11, 12)
    }
    
    # Calculate the Euclidean distance between the given node and the goal node
    return euclidean_distance(coordinates[node], coordinates[goal])
'''


