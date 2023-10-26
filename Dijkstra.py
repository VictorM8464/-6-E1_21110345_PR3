import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def shortest_path(graph, start, end):
    distances, previous_nodes = dijkstra(graph, start)
    path = []
    while end:
        path.insert(0, end)
        end = previous_nodes.get(end)
    return path

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
end_node = 'D'
distances, previous_nodes = dijkstra(graph, start_node)

current_node = end_node
while current_node:
    print(f'Nodo actual: {current_node}, Distancia desde {start_node}: {distances[current_node]}')
    current_node = previous_nodes.get(current_node)

print(f'Camino mas corto desde {start_node} a {end_node}: {shortest_path(graph, start_node, end_node)}')
