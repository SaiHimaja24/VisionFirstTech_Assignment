import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == end:
            break
        for neighbor, weight in graph[current_node]:
            if neighbor in visited:
                continue
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
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
