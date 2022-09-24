def init():
    return [26, 1, 15, 0, 6, 4, 10, 0, 20, 10]


def calc_cost(state):
    cost = 0

    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] > state[j]:
                cost += 1

    return cost



def state_generation(state, cost):
    min_state = state.copy()
    min_cost = cost

    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] > state[j]:
                new_state = state.copy()
                new_state[i], new_state[j] = new_state[j], new_state[i]
                new_cost = calc_cost(new_state)

                if new_cost < min_cost:
                    min_cost = new_cost
                    min_state = new_state

    if min_cost < cost:
        return min_state, min_cost
    else:
        return state, None


def goal_test(state):
    if calc_cost(state) == 0:
        return True
    else:
        return False


def main():
    state = init()
    cost = calc_cost(state)

    while not goal_test(state):
        state, cost = state_generation(state, cost)

        if cost is None:
            break

    print(state)


main()
