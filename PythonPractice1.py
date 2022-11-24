"""
As a part of the route planner, the route_exists method is used as a quick filter if the destination is reachable, before using more computationally intensive procedures for finding the optimal route.
The roads on the map are rasterized and produce a matrix of boolean values - True if the road is present or False if it is not. 
The roads in the matrix are connected only if the road is immediately left, right, below or above it.

Finish the route_exists method so that it returns True if the destination is reachable or False if it is not. 
The from_row and from_column parameters are the starting row and column in the map_matrix. 
The to_row and to_column are the destination row and column in the map_matrix. 
The map_matrix parameter is the above mentioned matrix produced from the map.

For example, for the given rasterized map, the code below should return True since the destination is reachable:

map_matrix = [
    [True, False, False],
    [True, True, False],
    [False, True, True]
];

route_exists(0, 0, 2, 2, map_matrix)


#Current Solution:
class RouteFinder:
    def __init__(self,s_row,s_col,d_row,d_col,matrix):
        self.matrix=matrix
        self.s_row=s_row
        self.s_col=s_col

        self.d_row=d_row
        self.d_col=d_col
        
        self.visited=[ [False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.visited[s_row][s_col]=True
        self.stack=[(s_row,s_col)]

    def valid_move(self,next_row,next_column):
        #print("IN valid Check",next_row," ",next_column)
        if next_row < 0 or next_row >= len(self.matrix) or next_column < 0 or next_column>=len(self.matrix[0]):
            return False
        if self.visited[next_row][next_column]: #already visted node
            return False
        if not self.matrix[next_row][next_column]: #path not exsist
            return False
        return True
    def reached(self,c_row,c_col):
        #print("IN Reached Check",c_row," ",c_col)
        if c_row == self.d_row and c_col == self.d_col:
            return True
        return False

    
    def find_route(self):
        
        if len(self.stack): #non empty stack
            cur_row,cur_col=self.stack.pop()
            if self.reached(cur_row+1,cur_col) and self.valid_move(cur_row+1,cur_col):
                return True
            elif self.reached(cur_row,cur_col+1) and self.valid_move(cur_row,cur_col+1):
                return True
            elif self.reached(cur_row-1,cur_col) and self.valid_move(cur_row-1,cur_col):
                return True
            elif self.reached(cur_row,cur_col-1) and self.valid_move(cur_row-1,cur_col):
                return True

            elif self.valid_move(cur_row+1,cur_col):
                self.stack.append((cur_row+1,cur_col))
                self.visited[cur_row+1][cur_col]=True
                #print("STACK:",self.stack)
                #print("Visited:",self.visited)
                return self.find_route()
            
            elif self.valid_move(cur_row,cur_col+1):
                self.stack.append((cur_row,cur_col+1))
                self.visited[cur_row][cur_col+1]=True
                #print("STACK:",self.stack)
                #print("Visited:",self.visited)
                return self.find_route()

            elif self.valid_move(cur_row-1,cur_col):
                self.stack.append((cur_row-1,cur_col))
                self.visited[cur_row-1][cur_col]=True
                #print("STACK:",self.stack)
                #print("Visited:",self.visited)
                return self.find_route()

            elif self.valid_move(cur_row,cur_col-1):
                self.stack.append((cur_row,cur_col-1))
                self.visited[cur_row][cur_col-1]=True
                #print("STACK:",self.stack)
                #print("Visited:",self.visited)
                return self.find_route()

        #stack empty no path found
        return False
def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    if from_row < 0 or from_row > len(map_matrix):
        return False
    if to_row < 0 or to_row > len(map_matrix):
        return False
    if from_column < 0 or from_column > len(map_matrix[0]):
        return False
    if to_column < 0 or to_column > len(map_matrix[0]):
        return False
    r=RouteFinder(from_row, from_column, to_row, to_column, map_matrix)
    if not r.matrix[from_row][from_column] or not r.matrix[to_row][to_column]:
        return False
    return r.find_route()

if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ];

    print(route_exists(0, 0, 2, 2, map_matrix))

"""
class RouteFinder:
    def __init__(self,s_row,s_col,d_row,d_col,matrix):
        self.matrix=matrix
        self.s_row=s_row
        self.s_col=s_col

        self.d_row=d_row
        self.d_col=d_col
        
        self.visited=[ [False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        #self.visited[s_row][s_col]=True
        self.stack=[(s_row,s_col)]

    def valid_move(self,next_row,next_column):
        print("IN valid Check",next_row," ",next_column)
        if next_row < 0 or next_row >= len(self.matrix) or next_column < 0 or next_column>=len(self.matrix[0]):
            return False
        if self.visited[next_row][next_column]: #already visted node
            return False
        if not self.matrix[next_row][next_column]: #path not exsist
            return False
        return True
    def reached(self,c_row,c_col):
        print("IN Reached Check",c_row," ",c_col)
        if c_row == self.d_row and c_col == self.d_col:
            return True
        return False

    
    def find_route(self):
        
        if len(self.stack): #non empty stack
            cur_row,cur_col=self.stack.pop()
            self.visited[cur_row][cur_col]=True
            if self.reached(cur_row+1,cur_col):
                return True
            elif self.reached(cur_row,cur_col+1):
                return True
            elif self.reached(cur_row-1,cur_col):
                return True
            elif self.reached(cur_row,cur_col-1):
                return True
            else: #Add all it's child to stack
                if self.valid_move(cur_row+1,cur_col):
                    self.stack.append((cur_row+1,cur_col))
                if self.valid_move(cur_row,cur_col+1):
                    self.stack.append((cur_row,cur_col+1))
                if self.valid_move(cur_row-1,cur_col):  
                    self.stack.append((cur_row-1,cur_col))
                if self.valid_move(cur_row,cur_col-1):
                    self.stack.append((cur_row,cur_col-1))                
                self.find_route()
            
            print("STACK:",self.stack)
            print("Visited:",self.visited)
                
        #stack empty no path found
        return False

def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    if from_row < 0 or from_row > len(map_matrix):
        return False
    if to_row < 0 or to_row > len(map_matrix):
        return False
    if from_column < 0 or from_column > len(map_matrix[0]):
        return False
    if to_column < 0 or to_column > len(map_matrix[0]):
        return False

    r=RouteFinder(from_row, from_column, to_row, to_column, map_matrix)
    if not r.matrix[from_row][from_column] or not r.matrix[to_row][to_column]:
        print("Invalid Source or Desti:",r.matrix[from_row][from_column]," ",r.matrix[to_row][to_column])
        return False
    
    return r.find_route()
        
if __name__ == '__main__':
    map_matrix = [
        [True, True, True],
        [True, True, True],
        [True, True, True]
    ];
    map_matrix = [
        [True,False,True,True,False,False,False],
        [True,False,True,True,False,False,False],
        [True,True,True,True,False,False,False],
        [False,False,False,True,False,False,False],
        [False,False,True,True,False,False,False],
        [True,True,True,False,False,False,False],
        [True,False,False,False,False,False,False],
        [True,True,False,False,False,False,False],
        [False,True,False,False,False,False,False],
        [False,True,False,False,False,False,False],
        [False,True,False,False,False,False,False],
        [False,True,False,False,False,False,False],
        [False,True,False,False,False,False,False],
        [False,True,False,False,False,False,False],
        [False,True,False,False,False,False,False],
        [False,True,True,True,True,True,True],
        [False,False,False,False,False,False,True],
    ];
    map_matrix = [
        [True, False, True],
        [True, True, True],
        [True, True, True]
    ];  
    print(route_exists(2, 2, 0, 0, map_matrix))