### Nemoization and Tabulation, are the core of DP
## Recursion forms the basis of these 2 techniques



# Obtain the 5th number in the Fibo sequence
#Tracing tree
### Two types of complexity: Time and Space
## Space complexity uses memory storage a LOT
## as number of elements in a recursion go up the number of times the function is called exponentially increases
## Different types of time complexity: ex. the quicksort function we did in recursions
# time complexities we want to achieve are linear or less

# steps of dynamic programming:
#       1) break down the complex problem into simpler solutions
#       2) find optimal solutions to the sub problems
#       3) store the results of the sub-problems - memoization
#       4) resue the results so that a given sub-problem isn't calculated more than once
#       5) calculate the result of the complex problem
## These are aplicable to problems which have:
#       Overlapping sub-problems
#       final solution can be obtained by combining optimal solutions of sub-problems
# Dynamic programming is better used for opimization problems (min. possible time or use min, possible memory space)


# Longest Common Subsequence (LCS)
#