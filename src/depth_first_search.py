import json

class DepthFirstSearch:
    def __init__(self, map_file):
        # Load the Romanian road map from the JSON file
        with open(map_file, 'r') as f:
            self.romania_map = json.load(f)

    def dfs_search(self, start_city, goal_city):
        # Initialize the fringe (stack) with the start node
        fringe = [(start_city, [start_city])]
        visited = set()
        nodes_expanded = 0
        max_fringe_size = 0

        # Start Depth-First Search
        while fringe:
            # Track the max fringe size
            max_fringe_size = max(max_fringe_size, len(fringe))

            # Pop the last node from the stack
            current_city, path = fringe.pop()

            # Check if the current city is the goal
            if current_city == goal_city:
                return {
                    "path": path,
                    "nodes_expanded": nodes_expanded,
                    "max_fringe_size": max_fringe_size
                }

            # If not visited, expand this node
            if current_city not in visited:
                visited.add(current_city)
                nodes_expanded += 1  # Track the number of nodes expanded

                # Add all unvisited neighbors to the stack
                for neighbor, distance in self.romania_map[current_city].items():
                    if neighbor not in visited:
                        fringe.append((neighbor, path + [neighbor]))

        # If no path is found, return empty metrics
        return {
            "path": [],
            "nodes_expanded": nodes_expanded,
            "max_fringe_size": max_fringe_size
        }

# Example usage
if __name__ == "__main__":
    search_algo = DepthFirstSearch('data/romania_map.json')
    start = "Arad"
    goal = "Bucharest"
    result = search_algo.dfs_search(start, goal)
    
    print(f"Path: {result['path']}")
    print(f"Nodes Expanded: {result['nodes_expanded']}")
    print(f"Max Fringe Size: {result['max_fringe_size']}")
