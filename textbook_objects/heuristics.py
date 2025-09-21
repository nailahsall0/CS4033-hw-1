import math
# heuristic from textbook: straight line distances to Bucharest
hSLD_bucharest = {
    "Arad": 366, "Bucharest": 0, "Craiova": 160, "Drobeta": 242,
    "Eforie": 161, "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151,
    "Iasi": 226, "Lugoj": 244, "Mehadia": 241, "Neamt": 234,
    "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193,
    "Sibiu": 253, "Timisoara": 329, "Urziceni": 80,
    "Vaslui": 199, "Zerind": 374
}

def heuristic1(goal, romania_adj_list):
    cities_list = romania_adj_list.keys()
    h ={}
    for city in cities_list:
        h[city] = math.inf
    h[goal] = 0

    distance_changed = True
    while distance_changed == True:
        distance_changed = False
        for city in cities_list:
            neighbors = romania_adj_list[city]
            for neighbor in neighbors:
                distance = neighbors[neighbor]
            
            # if you find a shorter path
            if h[city] > h[neighbor] + distance:
                h[city] = h[neighbor] + distance
                distance_changed = True
    return h

def heuristic2(goal, romania_adj_list):
    cities_list = romania_adj_list.keys()
    h = {}

    for city in cities_list:
        if city == goal:
            h[city] = 0 #the heuristic for the goal is always 0
        else:
            neighbors = romania_adj_list[city]
            estimates = []
            for neighbor, dist in neighbors.items(): 
                neighbor_est = 0 if neighbor == goal else hSLD_bucharest.get(neighbor, 999) #if neighbor is the goal use edge distanc, else use SLD
                estimates.append(dist + neighbor_est)
                #choose the smallest estimate
            h[city] = min(estimates) if estimates else 9999 #if there are no neighbors use fallback num
    return h


