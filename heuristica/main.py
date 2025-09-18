from greedy import greedy_best_first_search
from a_star import a_star_search
from graphs import graph_romania
from heuristics import heuristic_romania

def run_romania():
    start, goal = 'Arad', 'Bucharest'
    print(f'=== ROMANIA GRAPH (start: {start} -> goal: {goal}) ===')
    g_path, g_order, g_cost = greedy_best_first_search(graph_romania, start, goal, heuristic_romania)
    print('[Greedy] path:', g_path, 'explored:', g_order, 'cost:', g_cost)
    a_path, a_order, a_cost = a_star_search(graph_romania, start, goal, heuristic_romania)
    print('[A*]     path:', a_path, 'explored:', a_order, 'cost:', a_cost)

if __name__ == '__main__':
    run_romania()
