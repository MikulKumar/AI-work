'''
Terminoligies:

-Agent: entity that preceives its environment and acts upon that environment 
-State: a cofiguration of the agent and its environment
-initial state: the state in which the agent begins
-actions: choices that can be made in a state  / actions
    -Actions(s): returns the set of actions that can be executed in state s 
-transition model: a descripition of what state results from performing any applicable action in any state
    -Result(s,a): returns the state resultimg from performing action a in state s. Input s: some state, Input a: some action
-state space: the set of all states reacheable from the initial state by any sequence of actions
-goal test: way to determine whether a given state is a goal state 
-path cost: numerical cost associated with a given path 
-solution: a sequence of actions that leads from the intial state to a goal state
-optimal solution: a solution that has the lowest path cost among all solutions 


Search problems main components:
-Initial state
-actions 
-transition model 
-goal test
-path cost function

node:
a data structure that keeps track of 
    - a state
    - a parent (node that generated this node)
    - an action (action applied to parent to get node)
    - a path cost (from initial state to node)

frontier
a data structure
    -represent all of the things that we could explore ,that we havent yet explored

Approach 
-start with a frontier that contains the initial state.
-Repeat:
    -If the frontier is empty, then no solution
    -Remove a node from the frontier
    -If node contains goal state, return the solution
    -Expand node, add resulting nodes to the frontier

eg problem:
Find a path from A to E:
    -Start with a frontier that contains the intial state
    -Repeat:
        -If the frontier is empty, then no solution
        -Remove a node from the frontier 
        -If node contains goal state, return the solution 
        -Expand node, add resulting nodes to the frontier.

The graph:
A-->B-->D--F
    |
    C-->E

some problems that can arise:
if the graph was something like:
    A<-->B-->D--F
         |
         C-->E
implying that i can go from A to B and back to B in a forever loop
because now there are three possible nodes i can go to from B ,which are A,C,D
as to before it was only D and C



Revised Approach:
-Start with a frontier that contains the intial state
-Start with an empty explored set
-Repeat:
    - If the frontier is empty, then no solution
    - Remove a node from the frontier 
    - If the node contains goal state, return the solution
    - Add the node to the explored set
    - Expand node, add resulting nodes to the frontier if they aren't already in the frontier or the explored set 


what order will we remove a node from the frontier, randomly? or some systematic way 

we use a data structure for this 

Stack:
- last-in first-out data type

when we use the stack approach to remove nodes from the frontier,
we basically go deep into one branch of the path and then back up to explore the other 
eg:
A-->B-->D--F
    |
    C-->E
The AI goes deep into D node till F and then backs up to B and explores the C branch till the end E, where we find the solution 

we call this algorithm a Depth-first Search

1)Depth First Search(DFS)
- search algorithm that always expands the deepest node in the frontier

this is just one of the algorithms we can use

2)Breadth-first search(BFS)
- search algorithm that always expands the shallowest node in the frontier

for this algorithm we use the data type:

Queue:
- first-in first-out data type
  

eg:
A-->B-->D--F
    |
    C-->E
we start with A then go to B from where we add C and D to the frontier , 
but as C was added first into the frontier first we explore that first and remove C to add E to the frontier 
but because D was added before E , we explore D first and remove D to add F 
now E was here before F so we explore E and find out that it matches the goal state
We have found our answer!!

DFS has memory savings comapred to BFS 
but BFS finds the most optimal path everytime while DFS might not 

but what if the algorithm knew which way to go like if the start is on the left side and the final destination 
is at the right side, how does the algorithm know to take a right turn instead of a left to reach the destination without exploring the wrong path

we humans can tell because of our intuition

How to add intiution to a algorithm?

-Uniformed search(blind search)
    - search stratergy that uses no problem-specific knowledge. 
    - cannot estimate how close a given state is to the goal 
    - systematic exploration without any "guidance"
    - eg: DFS, BFS

-Informed search
    - search stratergy that uses problem-specific knowledge to find soltions more efficiently 
    - uses heuristic functions to estimate how close a state is to the goal (way to estimate how close to the goal we are, but dont know the full path to it)
    - eg: Greedy best search, A* search

-Greedy best-first search 
    - search algorithm that expands the node that is closest to the goal, as estimated by a heuristic function h(n)
    - uses heuristic function/manhattan distance
        - it is a way to estimate how close we are to the goal
        - it uses coordinates, while ignoring the walls

    - not optimal, may give a response that is not the quickest path
    
-A* search 
    - search algorithm that expands node with lowest value of g(n) + h(n)

    g(n) = cost to reach node
    h(n) = estimate cost to goal
      
    -it is a optimal solution
    -but only optimal if:
    - h(n) is admissible (never overestimate the true cost)
    - h(n) is consistent (for every node n and successor n' with step cost c, h(n) <= h(n') + c)




Adversarial Search
- There are more than one agents , if i am trying to get to a objective , someone is tryig to stop me from getting there
- eg: a game, tic tac toe


-Minimax
    -"O" winning = -1 , "O" player is the min player
    -"draw" = 0
    -"X" winning = 1, "X" player is the max player

    we assign these player names because in 
    the Minimax function 
    - MAX- aims to maximize score
    - MIN- aims to minimize score
    - The possible options for the scores are [-1,0,1]


Game:
- S0: initial state
- Players(s): returns which player to move in state s 
- Actions(s): returns legal moves in state s 
- Result(s,a): returns state after action a taken in state s
- Terminal(s): checks if state s is a terminal state, kind of like a goal set 
- Ulility(s): final numerical value for terminal state s 

      | |
   ---+-+---
      | |
   ---+-+---
      | |

Minimax procedure
- given a state s:
    -MAX picks action a in Actions(S) that produces highest value of Min-Value(Results(s,a))
    -MIN picks action a in Actions(s) that produces smallest value of Max-Value(Result(s,a))

function Max-Value(state):
    if Terminal(state):
        return Utility(state)
    v = -infinity

    for action in Actions(state):
        v = Max(v,Min-Value(Result(state,action)))
    return v

function Min_value(state):
    if Terminal(state):
        return Utility(state)
    v = +infinity 
    for actions in Actions:
        v = Min(v,Max-Value(Result(state,action)))


this will take more space as the game gets bigger and bigger 
eg: chess ,which has a lot of more moves that we can make 


a way to optimize the minimax function

- Alpha-beta Pruning
    Alpha-beta pruning is an enhancement to the 
    minimax algorithm that significantly reduces 
    the number of nodes evaluated in the search 
    tree without affecting the final result. 
    It allows the AI to discard (or "prune") 
    entire branches of the search tree that 
    cannot possibly influence the final decision.

this still isnt the most optimal approach 
as the most possible configuration of a tic tac toe board is 288,000

compare that to a game of chess which is way more complex than tic tac toe
10**29000

so we use

Depth-Limited Minimax

this uses a 
evaluation function:
    function that estimates the expected utility of the game from a 
    given state
    
'''
