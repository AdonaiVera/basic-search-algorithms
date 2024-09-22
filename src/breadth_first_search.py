import json
from collections import deque
import time

class BreadthFirstSearch:
    def __init__(self, map_file):
        # Load the Romanian road map from the JSON file
        with open(map_file, 'r') as f:
            self.romania_map = json.load(f)

    def bfs_search(self, start_city, goal_city):
        # Initialize the fringe (queue) with the start node
        fringe = deque([(start_city, [start_city])])
        visited = set()
        nodes_expanded = 0
        max_fringe_size = 0

        # Start timer
        start_time = time.time()

        while fringe:
            # Track the max fringe size
            max_fringe_size = max(max_fringe_size, len(fringe))
            
            # Dequeue the next node from the front of the queue
            current_city, path = fringe.popleft()

            # Test if this is the goal
            if current_city == goal_city:
                end_time = time.time()
                return {
                    "path": path,
                    "nodes_expanded": nodes_expanded,
                    "time_taken": end_time - start_time,
                    "max_fringe_size": max_fringe_size
                }

            # If not visited, expand this node
            if current_city not in visited:
                visited.add(current_city)
                nodes_expanded += 1  # Track the number of nodes expanded

                # Add all children (neighbors) to the back of the queue
                for neighbor, distance in self.romania_map[current_city].items():
                    if neighbor not in visited:
                        fringe.append((neighbor, path + [neighbor]))

        # If the queue is empty and no solution was found, return metrics with an empty path
        end_time = time.time()
        return {
            "path": [],
            "nodes_expanded": nodes_expanded,
            "time_taken": end_time - start_time,
            "max_fringe_size": max_fringe_size
        }

# Example usage
if __name__ == "__main__":
    search_algo = BreadthFirstSearch('data/romania_map.json')
    start = "Arad"
    goal = "Bucharest"
    result = search_algo.bfs_search(start, goal)
    
    print(f"Path: {result['path']}")
    print(f"Nodes Expanded: {result['nodes_expanded']}")
    print(f"Max Fringe Size: {result['max_fringe_size']}")