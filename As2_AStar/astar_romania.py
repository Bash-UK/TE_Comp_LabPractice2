def aStarAlgo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {}  # store distance from starting node
    parents = {}  # parents contains an adjacency map of all nodes m
    # ditance of starting node from itself is zero
    g[start_node] = 0  # start_node is root node i.e it has no parent nodes
    # so start_node is set to its own parent node
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None  # node with Lowest f( ) is found
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            break
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        # update g(m)
                        g[m] = g[n] + weight
                        # change parent of m to n
                        parents[m] = n
                        # if m in closed set, remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        # remove n from the open_set and add it to closed_set
        # because all of its neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)

    if n == None:
        print('Path does not exist!')
        return None

    # reconstruct the path from the start_node to n
    path = []
    while parents[n] != n:
        path.append(n)
        n = parents[n]
    path.append(start_node)
    path.reverse()
    print(f'Path found: {path}')
    return path


# define function to return neighbor and its distance
# from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


# for simplicity we'll consider heuristic distances given
# and this function returns heuristic distance for all nodes
def heuristic(n):
    H_dist = {
        'Arad':366,
        'Bucharest':0,
        'Craiova':160,
        'Dobreta':242,
        'Eforie':161,
        'Fagaras':176,
        'Giurgiu':77,
        'Hirasova':151,
        'Iasi':226,
        'Lugoj':244,
        'Mehadia':241,
        'Neamt':234,
        'Oradea':380,
        'Pitesti':100,
        'Rimnicu Vilcea':193,
        'Sibiu':253,
        'Timisoara':329,
        'Urziceni':80,
        'Vaslui':199,
        'Zerind':374
    }
    return H_dist[n]


# Describe your graph here
Graph_nodes = {
                'Arad': [('Sibiu',140),('Timisoara',118),('Zerind',75)],
                'Bucharest': [('Fagaras',211),('Giurgiu',90),('Pitesti',101),('Urziceni',85)],
                'Craiova': [('Dobreta',120),('Pitesti',138),('Rimnicu Vilcea',146)],
                'Dobreta': [('Craiova',120),('Mehadia',75)],
                'Eforie': [('Hirasova',86)],
                'Fagaras': [('Bucharest',211),('Sibiu',99)],
                'Giurgiu': [('Bucharest',90)],
                'Hirasova': [('Eforie',86)],
                'Iasi': [('Neamt',87),('Vaslui',92)],
                'Lugoj': [('Mehadia',75),('Timisoara',111)],
                'Mehadia': [('Dobreta',75),('Lugoj',70)],
                'Neamt': [('Iasi',87)],
                'Oradea': [('Sibiu',151),('Zerind',71)],
                'Pitesti': [('Bucharest',101),('Craiova',138),('Rimnicu Vilcea',97)],
                'Rimnicu Vilcea': [('Craiova',146),('Pitesti',97),('Sibiu',80)],
                'Sibiu': [('Arad',140),('Fagaras',99),('Oradea',151),('Rimnicu Vilcea',80)],
                'Timisoara': [('Arad',118),('Lugoj',111)],
                'Urziceni': [('Bucharest',85),('Hirasova',98),('Vaslui',142)],
                'Vaslui': [('Iasi',92),('Urziceni',142)],
                'Zerind': [('Arad',75),('Oradea',71)],
               }
flag = True
while(flag):
	print(" Arad\tBucharest\nCraiova\tDobreta\nEforie\tFagaras\nGiurgiu\tHirasova\nIasi\tLugoj\nMehadia\tNeamt\nOradea\tPitesti\nRimnicu Vilcea\tSibiu\nTimisoara\tUrziceni\nVaslui\tZerind")
	start = input("Start Node: ")
	goal = input("Goal Node: ")
	aStarAlgo(start,goal)
	ans = input("Continue?(y/n): ")
	if(ans=='n'):
	    flag = False