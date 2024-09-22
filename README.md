# Basics Search Algorithms

This repository contains the implementation of four different search algorithms to solve the problem of navigating a Romanian road map. These algorithms are part of a homework assignment for the **Artificial Intelligence I** class (20CS633 AI – I), instructed by Professor Anca Ralescu.

1. **Breadth-first search (BFS)**.
2. **Depth-first search (DFS)**.
3. **Best-first search (Greedy)**.
4. **A\* search algorithm**.

## Table of Contents
- [Introduction](#introduction)
- [Algorithms](#algorithms)
- [Heuristics](#heuristics)
- [Data](#data)
- [How to Run](#how-to-run)
- [Results](#results)
- [Requirements](#requirements)

## Introduction
This project demonstrates the performance of different search algorithms when navigating a simplified Romanian road map. The algorithms are implemented in Python and can be easily run for experimentation and comparison.

## Algorithms
Each algorithm follows a specific strategy for expanding nodes:
- **Breadth-first search (BFS)**: Expands the shallowest unexpanded node.
- **Depth-first search (DFS)**: Explores as far down each branch as possible before backtracking.
- **Best-first search (Greedy)**: Uses a heuristic based on the straight-line distance (SLD) to the goal.
- **A\* Search**: Uses both the cost of the path so far and the estimated cost to the goal (SLD).

## Heuristics
The project uses different heuristics based on the goal city:
- When the goal is **Bucharest**, the SLD is directly provided.
- For other cities, SLD is estimated using geometry (triangle inequality).

## Data
The `data/romania_map.jsonb` file contains the Romanian road map represented as an adjacency matrix. Each cell indicates the distance between two cities.

## How to Run
1. **Clone the repository**:
    ```bash
    git clone https://github.com/AdonaiVera/basic-search-algorithms.git
    cd basic-search-algorithms
    ```
2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the algorithms**:
    Run all the unit tests together using:
    ```bash
    python -m unittest discover tests
    ```
    
   Run each algorithm separately using (Inside each class there is an example of use):
    ```bash
    python src/breadth_first_search.py
    python src/depth_first_search.py
    python src/best_first_search.py
    python src/a_star_search.py
    ```

    Run experimental results (Added in the Report):
    ```bash
    python tests/test_experimental_results.py
    ```

## Arquitecture project
│
├── README.md
├── data/
│   ├── heuristic_to_bucharest.json
│   └── romania_map.json
├── src/
│   ├── breadth_first_search.py
│   ├── depth_first_search.py
│   ├── best_first_search.py
│   └── a_star_search.py
├── tests/
│   ├── test_experimental_results.py
│   └── test_search_algorithms.py
├── results/
│   └── ...
└── requirements.txt

## Results
Performance comparison of the algorithms can be found in the `results/report.pdf`. 

## Requirements
This project uses the following libraries:
- Python 3.12
- matplotlib (for visualizing results)

Install the necessary dependencies by running:
```bash
pip install -r requirements.txt
```

## Team - Group 33
Alhim Vera Gonzalez
Ajay Mannam
Hannah Krzywkowski
