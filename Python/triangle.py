# Determine if a triangle is equilateral, isosceles, or scalene.

# Approach 1:
def equilateral(sides):
    if sides[0] == sides[1] == sides[2] and sides[0] > 0:
        return True
    else:
        return False


def isosceles(sides):
    if sides[0] == sides[1] and sides[0] + sides[1] >= sides[2]:
        return True
    elif sides[1] == sides[2] and sides[1] + sides[2] >= sides[0]:
        return True
    elif sides[0] == sides[2] and sides[0] + sides[2] >= sides[1]:
        return True
    else:
        return False


def scalene(sides):
    if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
        sides.sort() # Sorts the list from smallest to largest
        if sides[0] + sides[1] >= sides[2]:
            return True
        else:
            return False
    else:
        return False
    
# Approach 2: (Attempt to recreate bidouille's solution)

def equilateral(sides):
    a, b, c = sorted(sides) # Sorts the list from smallest to largest or can use sides.sort()
    return a > 0 and a == c

def isosceles(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b >= c and b in (a, c)

def scalene(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b >= c and b not in (a, c)