# A.D.R Fernandopulle_w1810201_2019711

# Algorithms: Theory, Design and Implementation- Coursework

from time import time


class Maze:
    def __init__(self, row, col, distance, direction):
        self.row = row
        self.col = col
        self.distance = distance
        self.direction = direction

    def __repr__(self):
        return f"Maze({self.row}, {self.col}, {self.distance}, {self.direction})"


def getShortestPath(start, grid):
    # Finds the shortest path,return shortestPath : list

    # To maintain location visit status
    visited = [[False for _ in range(len(grid[0]))]
               for _ in range(len(grid))]

    # ========= BFS Algorithm : Shortest Path through BFS Brute Force ======== #
    currentPosition = start
    queue = [currentPosition]  # Starting to explore : Current Position -> Start
    visited[currentPosition.row][currentPosition.col] = True
    st_row = str(currentPosition.row)
    st_col = str(currentPosition.col)

    # Starting Point
    currentPosition.direction += [
        st_row + st_col + "|" + "Start From      (" + str(currentPosition.col + 1) + "," + str(
            currentPosition.row + 1) + ")"]

    while len(queue) != 0:
        currentPosition = queue.pop(0)

        # Finish node found;
        if (grid[currentPosition.row][currentPosition.col] == 'F'):
            currentPosition.direction += ["00|Done!"]
            return currentPosition.direction

        # Move until reach a rock
        # track the current cell row and column

        # maze goes left
        if validateMove(currentPosition.row, currentPosition.col - 1, grid, visited):
            row = str(currentPosition.row)
            col = str(currentPosition.col - 1)

            queue.append(Maze(currentPosition.row, currentPosition.col - 1, currentPosition.distance + 1,
                              currentPosition.direction + [
                                  row + col + "|" + "Move Left From  (" + str(currentPosition.col + 1) + "," + str(
                                      currentPosition.row + 1) + ")"]))

            visited[currentPosition.row][currentPosition.col - 1] = True

        # maze goes right
        if validateMove(currentPosition.row, currentPosition.col + 1, grid, visited):
            row = str(currentPosition.row)
            col = str(currentPosition.col + 1)

            queue.append(Maze(currentPosition.row, currentPosition.col + 1, currentPosition.distance + 1,
                              currentPosition.direction + [
                                  row + col + "|" + "Move Right From (" + str(currentPosition.col + 1) + "," + str(
                                      currentPosition.row + 1) + ")"]))

            visited[currentPosition.row][currentPosition.col + 1] = True

        # maze goes up
        if validateMove(currentPosition.row - 1, currentPosition.col, grid, visited):
            row = str(currentPosition.row - 1)
            col = str(currentPosition.col)

            queue.append(Maze(currentPosition.row - 1, currentPosition.col, currentPosition.distance + 1,
                              currentPosition.direction + [
                                  row + col + "|" + "Move Up From    (" + str(currentPosition.col + 1) + "," + str(
                                      currentPosition.row + 1) + ")"]))

            visited[currentPosition.row - 1][currentPosition.col] = True

        # maze goes down
        if validateMove(currentPosition.row + 1, currentPosition.col, grid, visited):
            row = str(currentPosition.row + 1)
            col = str(currentPosition.col)

            queue.append(Maze(currentPosition.row + 1, currentPosition.col, currentPosition.distance + 1,
                              currentPosition.direction + [
                                  row + col + "|" + "Move Down From  (" + str(currentPosition.col + 1) + "," + str(
                                      currentPosition.row + 1) + ")"]))

            visited[currentPosition.row + 1][currentPosition.col] = True

    return "Search Failed!"


# checking where the  move of the maze is valid or not
def validateMove(x, y, grid, visited):
    if ((x >= 0 and y >= 0) and
            (x < len(grid) and y < len(grid[0])) and
            (grid[x][y] != '0') and (visited[x][y] == False)):
        return True
    return False


def points(start, finish, grid):
    # Finds the positions of Start and Finish in the Map
    # Assuming S and F will be in the Map in all instances (Otherwise Terminates)
    # While registering start and finish, the function also traverses through the entire map.
    # The idea behind it is to allow keep a track of the paths already explored when performing BFS later on.

    startFound = False  # Flag
    finishFound = False  # Flag

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "S":  # Start : Register the row and col values
                start.row = row
                start.col = col
                startFound = True
            if grid[row][col] == "F":  # Finish: Register the row and col values
                finish.row = row
                finish.col = col
                finishFound = True
            if startFound and finishFound:  # Start and Finish nodes found and exiting from the maze
                break

    # Start and Finish nodes not found program will end with a message
    if not startFound:
        print("start not found")
        exit()

    if not finishFound:
        print("finish not found")
        exit()

    return start, finish


def parser(txtGridFile):
    # Takes in a text file and converts it into a list of lists
    # Creates start and finish Point objects

    gridFile = open(txtGridFile)

    # removing the white space
    # read the file line by line and adding to the list

    grid = [list(row.strip()) for row in gridFile.readlines()]
    print()

    width = len(grid[0])  # Assuming the input Map contains at least 1 row : Getting num of cols
    height = len(grid)  # num of rows
    start = Maze(0, 0, 0, [])  # Creates start and finish Point objects
    finish = Maze(0, 0, 0, [])
    return grid, start, finish, height, width  # Returns mapObj, start, finish, height, width


# printing the output of the maze
def printMaze(grid, nodes):
    nodes.remove("00")  # removing the element to print finish as Done
    print()
    print(" -----PATH-----")
    print()

    # travel through a loop to print the maze
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            item = str(row) + str(col)
            if item in nodes:
                print("+", end=" ")  # replacing "." with "+" of the shortest path

            else:
                print(grid[row][col], end=" ")
        print()


# main method
def main():
    global t1
    global t2
    node = []
    filepath = input('Enter file name: ')
    t1 = time()  # start time
    grid, start, finish, height, width = parser(filepath)
    start, finish = points(start, finish, grid)
    totalPath = getShortestPath(start, grid)

    print("----DIRECTION----")
    print()
    for eachMove in totalPath:
        # exit the programme
        # taking the status of the path and splitting it into two half one for columns and rows and other for the print the values
        line_data = eachMove.split('|')
        node.append(line_data[0])
        print(line_data[1])
        t2 = time()  # End time
    printMaze(grid, node)  # printing the grid
    print()
    elapsed = t2 - t1
    print('Elapsed time is %f seconds.' % elapsed)  # print time complexity


main()
