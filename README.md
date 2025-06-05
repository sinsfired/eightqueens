# eightqueens
This is my first GitHub repo about eight queens game

8 queens problem using Basic Hill Climbing and Random restart hill climbing

Objective: Implement and analyze Basic Hill Climbing and Random restart hill climbing to solve 8 queens problem. Goal is to find a pattern such that no two of the eight queens threaten each other.

Algorithms:
1.	Basic Hill Climbing
Place one queen in each column randomly
Heuristic function= number of attacking pairs ‘attack’
Move queens in columns until total attacking is lowest ( i.e 0 )OR
Stop when nothing better is found, i.e no better neighbours “local minimum”
2.	Random restart hill climbing
Use when stuck (problem of local minimum)
Restart hill algorithm from random initial state
Keep going until solution ( heuristic = 0)  is found


State = position of queen in x row of y column, represented as list of 8 numbers
Heuristic = how many queens are attacking each other
