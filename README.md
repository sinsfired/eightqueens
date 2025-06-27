# eightqueens

This is my first GitHub repo on the Eight Queens problem using Basic Hill Climbing and Random Restart Hill Climbing algorithms

Objective: Implement and analyze Basic Hill Climbing and Random restart hill climbing to solve 8 queens problem. Place eight queens on a chessboard such that no two queens threaten each other (no queens share the same row, column, or diagonal)

Algorithms Used:
1.	Basic Hill Climbing
Start with one queen randomly placed in each column
Heuristic function = number of attacking pairs of queens
Move queens in columns to reduce the heuristic until:
- total attacking is lowest ( i.e heuristic = 0 ) or,
- nothing better is found, i.e no better neighbours (local minimum)

2.	Random restart hill climbing
Solves the problem of getting stuck in local minima
Repeatedly restarts hill climbing algorithm from random initial state until solution is found


State Representation
Each index represents a column, and the value at that index represent the row the queen is in that column
eg: [0,7,1,3,2,0,0,5]


Heuristic Function
Calculates the number of pairs of queens attacking each other
Goal is to reduce this  value to 0.

Recent Features Added:
Imporved board display using spaces
Clears the console screen between random restarts for a cleaner view
Displays heuristic trend at each step showing how numbr of conflicts decrease over time
