
100 %
import heapq



def get_successors(state):
    """Retourne les successeurs d'un état sous forme (next_state, action, cout)."""
    successors = []

    index = state.index(0)  # position de x
    row = index // 3
    col = index % 3

    def swap_and_create(i1, i2):
        new_state = list(state)
        new_state[i1], new_state[i2] = new_state[i2], new_state[i1]
        return tuple(new_state)

   
    if row > 0:
        new_state = swap_and_create(index, index - 3)
        successors.append((new_state, 'UP', 9))

    
    if row < 2:
        new_state = swap_and_create(index, index + 3)
        successors.append((new_state, 'DOWN', 2))

   
    if col > 0:
        new_state = swap_and_create(index, index - 1)
        successors.append((new_state, 'LEFT', 4))

   
    if col < 2:
        new_state = swap_and_create(index, index + 1)
        successors.append((new_state, 'RIGHT', 3))

    return successors




def UCS(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    parents = {start: None}
    actions = {start: None}
    g_cost = {start: 0}

    closed = set()

    while open_list:
        current_cost, state = heapq.heappop(open_list)

        if state in closed:
            continue
        closed.add(state)

      
        if state == goal:
            path_actions = []
            path_costs = []
            while parents[state] is not None:
                path_actions.append(actions[state][0])
                path_costs.append(actions[state][1])
                state = parents[state]
            path_actions.reverse()
            path_costs.reverse()
            return path_actions, path_costs, sum(path_costs)

        
        for next_state, action, cost in get_successors(state):
            new_cost = current_cost + cost

            if next_state not in g_cost or new_cost < g_cost[next_state]:
                g_cost[next_state] = new_cost
                parents[next_state] = state
                actions[next_state] = (action, cost)
                heapq.heappush(open_list, (new_cost, next_state))

    return None





start = (2, 8, 3,
         1, 6, 4,
         7, 0, 5)

goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)

result = UCS(start, goal)

print("Actions :", result[0])
print("Coûts   :", result[1])
print("Coût total :", result[2])
