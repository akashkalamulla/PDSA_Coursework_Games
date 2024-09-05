import heapq
import time

from algo import random_no_generator
from algo.Bellman_Ford_algo import distances, get_path

random_numbers = random_no_generator.random_numbers
random_letter = random_no_generator.random_letter

random_city = f"City {random_letter}"


cities = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
city_index = {cities[i]: i for i in range(len(cities))}


# Dijkstra's algorithm to find shortest paths from the start city
def dijkstra(dist_matrix, start_city_idx):
    num_cities = len(dist_matrix)
    dist = [float('inf')] * num_cities
    pred = [None] * num_cities  # Predecessor array to store the path
    dist[start_city_idx] = 0
    priority_queue = [(0, start_city_idx)]  # (distance, city_idx)

    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)

        if current_dist > dist[u]:
            continue

        for v in range(num_cities):
            if dist_matrix[u][v] < float('inf'):
                new_dist = dist[u] + dist_matrix[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    pred[v] = u
                    heapq.heappush(priority_queue, (new_dist, v))

    return dist, pred


# Use the same `get_path` function to reconstruct the shortest path
# Ensure `distances` is defined from previous code

# Find the shortest path distances from the selected city
start_city_idx = city_index[random_letter]

# Record the start time
start_time = time.time()

shortest_paths, predecessors = dijkstra(distances, start_city_idx)

# Record the end time
end_time = time.time()

""""
def display1():
    # Output the results
    if shortest_paths is not None:
        print(f"Shortest paths from {random_city}:")
        for i in range(len(cities)):
            path = get_path(predecessors, start_city_idx, i)
            path_str = ''.join(path)  # Concatenate city names into a single string
            if i == start_city_idx:
                print(f"Distance to City {cities[i]} (itself): 0 km")
                print(f"Path: {cities[i]}")
            else:
                print(f"Distance to City {cities[i]}: {shortest_paths[i]} km")
                print(f"Path: {path_str}")

    # Display the time taken
    print(f"\nTime taken for Dijkstra's algorithm: {end_time - start_time} seconds")
"""""
dijkstra_time=end_time - start_time
# Call the display function to show the results
#display1()
