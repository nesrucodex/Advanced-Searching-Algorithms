def uniformCostSearch():
    def uniform_cost_search(goal, start):
        global graph, cost
        answer = []
        # create a priority queue
        queue = []

        # set the answer vector to max value
        for i in range(len(goal)):
            answer.append(10 ** 8)

        # insert the starting index
        queue.append([0, start])

        # map to store visited node
        visited = {}

        # count
        count = 0

        # while the queue is not empty
        while (len(queue) > 0):

            # get the top element of the queue
            queue = sorted(queue)
            p = queue[-1]

            # pop the element
            del queue[-1]

            # get the original value
            p[0] *= -1

            if (p[1] in goal):
                # get the position
                index = goal.index(p[1])

                # if a new goal is reached
                if (answer[index] == 10 ** 8):
                    count += 1

                # if the cost is less
                if (answer[index] > p[0]):
                    answer[index] = p[0]

                    # pop the element
                    del queue[-1]

                    queue = sorted(queue)

                    if (count == len(goal)):
                        return answer

            if (p[1] not in visited):
                for i in range(len(graph[p[1]])):
                    # append the next node and its cost to the queue
                    queue.append([(p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])

                # mark as visited
                visited[p[1]] = 1

        return answer

   
    # create the graph
    graph, cost = [[] for i in range(8)], {}

    # add edges
    graph[0].append(1)
    graph[0].append(3)
    graph[3].append(1)
    graph[3].append(4)
    graph[1].append(6)
    graph[2].append(1)
    graph[5].append(2)
    graph[5].append(6)
    graph[6].append(4)

    # add the cost
    cost[(0, 1)] = 2
    cost[(0, 3)] = 5
    cost[(1, 6)] = 1
    cost[(3, 1)] = 5
    cost[(5, 2)] = 6
    cost[(5, 6)] = 3
    cost[(6, 4)] = 7

    # goal state
    goal = []
    goal.append(6)

    # get the answer
    answer = uniform_cost_search(goal, 0)

    # print the answer
    print("Minimum cost from 0 to 6 is = ", answer[0])

def AO():
    # Function to calculate the cost for a given condition
    def Cost(H, condition, weight=1):
        cost = {}
        
        # Check for 'AND' condition
        if 'AND' in condition:
            AND_nodes = condition['AND']
            Path_A = ' AND '.join(AND_nodes)
            PathA = sum(H[node] + weight for node in AND_nodes)
            cost[Path_A] = PathA
        
        # Check for 'OR' condition
        if 'OR' in condition:
            OR_nodes = condition['OR']
            Path_B = ' OR '.join(OR_nodes)
            PathB = min(H[node] + weight for node in OR_nodes)
            cost[Path_B] = PathB
        
        return cost

    # Function to update the cost for each node based on the given conditions
    def update_cost(H, Conditions, weight=1):
        Main_nodes = list(Conditions.keys())
        Main_nodes.reverse()
        least_cost = {}
        
        for key in Main_nodes:
            condition = Conditions[key]
            print(key, ':', Conditions[key], '>>>', Cost(H, condition, weight))
            c = Cost(H, condition, weight)
            H[key] = min(c.values())
            least_cost[key] = Cost(H, condition, weight)
        
        return least_cost

    # Function to print the shortest path
    def shortest_path(Start, Updated_cost, H):
        Path = Start
        
        if Start in Updated_cost.keys():
            Min_cost = min(Updated_cost[Start].values())
            key = list(Updated_cost[Start].keys())
            values = list(Updated_cost[Start].values())
            Index = values.index(Min_cost)
            
            # Find minimum path key
            Next = key[Index].split()
            
            # Add to path for OR path
            if len(Next) == 1:
                Start = Next[0]
                Path += '<--' + shortest_path(Start, Updated_cost, H)
            # Add to path for AND path
            else:
                Path += '<--(' + key[Index] + ') '
                Start = Next[0]
                Path += '[' + shortest_path(Start, Updated_cost, H) + ' + '
                Start = Next[-1]
                Path += shortest_path(Start, Updated_cost, H) + ']'
        
        return Path


    # Initial values for nodes and conditions
    H = {'A': -1, 'B': 5, 'C': 2, 'D': 4, 'E': 7, 'F': 9, 'G': 3, 'H': 0, 'I': 0, 'J': 0}

    Conditions = {
        'A': {'OR': ['B'], 'AND': ['C', 'D']},
        'B': {'OR': ['E', 'F']},
        'C': {'OR': ['G'], 'AND': ['H', 'I']},
        'D': {'OR': ['J']}
    }

    # Weight for the calculation
    weight = 1

    # Print updated cost
    print('Updated Cost :')
    Updated_cost = update_cost(H, Conditions, weight=1)
    print('*' * 75)

    # Print the shortest path
    print('Shortest Path :\n', shortest_path('A', Updated_cost, H))



