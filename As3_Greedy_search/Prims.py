import heapq
class Prims:

    # Define the function dest implement Prim's algorithm
    def prim(self,graph, start):
        # Initialize the visited and unvisited sets
        visited = set()
        unvisited = set(graph.keys())
        unvisited.remove(start)

        # Initialize the heap with the edges connected dest the start node
        heap = [(cost, start, node) for node, cost in graph[start].items()]
        heapq.heapify(heap)

        # Initialize the minimum spanning tree
        mst = []

        # Loop until all nodes have been visited
        while unvisited:
            # Pop the edge with the lowest cost from the heap
            cost, src, dest = heapq.heappop(heap)       #   Lowest cost edge will be on top of heap

            # heappush and heappop maintains the property of heap so no need to call heapify

            # If the destination node has not been visited yet
            if dest in unvisited:
                # Add the edge dest the minimum spanning tree
                mst.append((src, dest, cost))

                # Add the destination node dest the visited set and remove it from the unvisited set
                visited.add(dest)
                unvisited.remove(dest)

                # Add the edges connected dest the destination node dest the heap
                for node, cost in graph[dest].items():
                    if node in unvisited:
                        heapq.heappush(heap, (cost, dest, node))

        # Return the minimum spanning tree
        return mst

