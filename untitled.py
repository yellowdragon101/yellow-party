import random
import math

# damour's comments are uppercase mine aren't 

class Location:
    
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.neighbors = []
        self.players = []

    def get_position(self):
        # Right now this function always returns the position tuple (0, 0)
        # Modify it to return (x, y) of the location.
        return (self.x, self.y)

    def __str__(self):
        return self.name + " (" + str(self.x) + ", " + str(self.y) + ")"

    def get_neighbors(self):
        locnames= []
        for loc in self.neighbors:
            locnames.append(loc.name) 
        return locnames

class Player:
    def __init__(self, name):
        self.name = name
        self.location = None


def midpoint(pos1, pos2):
    # The input parameters pos1 and pos2 should be tuples of (x,y) positions:
    # This function should return the midpoint between them.

    # Finish the code...  
    x1, y1 = pos1
    x2, y2 = pos2
    xm = (x1 + x2)/2 
    ym = (y1 + y2)/2

    return (xm, ym)

# i cant do trig
def get_dir(origin, dest):
    origin_x, origin_y = origin
    dest_x, dest_y = dest
    delta_x = abs(origin_x - dest_x)
    delta_y = abs(origin_y - dest_y)

    # Handle case where we will have a divsion by zero error
    if delta_x == 0:
        if dest_y > origin_y:
            return 0.0
        else:
            return 180

    if delta_y == 0:
        if dest_x > origin_x:
            return 90
        else:
            return 270

    if dest_x >= origin_x and dest_y >= origin_y:
        return 90 - math.degrees(math.atan(delta_y / delta_x))
    if dest_x <= origin_x and dest_y >= origin_y:
        return 270 + math.degrees(math.atan(delta_y / delta_x))
    if dest_x >= origin_x and dest_y <= origin_y:
        return 270 - math.degrees(math.atan(delta_y / delta_x))
    if dest_x <= origin_x and dest_y <= origin_y:
        return 90 + math.degrees(math.atan(delta_y / delta_x))

def get_compass_dir(origin, dest):
        # 315 - 45 = N  0 - 45, 315 - 360 
        # 45 - 135 = E
        # 135 - 225 = S
        # 225 - 315 = W
    dir = get_dir(origin, dest)
    if (dir >= 0 and dir <= 45) or (dir >= 315 and dir <= 360):
        return "N"
    if dir >= 45 and dir <= 135:
        return "E"
    if dir >= 135 and dir <= 225:
        return "S"
    if dir >= 225 and dir <= 315:
        return "W"

if __name__ == '__untitled__':
    farm = Location(276,659, "Farm")
    castle = Location(260, 579, "Castle")
    bosdirnao = Location(493, 610, "Bosdirnao") # shoutouts to alpha's keyboard smash with added vowels 
    left_mountain = Location(219, 363, "Left Mountain Base") # what do i call these i have no idea
    right_mountain = Location(353, 198, "Right Mountain Base")
    summit = Location(228, 52, "Mountain Summit")
    swamp = Location(497, 204, "Swamp")
    forest = Location(686, 208, "Forest")
    deep_forest = Location(701, 82, "Deep Forest")
    treesed = Location(873, 226, "Treesed") # shoutouts to boggy
    desert = Location(964, 408, "Desert") # i like cacti
    mirage = Location(693, 416, "Mirage") # shoutouts to dragon view 
    waterfall = Location(584, 518, "Waterfall")
    arena = Location(474, 410, "Arena") # t21 btw

    castle.neighbors.append(farm)
    farm.neighbors.append(castle)
    farm.neighbors.append(bosdirnao)
    bosdirnao.neighbors.append(farm)
    bosdirnao.neighbors.append(waterfall)
    bosdirnao.neighbors.append(arena)
    summit.neighbors.append(right_mountain)
    summit.neighbors.append(left_mountain)
    right_mountain.neighbors.append(summit)
    right_mountain.neighbors.append(swamp)
    left_mountain.neighbors.append(summit)
    left_mountain.neighbors.append(arena)
    swamp.neighbors.append(right_mountain)
    swamp.neighbors.append(forest)
    forest.neighbors.append(swamp)
    forest.neighbors.append(deep_forest)
    forest.neighbors.append(treesed)
    deep_forest.neighbors.append(forest)
    deep_forest.neighbors.append(treesed)
    treesed.neighbors.append(forest)
    treesed.neighbors.append(deep_forest)
    treesed.neighbors.append(desert)
    desert.neighbors.append(treesed)
    desert.neighbors.append(mirage)
    mirage.neighbors.append(desert)
    mirage.neighbors.append(waterfall)
    waterfall.neighbors.append(mirage)
    waterfall.neighbors.append(bosdirnao)
    arena.neighbors.append(left_mountain)
    arena.neighbors.append(bosdirnao)

    player = Player("Yellow")
    player.location = random.choice([summit, desert, farm, deep_forest])

    while True:
        print("Your location:" + str(player.location))
        print(player.location.get_neighbors())
        player.location = player.location.neighbors[int(input(">"))]    