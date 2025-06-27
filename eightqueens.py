import random

WHITE_BG = "\033[47m"  # White background
BLACK_BG = "\033[100m" # Dark gray background
RESET = "\033[0m"      # Reset color

# Creates the chess board and randomly place the queen in each column
def createBoard(n):
    board = [' '] * n 
    for i in range(n):
        board[i] = [' '] * n #all rows initialised to dots
    for i in range(n):
        rand = random.randint(0, 7)
        board[rand][i] = 'Q' #queen sits in random row of column i
    return board

#function to print the board 
def printBoard(board):
    for i, row in enumerate(board):
        line = ""
        for j, cell in enumerate(row):
            bg = WHITE_BG if (i + j) % 2 == 0 else BLACK_BG
            content = f" {cell} "
            line += bg + content + RESET
        print(line)
    print()

#initialise all column values to 0 and then place 1 where the heuristic value (attack) is minimum 
def changeState(board, min_index, col):
    for row in range(len(board)):
        board[row][col] = ' '
    board[min_index][col] = 'Q'


def boardToState(board):
    state = [-1] * noOfQueens
    for col in range(noOfQueens): # each column
        for row in range(noOfQueens): # each row
            if board[row][col] == 'Q': # condition when queen is there
                state[col] = row
                break
    return state

# state to board format
def stateToBoard(state):
    board = [[0 for _ in range(noOfQueens)] for _ in range(noOfQueens)]
    for col in range(noOfQueens):
        board[state[col]][col] = 1
    return board

# Heuristic function: number of attacking pairs of queens
def heuristic(state):
    attacks = 0
    for i in range(noOfQueens):
        for j in range(i + 1, noOfQueens):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j): #same row or diagnol
                attacks += 1
    return attacks

# best neighbor by moving one queen in its column
def get_best_neighbor(state):
    neighbors = []
    min_h = float('inf') #initialise to big value infinity
    for col in range(noOfQueens):
        for row in range(noOfQueens):
            if state[col] != row: #in row= skip
                new_state = list(state)
                new_state[col] = row
                h = heuristic(new_state)
                if h < min_h:
                    neighbors = [new_state]
                    min_h = h
                elif h == min_h:
                    neighbors.append(new_state)
    if neighbors:
        return random.choice(neighbors), min_h
    return state, heuristic(state)

# basic hill climbing algorithm
def hill_climb(initial_state):
    current = initial_state
    current_h = heuristic(current)
    steps = 0
    heuristics = [current_h]

    print("Initial State:")
    displayStateAsBoard(current)
    print(f"Heuristic: {current_h}\n")
    
    while True:
        neighbor, neighbor_h = get_best_neighbor(current)
        if neighbor_h >= current_h: #no improvement then stop
            print("Local minimum reached.")
            break
        current = neighbor
        current_h = neighbor_h
        steps += 1
        heuristics.append(current_h)#track each heuristic
        print(f"Step {steps}: Heuristic = {current_h}")
        displayStateAsBoard(current)
    print("Heuristic trend during this run:",heuristics)
    return current, current_h, steps

# random restart hill climbing
def random_restart_hill_climb():
    total_steps = 0
    restarts = 0
    while True:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nRestart #{restarts + 1}")
        initial_state = [random.randint(0, noOfQueens - 1) for _ in range(noOfQueens)]
        solution, h, steps = hill_climb(initial_state)
        total_steps += steps
        if h == 0:
            break
        restarts += 1
    return solution, restarts, total_steps + restarts

# display board from state
def displayStateAsBoard(state):
    board = [[" " for _ in range(noOfQueens)] for _ in range(noOfQueens)]
    for col in range(noOfQueens):
        board[state[col]][col] = 'Q'
    printBoard(board)

# run the algorithm
noOfQueens = 8
solution, restarts, total_steps = random_restart_hill_climb()
print("\nSolution Found!\n")
displayStateAsBoard(solution)
print(f"Restarts: {restarts}")
print(f"Total Steps (incl. restarts): {total_steps}")