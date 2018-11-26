"""
The following algorithms are great to practice whiteboarding!

These problems require:

- Visualizations and diagrams
- Heavy collaboration
- Moderate to difficult problem solving skills

"""

def encircle(commands):
    """
    You control a little bot that moves around along the lines of a grid. The commands to move the
    bot are simple:
    - L will make the robot turn LEFT
    - G will make the robot GO 1 point forward
    - R will make the robot turn RIGHT

    For example, if you wanted the robot to encirlce the starting point, the command string may
    look like this:

        'GLGLG'

    ...which would command the robot to:
    move 1 point forward, turn left, forward, turn left, forward turn right.

    Given an array of commands, determine which will encircle the starting point. Return an
    array of booleans that say true if the command will encircle and false if it will not.
    """
    solutions = []

    if len(commands) == 1 and commands[0] == 'G':
        print("One command: ", commands[0])
        return ['NO']

    for line in commands:
        size = len(line)
        print("Command: ", line)
        if size == 1 and line == 'G':
            solutions.append(False)
        elif 'R' in line and 'L' in line:
            solutions.append(False)
        elif {'G'} == set(line):
            solutions.append(False)
        else:
            solutions.append(True)

    return solutions


def how_many_cats_in_hats():
    """Cats in Hats

    https://gist.github.com/Protosac/439e77dd9ee3880dc5cc870a8533b38e

    You have 100 cats. You have arranged all your cats in a line. Initially,
    none of your cats have any hats. You take 100 rounds walking around the cats,
    always starting with the first cat. Every time you stop at a cat, you put a
    hat on it if it doesn't have one, and you take its hat off if it has one on.
    The first round, you stop at every cat. The second round, you only stop at
    every 2nd cat (#2, #4, #6, #8, etc.). The third round, you only stop at every
    3rd cat (#3, #6, #9, #12, etc.). You continue this process until the 100th
    round (i.e. you only visit the 100th cat). Write a program that prints which
    cats have hats at the end.
    """
    # First use a dictionary to track the cats
    # Cats have no hats at the beginning
    cats_with_hats = {i: False for i in range(1, 101)}

    # Walk around for 100 rounds
    for n in range(100):
        # For each round, place or remove a hat on every cat
        for cat in cats_with_hats.keys():
            # Place/remove a hat on every nth cat
            if cat % n == 0:
                # Alternate between placing or removing a hat.
                # If a cat has a hat, remove it. If not, place a hat on its head
                cats_with_hats[cat] = !cats_with_hats[cat]

    # Count the final number of cats with hats!
    return len(list(filter(lambda cat: cats_with_hats[cat])))



def escape(carpark):
    """Escape the Parking Garage

    Return the shortest path to exit the parking garage.

    - 0: parking space
    - 1: stair well
    - 2: your parking space
    - The exit is always the last element of the ground floor

    Directions should be formatted like so:

    - A string with the capitalized direction followed by the number of spaces
    - Directions are D, R and L for down, right, or left

    Example:
    [[1, 0, 0, 2, 0],  # Level 1
     [0, 0, 0, 0, 0]]  # Ground, element floor[4] is the exit
    
    Go left 3 spaces, down 1 floor and right 4 spaces:
    => ['L3', 'D1', 'R4']

    """
    if len(carpark) == 1 and carpark[len(carpark) -1] is not 0: return []
    if len(carpark) == 1:
        car = carpark.index(2)
        exit = carpark[len(carpark) -1]
        return ["R{}".format(str(exit - car))]

    for i, level in enumerate(carpark):
        if 2 in level:
            break
        else:
            idx = i +1
            carpark = carpark[idx:]
            print("Removing ", level)

    directions = []
    down = 0
    current = carpark[0].index(2)

    for level in carpark:
        size = len(level)
        if 2 in level:
            start = level.index(2)
            stair = level.index(1)
            if stair < start:
                directions.append("L{}".format(str(start - stair)))
            else:
                directions.append("R{}".format(str(stair - start)))
            down += 1
            current = stair
            print(directions)
        elif 1 in level:
            stair = level.index(1)
            if current < stair:
                directions.append("D1")
                directions.append("R{}".format(str(stair - current)))
            elif stair < current:
                directions.append("D1")
                directions.append("L{}".format(str(current - stair)))
            elif stair == current:
                down += 1

            current = stair
            print(directions)
        else:
            exit = size - 1
            directions.append("D{}".format(down))
            if current < exit:
                directions.append("R{}".format(str(exit - current)))
            print(directions)


    print(directions)
    return directions

carpark = [[0, 0, 0, 0, 1],
           [0, 2, 0, 0, 1],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]]
