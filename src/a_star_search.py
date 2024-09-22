import json
import heapq

class AStarSearch:
    def __init__(self, map_file, heuristic_file):
        # Load the Romanian road map from the JSON file
        with open(map_file, 'r') as f:
            self.romania_map = json.load(f)
        # Load the straight-line distance heuristic to Bucharest
        with open(heuristic_file, 'r') as f:
            self.heuristic_to_bucharest = json.load(f)

    def a_star_search(self, start_city, goal_city):
        # Initialize the priority queue (min-heap)
        fringe = []
        heapq.heappush(fringe, (0 + self.heuristic_to_goal(start_city, goal_city), 0, start_city, [start_city]))
        visited = set()
        nodes_expanded = 0
        max_fringe_size = 0

        # Start A* Search
        while fringe:
            # Track the max fringe size
            max_fringe_size = max(max_fringe_size, len(fringe))

            # Pop the node with the lowest f(n) = g(n) + h(n)
            f_cost, g_cost, current_city, path = heapq.heappop(fringe)

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

                # Add all unvisited neighbors to the priority queue (min-heap)
                for neighbor, distance in self.romania_map[current_city].items():
                    if neighbor not in visited:
                        g_value = g_cost + distance
                        f_value = g_value + self.heuristic_to_goal(neighbor, goal_city)
                        heapq.heappush(fringe, (f_value, g_value, neighbor, path + [neighbor]))

        # If no path is found, return empty metrics
        return {
            "path": [],
            "nodes_expanded": nodes_expanded,
            "max_fringe_size": max_fringe_size
        }

    def heuristic_to_goal(self, city, goal):
        """ 
        Heuristic function to determine the heuristic value based on the goal.
        If the goal is Bucharest, use the straight-line distance to Bucharest.
        If the goal is not Bucharest, apply the triangle inequality.
        """
        if goal == "Bucharest":
            # Use the heuristic to Bucharest
            return self.heuristic_to_bucharest.get(city, float('inf'))
        else:
            # Apply the triangle inequality heuristic for non-Bucharest goals
            sld_to_bucharest = self.heuristic_to_bucharest.get(city, float('inf'))
            sld_from_bucharest_to_goal = self.heuristic_to_bucharest.get(goal, float('inf'))

            # Option 1: Heuristic via Bucharest
            heuristic_via_bucharest = sld_to_bucharest + sld_from_bucharest_to_goal

            # Option 2: Direct heuristic or estimate
            heuristic_direct = self.estimate_direct_sld(city, goal)

            # Return the smaller of the two admissible heuristics
            return min(heuristic_via_bucharest, heuristic_direct)

    def estimate_direct_sld(self, city, goal):
        """
        Estimate the straight-line distance (SLD) between two cities when the goal is not Bucharest.
        We use the triangle inequality with Bucharest as an intermediate city.
        """
        sld_to_bucharest = self.heuristic_to_bucharest.get(city, float('inf'))
        sld_from_bucharest_to_goal = self.heuristic_to_bucharest.get(goal, float('inf'))

        # Estimate the SLD using Bucharest as an intermediate node
        heuristic_estimate = sld_to_bucharest + sld_from_bucharest_to_goal

        return heuristic_estimate

# Example usage
if __name__ == "__main__":
    search_algo = AStarSearch('data/romania_map.json', 'data/heuristic_to_bucharest.json')
    start = "Arad"
    goal = "Fagaras"
    result = search_algo.a_star_search(start, goal)

    print(f"Path: {result['path']}")
    print(f"Nodes Expanded: {result['nodes_expanded']}")
    print(f"Max Fringe Size: {result['max_fringe_size']}")
