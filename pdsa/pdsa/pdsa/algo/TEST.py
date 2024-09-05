from algo import random_no_generator

random_numbers = random_no_generator.random_numbers
random_letter = random_no_generator.random_letter

random_city = f"City {random_letter}"

cities = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
city_index = {cities[i]: i for i in range(len(cities))}

names = ["AJ", "BJ", "CJ", "DJ", "EJ",  # Add as many names as needed
         "FJ", "GJ", "HJ", "IJ", "AI",
         "BI", "CI", "DI", "EI", "FI",
         "GI", "HI", "AH", "BH", "CH",
         "DH", "EH", "FH", "GH", "AG",
         "BG", "CG", "DG", "EG", "FG",
         "AF", "BF", "CF", "DF", "EF",
         "AE", "BE", "CE", "DE", "AD",
         "BD", "CD", "AC", "BC", "AB"]

# Generating a 2D array where each sub-array contains a name and a random number
random_numbers_with_names = [[names[i], random_numbers[i]] for i in range(45)]

# Initialize the distance matrix
inf = float('inf')
distances = [[inf] * len(cities) for _ in range(len(cities))]

# Fill the distance matrix with the generated random distances
for pair, distance in random_numbers_with_names:
    from_city = pair[0]
    to_city = pair[1]
    from_idx = city_index[from_city]
    to_idx = city_index[to_city]
    distances[from_idx][to_idx] = distance
    distances[to_idx][from_idx] = distance  # Assuming it's a symmetric matrix

# Bellman-Ford algorithm to find shortest paths from the random city
def bellman_ford(dist_matrix, start_city_idx):
    num_cities = len(dist_matrix)
    dist = [inf] * num_cities
    pred = [None] * num_cities  # Predecessor array to store the path
    dist[start_city_idx] = 0

    # Relax edges up to (num_cities - 1) times
    for _ in range(num_cities - 1):
        for i in range(num_cities):
            for j in range(num_cities):
                if dist[i] != inf and dist[i] + dist_matrix[i][j] < dist[j]:
                    dist[j] = dist[i] + dist_matrix[i][j]
                    pred[j] = i  # Track the predecessor

    # Check for negative-weight cycles
    for i in range(num_cities):
        for j in range(num_cities):
            if dist[i] != inf and dist[i] + dist_matrix[i][j] < dist[j]:
                print("Graph contains a negative-weight cycle")
                return None, None

    return dist, pred

# Function to reconstruct the shortest path
def get_path(pred, start, end):
    path = []
    while end is not None:
        path.insert(0, cities[end])
        end = pred[end]
    if path[0] == cities[start]:
        return path
    return []

# Find the shortest path distances from the selected city
start_city_idx = city_index[random_letter]
shortest_paths, predecessors = bellman_ford(distances, start_city_idx)

def display():
    # Output the results
    if shortest_paths is not None:
        print(f"Shortest paths from {random_city}:")
        for i in range(len(cities)):
            if i != start_city_idx:  # Skip the start city itself
                path = get_path(predecessors, start_city_idx, i)
                print(f"Distance to City {cities[i]}: {shortest_paths[i]} km")
                print(f"Path: {' -> '.join(path)}")

# Call the display function to show the results
display()
