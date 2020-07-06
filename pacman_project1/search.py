# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import searchProblems
recnik = {}
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Najpre pretrazuje najdublje cvorove u stablu.

    Isprobajte i koristite sledece:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    # TODO 1: Implementirati DFS

    stack = util.Stack()
    stack.push((problem.getStartState(), [], []))
    while not stack.isEmpty():
        trenutni, akcije, visited = stack.pop()
        if problem.isGoalState(trenutni):
            return akcije

        for child, pravac, brPoteza in problem.getSuccessors(trenutni):
            if not child in visited:
                stack.push((child, akcije + [pravac], visited + [trenutni]))
                # akcije = akcije + [pravac]
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    queue.push((problem.getStartState(), [], []))
    expended = []

    while not queue.isEmpty():
        trenutni, akcije, curCost = queue.pop()

        if not trenutni in expended:
            expended.append(trenutni)

            if problem.isGoalState(trenutni):
                return akcije

            for child, pravac, brKoraka in problem.getSuccessors(trenutni):
                queue.push((child, akcije+ [pravac], curCost + [trenutni]))

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    akcije = []
    extended = {}
    cost = {}
    queue = util.PriorityQueue()
    parents = {}


    #Pocetno stanje tuple (x, y)
    start = problem.getStartState()
    # pozicija, pravac, cost
    queue.push((start, 'Undefined', 0), 0)
    # Ne znamo odakle smo dosli na pocetku
    extended[start] = 'Undefined'
    cost[start] = 0

    if problem.isGoalState(start):
        return akcije
    node_sol = None

    uslov = False
    while(queue.isEmpty() != True and uslov != True):
        node = queue.pop()
        extended[node[0]] = node[1]
        if problem.isGoalState(node[0]):
            node_sol = node[0]
            uslov = True
            break
        for elem in problem.getSuccessors(node[0]):
            if elem[0] not in extended.keys():
                # cost tacke i njenegov sledeci
                priority = node[2] + elem[2]
                # Ako je cena sledeceg svora vez izracunata prethodno
                # ako je nova cena veca preskoci
                if elem[0] in cost.keys():
                    if cost[elem[0]] <= priority:
                        continue
                # ako je nova cena izmeni je u queue i update-uj parent-a
                queue.push((elem[0], elem[1], priority), priority)
                cost[elem[0]] = priority
                parents[elem[0]] = node[0]

    # Vraca putanju akcije
    while(node_sol in parents.keys()):
        node_sol_prev = parents[node_sol]
        akcije.insert(0, extended[node_sol])
        node_sol = node_sol_prev

    return akcije

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    queue = util.PriorityQueue()
    queue.push((problem.getStartState(), [], 0),
               searchProblems.manhattanHeuristic(problem.getStartState(), problem.pacmanPosition))
    expended = set()

    while not queue.isEmpty():
        trenutni, akcije, curCost = queue.pop()
        uslov = False
        index = -1
        if not trenutni in expended:
            expended.add(trenutni)
            if problem.isGoalState(trenutni):  #
                for key in recnik.keys():
                    if recnik.get(key) == trenutni:
                        index = key

                if (index != -1):
                    if index == problem.agentIndex:
                        uslov = True

                else:
                    uslov = True
                if problem.gameState.getNumFood() <= problem.gameState.getNumAgents():
                    uslov = True
                # if trenutni not in recnik[problem.agentIndex]:
                if (uslov):
                    recnik[problem.agentIndex] = trenutni
                    # print(recnik)
                    return akcije

            for child, pravac, cena in problem.getSuccessors(trenutni):
                g = curCost + cena
                # curCost + cena, racuna cenu od pocetka do child cvora
                queue.push((child, akcije + [pravac], curCost + cena), g + searchProblems.manhattanHeuristic(child, problem.pacmanPosition))

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
