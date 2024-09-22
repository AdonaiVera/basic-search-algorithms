import unittest
from src.breadth_first_search import BreadthFirstSearch
from src.depth_first_search import DepthFirstSearch
from src.best_first_search import BestFirstSearch
from src.a_star_search import AStarSearch

class TestRomanianSearch(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Set up all search algorithms
        cls.bfs_algo = BreadthFirstSearch('data/romania_map.json')
        cls.dfs_algo = DepthFirstSearch('data/romania_map.json')
        cls.best_first_algo = BestFirstSearch('data/romania_map.json', 'data/heuristic_to_bucharest.json')
        cls.a_star_algo = AStarSearch('data/romania_map.json', 'data/heuristic_to_bucharest.json')
        
    # Breadth-First Search Tests
    def test_bfs_path_found(self):
        start = "Arad"
        goal = "Bucharest"
        result = self.bfs_algo.bfs_search(start, goal)
        path = result['path']

        # Assert that a valid path is found
        self.assertIsNotNone(path)
        self.assertIn(goal, path)
        self.assertEqual(path[0], start)
        
        # Assert that the metrics are reasonable
        self.assertGreater(result['nodes_expanded'], 0)
        self.assertGreaterEqual(result['time_taken'], 0)
        self.assertGreater(result['max_fringe_size'], 0)

    def test_bfs_no_path(self):
        start = "Arad"
        goal = "NonExistentCity"
        result = self.bfs_algo.bfs_search(start, goal)

        # Assert that the path is empty when no valid path exists
        self.assertEqual(result['path'], [])
        self.assertGreater(result['nodes_expanded'], 0)
        self.assertGreaterEqual(result['time_taken'], 0)
        self.assertGreater(result['max_fringe_size'], 0)

    def test_bfs_single_node(self):
        start = "Bucharest"
        goal = "Bucharest"
        result = self.bfs_algo.bfs_search(start, goal)
        path = result['path']
        
        # Assert that the path contains only one node (the start/goal)
        self.assertEqual(path, [start])
        self.assertEqual(result['nodes_expanded'], 0)
        self.assertGreaterEqual(result['time_taken'], 0)
        self.assertEqual(result['max_fringe_size'], 1)

    # Depth-First Search Tests
    def test_dfs_path_found(self):
        # Test DFS for finding a path between Arad and Bucharest
        start = "Arad"
        goal = "Bucharest"
        result = self.dfs_algo.dfs_search(start, goal)
        path = result['path']

        # Assert that a valid path is found
        self.assertIsNotNone(path)
        self.assertIn(goal, path)
        self.assertEqual(path[0], start)

        # Assert that the metrics are reasonable
        self.assertGreater(result['nodes_expanded'], 0)
        self.assertGreaterEqual(result['max_fringe_size'], 0)

    def test_dfs_no_path(self):
        # Test DFS when the goal city doesn't exist
        start = "Arad"
        goal = "NonExistentCity"
        result = self.dfs_algo.dfs_search(start, goal)

        # Assert that the path is empty when no valid path exists
        self.assertEqual(result['path'], [])
        self.assertGreater(result['nodes_expanded'], 0)
        self.assertGreaterEqual(result['max_fringe_size'], 0)

    def test_dfs_single_node(self):
        # Test DFS when start and goal are the same city
        start = "Bucharest"
        goal = "Bucharest"
        result = self.dfs_algo.dfs_search(start, goal)
        path = result['path']

        # Assert that the path contains only one node (the start/goal)
        self.assertEqual(path, [start])
        self.assertEqual(result['nodes_expanded'], 0)
        self.assertGreaterEqual(result['max_fringe_size'], 0)

    # Best-First Search Tests
    def test_bfs_path_found_bucharest(self):
        # Test Best-First Search for finding a path between Arad and Bucharest
        start = "Arad"
        goal = "Bucharest"
        result = self.best_first_algo.best_first_search(start, goal)
        path = result['path']

        # Assert that a valid path is found
        self.assertIsNotNone(path)
        self.assertIn(goal, path)
        self.assertEqual(path[0], start)

        # Assert that the metrics are reasonable
        self.assertGreater(result['nodes_expanded'], 0)
        self.assertGreaterEqual(result['max_fringe_size'], 0)

    def test_bfs_no_path(self):
        # Test Best-First Search when the goal city doesn't exist
        start = "Arad"
        goal = "NonExistentCity"
        result = self.best_first_algo.best_first_search(start, goal)

        # Assert that the path is empty when no valid path exists
        self.assertEqual(result['path'], [])
        self.assertGreater(result['nodes_expanded'], 0)
        self.assertGreaterEqual(result['max_fringe_size'], 0)

    def test_bfs_single_node(self):
        # Test Best-First Search when start and goal are the same city
        start = "Bucharest"
        goal = "Bucharest"
        result = self.best_first_algo.best_first_search(start, goal)
        path = result['path']

        # Assert that the path contains only one node (the start/goal)
        self.assertEqual(path, [start])
        self.assertEqual(result['nodes_expanded'], 0)
        self.assertGreaterEqual(result['max_fringe_size'], 0)

    def test_bfs_path_found_non_bucharest(self):
        # Test Best-First Search with a non-Bucharest goal to check the triangle inequality heuristic
        start = "Arad"
        goal = "Pitesti"
        result = self.best_first_algo.best_first_search(start, goal)
        path = result['path']

        # Assert that a valid path is found
        self.assertIsNotNone(path)
        self.assertIn(goal, path)
        self.assertEqual(path[0], start)

        # Assert that the metrics are reasonable
        self.assertGreater(result['nodes_expanded'], 0)
        self.assertGreaterEqual(result['max_fringe_size'], 0)

    # A* Search Tests
    def test_a_star_path_found_bucharest(self):
        # Test A* for finding a path between Arad and Bucharest
        start = "Arad"
        goal = "Bucharest"
        result = self.a_star_algo.a_star_search(start, goal)
        path = result['path']

        # Assert that a valid path is found
        self.assertIsNotNone(path)
        self.assertIn(goal, path)
        self.assertEqual(path[0], start)

        # Assert that the metrics are reasonable
        self.assertGreater(result['nodes_expanded'], 0)
        self.assertGreaterEqual(result['max_fringe_size'], 0)

    def test_a_star_no_path(self):
        # Test A* when the goal city doesn't exist
        start = "Arad"
        goal = "NonExistentCity"
        result = self.a_star_algo.a_star_search(start, goal)

        # Assert that the path is empty when no valid path exists
        self.assertEqual(result['path'], [])
        self.assertGreater(result['nodes_expanded'], 0)
        self.assertGreaterEqual(result['max_fringe_size'], 0)

    def test_a_star_single_node(self):
        # Test A* when start and goal are the same city
        start = "Bucharest"
        goal = "Bucharest"
        result = self.a_star_algo.a_star_search(start, goal)
        path = result['path']

        # Assert that the path contains only one node (the start/goal)
        self.assertEqual(path, [start])
        self.assertEqual(result['nodes_expanded'], 0)
        self.assertGreaterEqual(result['max_fringe_size'], 0)

    def test_a_star_path_found_non_bucharest(self):
        # Test A* with a non-Bucharest goal to check the triangle inequality heuristic
        start = "Arad"
        goal = "Pitesti"
        result = self.a_star_algo.a_star_search(start, goal)
        path = result['path']

        # Assert that a valid path is found
        self.assertIsNotNone(path)
        self.assertIn(goal, path)
        self.assertEqual(path[0], start)

        # Assert that the metrics are reasonable
        self.assertGreater(result['nodes_expanded'], 0)
        self.assertGreaterEqual(result['max_fringe_size'], 0)

if __name__ == "__main__":
    unittest.main()
