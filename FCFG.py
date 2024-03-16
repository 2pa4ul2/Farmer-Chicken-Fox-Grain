#PAUL ADRIAN TORRES
#BSCS - 3B

class RiverCrossingSolver:
    def __init__(self, initial, goal):
        self.initial, self.goal, self.state_stack = initial, goal, [initial]   #INIT ALL STATES

    def goal_reached(self, state):                                              #IF THE STATE IS REACHED RETURN TRUE
        return state == self.goal

    def generate_next_state(self, current_state, index):                        #CREATE STATE BASED ON THE CURRENT STATE
        new_state = list(current_state)
        new_state[3] = 'Right' if new_state[3] == 'Left' else 'Left'

        if new_state[3] == 'Left' and not self.state_valid(new_state):
            new_state[index] = 'Right' if new_state[index] == 'Left' else 'Left'
        elif new_state[3] == 'Right':
            new_state[index] = 'Right' if new_state[index] == 'Left' else 'Left'

        return new_state

    def state_valid(self, current_state):                                                                       #STATE VALIDITY CHECK
        return not ((current_state[0] == current_state[1] and current_state[3] != current_state[0]) or          #The fox and the chicken are alone together
                    (current_state[1] == current_state[2] and current_state[3] != current_state[1]))            #The chicken and the grain are alone together

    def unique_state(self, current_state):                                                                      #CHECKING STATE IF NOT VISITED MAKINF SURE ITS UNIQUE
        return current_state not in self.state_stack

    def step_state(self, state):                                                                                #PRINT CURRENT STATE
        labels = ['Fox', 'Chicken', 'Grain', 'Farmer']
        left_side = f"LEFT LAND: {', '.join([f'{labels[i]}({state[i]})' for i in range(4) if state[i] == 'Left'])}"
        right_side = f"RIGHT LAND: {', '.join([f'{labels[i]}({state[i]})' for i in range(4) if state[i] == 'Right'])}"
        print(f"{left_side} ||=========RIVER========|| {right_side}")

    def dfs(self):                                                                                              #DFS FUNCTION
        while not self.goal_reached(self.state_stack[-1]):
            current_state = self.state_stack[-1]

            farmer_location = current_state[3]
            next_state_found = False

            for i, item_location in enumerate(current_state):                                                   #STACK APPEND
                if item_location == farmer_location:
                    next_state = self.generate_next_state(current_state, i)
                    if self.state_valid(next_state) and self.unique_state(next_state):
                        self.state_stack.append(next_state)
                        next_state_found = True
                        break

            if not next_state_found:                                                                            #IF VALID STATE IS NOT FOUND THEN BACKTRACK BY POPPING  CURRENT STATE
                self.state_stack.pop()

    def solution(self):                                                                                         #PRINTING AND SOLVING
        self.dfs()
        for i, state in enumerate(self.state_stack):
            print(f"Step {i + 1}")
            self.step_state(state)


initial_state = ['Left', 'Left', 'Left', 'Left']                                                                #INITIAL STATE
goal_state = ['Right', 'Right', 'Right', 'Right']                                                               #GOAL STATE

solver = RiverCrossingSolver(initial_state, goal_state)
solver.solution()
