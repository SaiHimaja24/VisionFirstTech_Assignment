import heapq

def dijkstra(graph, start, end):
    # Initialize distances to all nodes as infinity
    distances = {node: float('inf') for node in graph}
    # The distance from the start node to itself is 0
    distances[start] = 0
    # Initialize an empty priority queue
    pq = [(0, start)]
    
    while pq:
        # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(pq)
        # If the current node is the end node, we have found the shortest path
        if current_node == end:
            break
        # If the distance to the current node is already larger than the stored distance, skip
        if current_distance > distances[current_node]:
            continue
        # Check neighbors of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            # If the new distance is smaller than the stored distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    # Reconstruct the shortest path
    path = []
    while end != start:
        path.append(end)
        for neighbor, weight in graph[end]:
            if distances[end] - weight == distances[neighbor]:
                end = neighbor
                break
    path.append(start)
    path.reverse()
    return path

def shortest_route(nodes, edges, start, end):
    graph = {node: [] for node in nodes}
    for edge in edges:
        graph[edge['from']].append((edge['to'], edge['weight']))
        graph[edge['to']].append((edge['from'], edge['weight']))  # if graph is undirected
    
    return dijkstra(graph, start, end)

# Example usage
if __name__ == "__main__":
    # Example input
    nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    edges = [
        {"from": "A", "to": "B", "weight": 1},
        {"from": "B", "to": "C", "weight": 3},
        {"from": "B", "to": "E", "weight": 3.5},
        {"from": "C", "to": "E", "weight": 4},
        {"from": "C", "to": "D", "weight": 2.5},
        {"from": "D", "to": "G", "weight": 2.5},
        {"from": "G", "to": "F", "weight": 3.5},
        {"from": "E", "to": "F", "weight": 2},
        {"from": "F", "to": "H", "weight": 2.5},
        {"from": "H", "to": "I", "weight": 1}
    ]
    start_node = "C"
    end_node = "F"
    
    # Find shortest route
    shortest_path = shortest_route(nodes, edges, start_node, end_node)
    print(shortest_path)
