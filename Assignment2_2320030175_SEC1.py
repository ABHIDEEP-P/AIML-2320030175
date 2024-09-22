# -*- coding: utf-8 -*-
"""AIML _ASSIGNMENT_2320030175_SEC1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T4nJveKGe0pXG-0BB23Xp4mp_Sp9t98Q
"""

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
bfs(graph, 'A')

"""BFS CODE"""

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
dfs_recursive(graph, 'A')

"""DFS CODE"""

def dfs_limited(graph, node, goal, depth, visited):
    if depth == 0:
        if node == goal:
            return [node]
        else:
            return None
    if depth > 0:
        visited.add(node)
        path = None
        for neighbor in graph[node]:
            if neighbor not in visited:
                result = dfs_limited(graph, neighbor, goal, depth - 1, visited)
                if result:
                    path = [node] + result
                    break
        return path
    return None

def iddfs(graph, start, goal):
    depth = 0
    while True:
        visited = set()
        path = dfs_limited(graph, start, goal, depth, visited)
        if path:
            return path
        depth += 1
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
goal = 'F'
path = iddfs(graph, start, goal)

print(f"Path from {start} to {goal}: {path}")

"""Iterative Depening Code"""

from collections import deque
def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]
    forward_queue = deque([start])
    backward_queue = deque([goal])
    forward_paths = {start: [start]}
    backward_paths = {goal: [goal]}
    forward_visited = set([start])
    backward_visited = set([goal])
    while forward_queue and backward_queue:
        current_forward = forward_queue.popleft()
        for neighbor in graph[current_forward]:
            if neighbor in backward_visited:
                return forward_paths[current_forward] + backward_paths[neighbor][::-1][1:]
            if neighbor not in forward_visited:
                forward_visited.add(neighbor)
                forward_queue.append(neighbor)
                forward_paths[neighbor] = forward_paths[current_forward] + [neighbor]
        current_backward = backward_queue.popleft()
        for neighbor in graph[current_backward]:
            if neighbor in forward_visited:
                return backward_paths[current_backward] + forward_paths[neighbor][::-1][1:]
            if neighbor not in backward_visited:
                backward_visited.add(neighbor)
                backward_queue.append(neighbor)
                backward_paths[neighbor] = backward_paths[current_backward] + [neighbor]

    return None
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
goal = 'F'
path = bidirectional_search(graph, start, goal)

print(f" {start} to {goal}: {path}")

"""Bidrectional Search Code"""

import heapq
def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start)]  # (cost, node)
    costs = {start: 0}
    paths = {start: [start]}
    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        if current_node == goal:
            return paths[current_node]
        for neighbor, weight in graph[current_node].items():
            new_cost = current_cost + weight
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappu

"""Least Cost Search"""

import heapq
def a_star_search(start, goal, grid):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    def neighbors(node):
        x, y = node
        results = []
        if x > 0: results.append((x - 1, y))
        if x < len(grid) - 1: results.append((x + 1, y))
        if y > 0: results.append((x, y - 1))
        if y < len(grid[0]) - 1: results.append((x, y + 1))
        return results
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), start))
    g_cost = {start: 0}
    came_from = {}
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        for neighbor in neighbors(current):
            if (0 <= neighbor[0] < len(grid) and
                0 <= neighbor[1] < len(grid[0]) and
                grid[neighbor[0]][neighbor[1]] == 0):
                tentative_g_cost = g_cost[current] + 1
                if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g_cost
                    f_cost = tentative_g_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_cost, neighbor))
                    came_from[neighbor] = current
    return None

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start_node = (0, 0)
goal_node = (4, 4)

path = a_star_search(start_node, goal_node, grid)
print(f"Path from {start_node} to {goal_node}: {path}")

"""A* Search Code"""

MAX, MIN = 1000, -1000
def minimax(depth, nodeIndex, maximizingPlayer,
			values, alpha, beta):
	if depth == 3:
		return values[nodeIndex]
	if maximizingPlayer:
		best = MIN
		for i in range(0, 2):
			val = minimax(depth + 1, nodeIndex * 2 + i,
						False, values, alpha, beta)
			best = max(best, val)
			alpha = max(alpha, best)
			if beta <= alpha:
				break
		return best
	else:
		best = MAX
		for i in range(0, 2):
			val = minimax(depth + 1, nodeIndex * 2 + i,
							True, values, alpha, beta)
			best = min(best, val)
			beta = min(beta, best)
			if beta <= alpha:
				break
		return best
if __name__ == "__main__":
	values = [3, 5, 6, 9, 1, 2, 0, -1]
	print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))

"""Alpha Beta Code"""

import heapq
class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.parent = None
    def __lt__(self, other):
        return self.heuristic < other.heuristic
def best_first_search(start, goal, graph, heuristic):
    open_list = []
    visited = set()
    heapq.heappush(open_list, (heuristic[start], Node(start, heuristic[start])))
    while open_list:
        current_heuristic, current_node = heapq.heappop(open_list)
        current_name = current_node.name
        if current_name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]
        if current_name in visited:
            continue
        visited.ad

"""Best First Search"""

class Node:
    def __init__(self, value=None, is_max_node=True):
        self.value = value
        self.children = []
        self.is_max_node = is_max_node
def minimax(node, depth, is_maximizing_player):
    if not node.children or depth == 0:
        return node.value
    if is_maximizing_player:
        best_value = float('-inf')
        for child in node.children:
            value = minimax(child, depth - 1, False)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for child in node.children:
            value = minimax(child, depth - 1, True)
            best_value = min(best_value, value)
        return best_value
root = Node(is_max_node=True)
min1 = Node(is_max_node=False)
min2 = Node(is_max_node=False)

leaf1 = Node(value=3, is_max_node=True)
leaf2 = Node(value=5, is_max_node=True)
leaf3 = Node(value=2, is_max_node=True)
leaf4 = Node(value=9, is_max_node=True)


min1.children = [leaf1, leaf2]
min2.children = [leaf3, leaf4]
root.children = [min1, min2]

best_value = minimax(root, depth=2, is_maximizing_player=True)
print(f"The best value for the maximizer is: {best_value}")

"""Min Max Code"""

