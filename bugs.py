
bugs_id2name = {1:'purple', 2:'green',3:'yellow', 4:'red'}
bugs_name2id = {name:id for id, name in bugs_id2name.items()}

# encode the bugs
PURPLE = 1 # purple bug
GREEN  = 2 # green and orange bug
YELLOW = 3 # yellow bug
RED    = 4 # lady bug

TOP    =  1 # top half of a bug
BOTTOM = -1 # bottom half of a bug

# tiles description from the image - considered 0 rotation
tiles= {
    1: {"top": TOP*PURPLE,    "bottom": BOTTOM*GREEN,   "left": TOP*YELLOW,   "right": BOTTOM*RED},
    2: {"top": TOP*YELLOW,    "bottom": BOTTOM*GREEN,   "left": TOP*RED,      "right": BOTTOM*YELLOW},
    3: {"top": TOP*GREEN,     "bottom": BOTTOM*PURPLE,  "left": BOTTOM*YELLOW,"right": TOP*RED},
    4: {"top": BOTTOM*GREEN,  "bottom": TOP*PURPLE,     "left": TOP*RED,      "right": TOP*YELLOW},
    5: {"top": TOP*RED,       "bottom": TOP*GREEN,      "left": TOP*PURPLE,   "right": BOTTOM*RED},
    6: {"top": TOP*GREEN,     "bottom": BOTTOM*PURPLE,  "left": TOP*RED,      "right": TOP*YELLOW},
    7: {"top": BOTTOM*PURPLE, "bottom": BOTTOM*RED,     "left": BOTTOM*GREEN, "right": BOTTOM*YELLOW},
    8: {"top": TOP*PURPLE,    "bottom": BOTTOM*GREEN,   "left": BOTTOM*RED,   "right": TOP*YELLOW},
    9: {"top": TOP*PURPLE,    "bottom": BOTTOM*PURPLE,  "left": TOP*YELLOW,   "right": BOTTOM*GREEN},
}

# example solution (from the image): (x_coord, y_coord): (tile_id, rotation))
solution = {(0,0): (5,0), (0,1): (2,0), (0,2):(9,0), 
            (1,0): (4,0), (1,1): (3,0), (1,2): (8,0),
            (2,0): (7,0), (2,1): (1,0), (2,2): (6,0)}

# precondition n = 0,1,2,3
# shifts items in a list by n positions
def shift_list(lst, n):
  assert(n >= 0 and n <= 3)
  return lst[-n:] + lst[:-n] 

# rotates the sides of a tile
# rotation = 0 (no rotation), 1 = 90 clockwise, 2 = 180 degrees clockwise, 3 = 270 degrees clockwise
def rotate_side(side_name, rotation):
  assert(rotation >= 0 and rotation <= 3)
  order_sides = ["top", "right", "bottom", "left"]
  ind_side_name = order_sides.index(side_name)
  rotate_sides = shift_list(order_sides,rotation)
  return rotate_sides[ind_side_name]

# tests okay
def get_side(tile_id, rotation, side_name): # get top of tile, rotation, get bottom of neighbor tile, rotation
  tile0 = tiles[tile_id]
  rotate_side_name = rotate_side(side_name, rotation)
  return tile0[rotate_side_name]

# matching constraints for each position on the board (x_coord, y_coord):
neighbors = {(0,0): ["right", "bottom"],
             (0,1): ["right", "bottom","left"],
             (0,2): ["bottom", "left"],
             (1,0): ["top", "right", "bottom"],
             (1,1): ["top", "right", "bottom", "left"],
             (1,2): ["top", "bottom", "left"],
             (2,0): ["top", "right"],
             (2,1): ["left", "top", "right"],
             (2,2): ["left", "top"]}

def check_solution(solution): # checks if full solution is valid
  for pos in solution: # for each position assigned in solution
    x,y = pos[0], pos[1]
    tile_id, rotation = solution[pos]
    check_new_tile(solution, pos, solution[pos])
  return True

# check if a new tile matches the other tiles placed 
def check_new_tile(solution, new_pos, new_val):
  x, y = new_pos[0], new_pos[1]
  tile_id, rotation = new_val[0], new_val[1]
  
  # identify the locations you need to check 
  for side in neighbors[new_pos]:
    
    side_tile, side_neighbor = None, None

    if side == "top" and (x-1,y) in solution:      # check pos x-1,y
      neighbor_id, neighbor_rotation = solution[(x-1,y)]
      # get top of tile, rotation, get bottom of neighbor tile, rotation
      side_tile     = get_side(tile_id, rotation, "top")
      side_neighbor = get_side(neighbor_id, neighbor_rotation, "bottom")
    
    elif side == "bottom" and (x+1,y) in solution: # check pos x+1,y
      neighbor_id, neighbor_rotation = solution[(x+1,y)]
      side_tile     = get_side(tile_id, rotation, "bottom")
      side_neighbor = get_side(neighbor_id, neighbor_rotation, "top")

    elif side == "left" and (x,y-1) in solution:   # check pos x, y-1
      neighbor_id, neighbor_rotation = solution[(x,y-1)]
      side_tile     = get_side(tile_id, rotation, "left")
      side_neighbor = get_side(neighbor_id, neighbor_rotation, "right")
      
    elif side == "right" and (x,y+1) in solution:  # check pos x, y+1
      neighbor_id, neighbor_rotation = solution[(x,y+1)]
      side_tile     = get_side(tile_id, rotation, "right")
      side_neighbor = get_side(neighbor_id, neighbor_rotation, "left")

      #print(neighbor_id, tiles[neighbor_id], rotation)
      #print(side, side_tile, side_neighbor)

    if side_tile != None and side_neighbor != None: 
      if side_tile + side_neighbor != 0:
        return False
  return True

def mrv(assignment, constraints):
  # select the unassigned variable with the minimum remaining values (MRV)
  pass

def backtrack_forward_checking(assignment, unassigned, domain_all):
  if len(assignment) == 9: # all positions assigned
    if check_solution(assignment):
      return assignment
    else:
      return False
  
  # select an unassigned position (x,y)
  next_pos = mrv(assignment, neighbors) # select the unassigned variable with the minimum remaining values (MRV)
  for value in domain_all[next_pos]:
    if

if __name__ == "__main__":
    assignment = {}
    unassigned = [key for key in solution] # all positions unassigned at the beginning
    domain_all = {key: [(tile_id, rotation) for tile_id in tiles for rotation in range(4)] for key in solution} # all possible tile and rotation combinations for each position
