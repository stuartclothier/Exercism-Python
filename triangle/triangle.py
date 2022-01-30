def is_triangle(sides: list[int]) -> bool:
    return all(ele > 0 for ele in sides) and max(sides) <= sum(sides) / 2


def equilateral(sides: list[int]) -> bool:
    return len(set(sides)) == 1 and is_triangle(sides)


def isosceles(sides: list[int]) -> bool:
    return len(set(sides)) <= 2 and is_triangle(sides)


def scalene(sides: list[int]) -> bool:
    return len(set(sides)) == 3 and is_triangle(sides)
