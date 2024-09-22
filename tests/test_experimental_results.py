import sys
import os

# Add the parent directory of 'src' to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import json
import csv
import matplotlib.pyplot as plt
from src.breadth_first_search import BreadthFirstSearch
from src.depth_first_search import DepthFirstSearch
from src.best_first_search import BestFirstSearch
from src.a_star_search import AStarSearch

# Number of repetitions for timing
REPETITIONS = 100

def run_experiment(start_city, goal_city):
    results = []

    # BFS
    bfs_algo = BreadthFirstSearch('data/romania_map.json')
    start_time = time.time()
    for _ in range(REPETITIONS):
        bfs_result = bfs_algo.bfs_search(start_city, goal_city)
    bfs_time = (time.time() - start_time) / REPETITIONS
    results.append({
        "Algorithm": "BFS",
        "Path Found": bool(bfs_result['path']),
        "Nodes Expanded": bfs_result['nodes_expanded'],
        "Time Taken (s)": bfs_time,
        "Max Fringe Size": bfs_result['max_fringe_size'],
        "Optimal Path": bfs_result['path'][-1] == goal_city if bfs_result['path'] else False
    })

    # DFS
    dfs_algo = DepthFirstSearch('data/romania_map.json')
    start_time = time.time()
    for _ in range(REPETITIONS):
        dfs_result = dfs_algo.dfs_search(start_city, goal_city)
    dfs_time = (time.time() - start_time) / REPETITIONS
    results.append({
        "Algorithm": "DFS",
        "Path Found": bool(dfs_result['path']),
        "Nodes Expanded": dfs_result['nodes_expanded'],
        "Time Taken (s)": dfs_time,
        "Max Fringe Size": dfs_result['max_fringe_size'],
        "Optimal Path": dfs_result['path'][-1] == goal_city if dfs_result['path'] else False
    })

    # Best-First Search
    best_first_algo = BestFirstSearch('data/romania_map.json', 'data/heuristic_to_bucharest.json')

    # Heuristic 1
    start_time = time.time()
    for _ in range(REPETITIONS):
        best_first_result_1 = best_first_algo.best_first_search(start_city, goal_city)
    best_first_time_1 = (time.time() - start_time) / REPETITIONS
    results.append({
        "Algorithm": "Best-First (Heuristic 1)",
        "Path Found": bool(best_first_result_1['path']),
        "Nodes Expanded": best_first_result_1['nodes_expanded'],
        "Time Taken (s)": best_first_time_1,
        "Max Fringe Size": best_first_result_1['max_fringe_size'],
        "Optimal Path": best_first_result_1['path'][-1] == goal_city if best_first_result_1['path'] else False
    })

    # A* Search
    a_star_algo = AStarSearch('data/romania_map.json', 'data/heuristic_to_bucharest.json')

    # Heuristic 1
    start_time = time.time()
    for _ in range(REPETITIONS):
        a_star_result_1 = a_star_algo.a_star_search(start_city, goal_city)
    a_star_time_1 = (time.time() - start_time) / REPETITIONS
    results.append({
        "Algorithm": "A* (Heuristic 1)",
        "Path Found": bool(a_star_result_1['path']),
        "Nodes Expanded": a_star_result_1['nodes_expanded'],
        "Time Taken (s)": a_star_time_1,
        "Max Fringe Size": a_star_result_1['max_fringe_size'],
        "Optimal Path": a_star_result_1['path'][-1] == goal_city if a_star_result_1['path'] else False
    })

    return results

def save_results_to_csv(results, test_case):
    # Ensure the results folder exists
    os.makedirs('results', exist_ok=True)
    csv_file = f'results/metrics_{test_case}.csv'

    # Save results in CSV format
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

def plot_results(results, test_case):
    # Ensure the results folder exists
    os.makedirs('results', exist_ok=True)

    # Extract data for plotting
    algorithms = [res["Algorithm"] for res in results]
    nodes_expanded = [res["Nodes Expanded"] for res in results]
    times_taken = [res["Time Taken (s)"] for res in results]

    # Plot Nodes Expanded vs Algorithm
    plt.figure(figsize=(10, 5))
    plt.bar(algorithms, nodes_expanded, color='blue')
    plt.title(f'Nodes Expanded vs Algorithm - {test_case}')
    plt.xlabel('Algorithm')
    plt.ylabel('Nodes Expanded')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'results/nodes_expanded_{test_case}.png')
    plt.close()  # Close the figure to avoid memory issues

    # Plot Time Taken vs Algorithm
    plt.figure(figsize=(10, 5))
    plt.bar(algorithms, times_taken, color='green')
    plt.title(f'Time Taken vs Algorithm - {test_case}')
    plt.xlabel('Algorithm')
    plt.ylabel('Time Taken (s)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'results/time_taken_{test_case}.png')
    plt.close()

if __name__ == "__main__":
    # List of test cases to run (start city, goal city)
    test_cases = [
        ("Arad", "Bucharest"),
        ("Timisoara", "Craiova"),
        ("Zerind", "Sibiu"),
        ("Oradea", "Pitesti"),
        ("Arad", "Neamt")
    ]

    for start_city, goal_city in test_cases:
        test_case_name = f"{start_city}_to_{goal_city}"
        print(f"Running experiment for {start_city} -> {goal_city}")

        # Run the experiment
        experiment_results = run_experiment(start_city, goal_city)

        # Save results to CSV
        save_results_to_csv(experiment_results, test_case_name)

        # Plot and save the results
        plot_results(experiment_results, test_case_name)
