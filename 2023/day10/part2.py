import numpy as np
import numpy as np
from enum import Enum
import networkx as nx
from collections import deque

def scanning_area(path):
    print(f"Reading {path} file")

    histories = []
    with open(path, "r") as f:
        lines = [linea.strip() for linea in f.readlines()]        
        board = np.array(np.zeros((len(lines), len(lines[0])))).astype(str)
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char == "\n":
                    continue
                board[i][j] = str(char)
        
        f.close()
    return board


class Pipe(Enum):
    VERTICAL = "|"
    HORIZONTAL = "-"
    NORTH_EAST = "L"
    NORTH_WEST = "J"
    SOUTH_WEST = "7"
    SOUTH_EAST = "F"
    START = "S"
    GROUND = "."

    def get_posible_directions(self, pipe, x, y):
        if pipe == Pipe.VERTICAL:
            return [(x+1, y), (x-1, y)]
        elif pipe == Pipe.HORIZONTAL:
            return [(x, y+1), (x, y-1)]
        elif pipe == Pipe.NORTH_EAST:
            return [(x-1, y), (x, y+1)]
        elif pipe == Pipe.NORTH_WEST:
            return [(x-1, y), (x, y-1)]
        elif pipe == Pipe.SOUTH_WEST:
            return [(x+1, y), (x, y-1)]
        elif pipe == Pipe.SOUTH_EAST:
            return [(x+1, y), (x, y+1)]
        elif pipe == Pipe.START:
            return [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]
        elif pipe == Pipe.GROUND:
            return []


class GraphConnected():
    def __init__(self, board):
        self.board = board
        self.visited = np.zeros_like(board)
        self.graph = nx.Graph()
        self.start = np.where(board == "S")
        self.new_board = np.zeros_like(board)
        self.new_board[self.start[0][0]][self.start[1][0]] = 0
        self.positions = []
        self.positions.append([self.start[0][0], self.start[1][0]])
        # self.visited[self.start[0][0]][self.start[1][0]] = "1"

    def dfs(self, x, y, value):
        pipe = Pipe(self.board[x][y])
        posible_positions = pipe.get_posible_directions(pipe, x, y)

        self.visited[x][y] = "1"

        # recorrer hijos hasta que se encuentre con uno ya visitado, cada nodo unicamente se conecta con otros dos nodos
        for pos in posible_positions:
                             
            if self.visited[pos[0]][pos[1]] != "1":
                next_pipe = Pipe(self.board[pos[0]][pos[1]])
                if next_pipe == Pipe.GROUND:
                    continue

                # add edge with weight
                self.positions.append([pos[0], pos[1]])
                self.graph.add_edge((x, y), (pos[0], pos[1]), weight=value + 1)
                self.dfs(pos[0], pos[1], value + 1)
                
    def bfs(self, start_x, start_y, initial_value):
        """
        En este caso no funciona pq si hay mas de dos caminos se van a superponer los valores
        """
        queue = deque()  # Inicializa la cola
        queue.append((start_x, start_y, initial_value))  # Agregar el punto inicial a la cola
        self.visited[start_x][start_y] = "1"  # Marcar el inicio como visitado

        while queue:  # Mientras haya elementos en la cola
            x, y, value = queue.popleft()  # Extraer el primer elemento de la cola

            pipe = Pipe(self.board[x][y])
            # print(f"Pipe: {pipe}")
            posible_positions = pipe.get_posible_directions(pipe, x, y)

            for pos in posible_positions:
                if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(self.board) or pos[1] >= len(self.board[0]):
                    continue

                if self.visited[pos[0]][pos[1]] != "1":
                    next_pipe = Pipe(self.board[pos[0]][pos[1]])
                    if next_pipe == Pipe.GROUND:
                        continue

                    # print("Posible positions: ", Pipe(self.board[pos[0]][pos[1]]))
                    # Agregar la arista con el peso
                    self.new_board[pos[0]][pos[1]] = value + 1
                    self.graph.add_edge((x, y), (pos[0], pos[1]), weight=value + 1)
                    self.visited[pos[0]][pos[1]] = "1"  # Marcar la posición como visitada
                    queue.append((pos[0], pos[1], value + 1))  # Agregar el nuevo nodo a la cola

    def get_greater_weight(self):
        greater = 0
        for edge in self.graph.edges(data=True):
            if edge[2]["weight"] > greater:
                greater = edge[2]["weight"]
        return greater
    
    
    def shoelace_theorem(self, positions: list[list[int]]) -> int:
        """
        Función que calcula el área de un polígono a partir de sus vértices
        utilizando el teorema de la zapatilla.
        """
        #A function to apply the Shoelace algorithm
        numberOfVertices = len(positions)
        sum1 = 0
        sum2 = 0
        
        for i in range(0,numberOfVertices-1):
            sum1 = sum1 + positions[i][0] *  positions[i+1][1]
            sum2 = sum2 + positions[i][1] *  positions[i+1][0]
        
        #Add xn.y1
        sum1 = sum1 + positions[numberOfVertices-1][0]*positions[0][1]   
        #Add x1.yn
        sum2 = sum2 + positions[0][0]*positions[numberOfVertices-1][1]   
        
        area = abs(sum1 - sum2) / 2
        return area
    
    def pick_theorem(self, A, b):
        """
        A = i + b/2 - 1
        A: Area of the polygon
        b: number of points with integer coordinates on the boundary of the polygon
        i: number of points with integer coordinates inside the polygon
        """

        i = (A + 1)*2 - b
        print("A", 10 + 165/2 -1)
        print("b", 84 + 1 - 10 )
        return i


board = scanning_area("input1.txt")

from sys import setrecursionlimit

setrecursionlimit(30000)
graph = GraphConnected(board)
graph.dfs(graph.start[0][0], graph.start[1][0], 1)
print(graph.get_greater_weight() // 2) 
print(graph.shoelace_theorem(graph.positions))
print(graph.pick_theorem(2.5, len(graph.positions)))
# busco el camino máximo y se divide entre ods ya que será a la mitad del camino donde se encuentran los dos caminos