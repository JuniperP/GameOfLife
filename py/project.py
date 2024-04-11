""" This function randomly generates a world for Conway's game of life.
PARAMETERS:
    wsize - The world is represented by a wsize x wsize list
    p1 - Proportion of cells that should be 1 (alive) when the program starts

RETURNS:
    world - A wsize x wsize list of 1s and 0s
"""
def generateRandomWorld(wsize): #Generates a random number of cells alive and dead based on the given variables.
  print("***************")
  p1 = float(input("Enter proportion (a number between 0 and 1) of cells that should start as alive. "))
  world = []
  for i in range(wsize):
    world.append(random.choices([0,1],weights=(1-p1,p1),k=wsize)) #adds alive/dead cells to the blank list based on the percentage the user gives.
    #printWorld(world)
  return world



def pulsar(wsize):

  #Below is the design for the pulsar

  pulsar = [[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,

        0.],

       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,

        0.],

       [0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 1., 1., 1., 0., 0., 0.,

        0.],

       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,

        0.],

       [0., 0., 1., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 1., 0.,

        0.],

       [0., 0., 1., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 1., 0.,

        0.],

       [0., 0., 1., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 1., 0.,

        0.],

       [0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 1., 1., 1., 0., 0., 0.,

        0.],

       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,

        0.],

       [0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 1., 1., 1., 0., 0., 0.,

        0.],

       [0., 0., 1., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 1., 0.,

        0.],

       [0., 0., 1., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 1., 0.,

        0.],

       [0., 0., 1., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 1., 0.,

        0.],

       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,

        0.],

       [0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 1., 1., 1., 0., 0., 0.,

        0.],

       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,

        0.],

       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,

        0.]]

#This creates a blank world to implement the design onto
  pworld = [[0]*wsize for i in range(wsize)]
  rows,cols = len(pulsar),len(pulsar[0])

#The for loops place the design into the world by iterating through the rows and columns
  for i in range(rows):
    for j in range(cols):
      pworld[(i+wsize//2)-len(pulsar)//2][(j+wsize//2)-len(pulsar)//2]= pulsar[i][j]
  return pworld

def glidergun(wsize):

#Here's the design for the glider gun

  glider = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

#This again creates the new world

  pworld = [[0]*wsize for i in range(wsize)]
  rows,cols = len(glider),len(glider[0])

#Iterating through the rows and lists to implement the design

  for i in range(rows):
    for j in range(cols):
      pworld[i][j] = glider[i][j]
  return pworld

""" This function prints a 2d list of 0s and 1s in rows and columns.
PARAMETERS:
    world - a list of 0s and 1s
"""
def printWorld(world):
  for line in world:
    print(line)


""" This function displays a list of 2d worlds of 0s and 1s as black and white squares.
PARAMETERS:
    worlds - a list of worlds of 0s and 1s
"""
def displayWorld(worlds):
    for world in worlds:
        plt.imshow(world,cmap=plt.cm.gray)
        plt.show()
        plt.pause(0.1)
        plt.close()

""" This function counts the number of 1s among the eight neighbors
    of cell at world[row][col].  Neighborhoods wrap at the edges of the list.
PARAMETERS:
    world - a 2d list of 0s and 1s
    row, col - the position in the world to check
RETURNS:
    numNeighbors - the number of neighbors equal to 1
"""

def countNeighbors(world, row, col):
    # Determine the number of rows and cols in the world.
    rows = len(world)
    cols = len(world[0])

    # Determine what the next and previous row and column are
    # If the specified cell is on the border, its neighborhood
    # will wrap to the other border

    nextRow = (row+1)%rows
    prevRow = (row-1)%rows
    nextCol = (col+1)%cols
    prevCol = (col-1)%cols

    # COMPLETE THE CODE BELOW TO CALCULATE THE NUMBER OF NEIGHBORS THAT ARE 1s.
    # Add the three neighbor cells in the previous row to numNeighbors
    numNeighbors = world[prevRow][prevCol] + world[prevRow][col] + world[prevRow][nextCol]

    # Add the two neighbors in the same row to numNeighbors
    numNeighbors += world[row][prevCol]+ world[row][nextCol]

    # Add the three neighbor cells in the next row to numNeighbors
    numNeighbors += world[nextRow][prevCol] + world[nextRow][col] + world[nextRow][nextCol]

    return numNeighbors

""" This function checks to see if a cell should live
PARAMETERS:
    world - A 2d list of 0s and 1s
    row, col - The position in the world to check
RETURNS:
    1 if the cell should live
    0 otherwise
"""
def isAliveHigh(world, row, col): #A separate function for the HighLife rule variation so that the user has the ability to choose which ruleset they want.

    # Use the countNeighbors function
    numNeighbors = countNeighbors(world,row,col)
    #print(numNeighbors)

    if world[row][col] == 1:
      if (numNeighbors == 2 or numNeighbors == 3):
        return 1
      else:
        return 0
    else:
      if (numNeighbors == 3 or numNeighbors == 6): #HIGHLIFE RULE IMPLEMENTED: B36/S23. Cells are born when there are 3 neighbors or 6 neighbors exactly.
        return 1
      else:
        return 0

  #This alters the original predestined evolution of the designs and creates a wildly different outcome than the standard rules display.

def isAlive(world, row, col): #This is the original isAlive function.

    numNeighbors = countNeighbors(world,row,col)
    #print(numNeighbors)
    if world[row][col] == 1:
      if (numNeighbors == 2 or numNeighbors == 3):
        return 1
      else:
        return 0
    else:
      if (numNeighbors == 3):
        return 1
      else:
        return 0


    """ If the current cell is alive:
            if it has 2 or 3 neighbors it should live on (stasis) (ie, return 1);
            otherwise it should die (over- or underpopulation) (ie, return 0)
        If the current cell is empty:
            if it has exactly 3 neighbors, it should become alive (reproduction) (return 1)
            otherwise it remains dead (return 0)
    """


    """ This function runs the game of life simulation
    PARAMETERS:
    wsize - The world is represented by a square wsize list
    gens - The number of generations to simulate
    prop_alive - Proportion of cells that should be 1 when the program starts
                 This should be a real number in the range [0, 1].
"""



def generateWorld(wsize): #Asks the user which type of world they'd like to start with and proceeds based on what is inputted.
  whichworld = (input("What type of world would you like to generate? glider gun, pulsar, or random: "))
  if whichworld == "pulsar":
    wo = pulsar(wsize)
  if whichworld == "glider gun":
    wo = glidergun(wsize)
  if whichworld == "random":
    wo = generateRandomWorld(wsize)
  return wo


def simulation(wsize,gens):

    # Generate the world

    world = generateWorld(wsize) #uses the new function to determine which type of rule.

    #Create a list of worlds, 1 for the initial world, plus 1 for each generation
    worlds = [0]*(gens+1)  #initial gen needs room so plus one
    worlds[0] = world

    rules = input("Which rule set would you like to play with? Standard or HighLife?")
    #Above asks the user what type of rules they want in their world.

    # Loop through each generation
    for gen in range(gens):
      nextWorld = [[0]*wsize for i in range(wsize)]  # A list of 0s for the next gen
      rows,cols = len(world),len(world[0])

        # FILL IN THE CODE HERE
      for i in range(rows):
        for j in range(cols):
          if rules == "Standard": #Creation of world based on standard/regular rules.
            if isAlive(world,i ,j) == 1:
              nextWorld[i][j] = 1
            else:
              nextWorld[i][j] = 0
          elif rules == "HighLife": #Creation of world based on HighLife rules.
            if isAliveHigh(world,i ,j) == 1:
              nextWorld[i][j] = 1
            else:
              nextWorld[i][j] = 0

        """ For every element in the world_next (ie, use a nested for loop)
        Determine whether it should be alive or dead (set it to 1 or 0)
        (Use the isAlive function to handle this)"""

      world = nextWorld.copy()
      worlds[gen+1] = nextWorld

    # Save the current world in the list to be displayed

    # Return the list of worlds to be displayed
    return worlds
