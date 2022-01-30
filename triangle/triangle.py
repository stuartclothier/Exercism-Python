from typing import Callable


def is_triangle(sides: list[int]) -> Callable[..., bool]:
    return lambda s: all(s) and 2 * max(s) < sum(s) and sides(s)


@is_triangle
def equilateral(sides: list[int]) -> bool:
    return len(set(sides)) == 1


@is_triangle
def isosceles(sides: list[int]) -> bool:
    return len(set(sides)) <= 2


@is_triangle
def scalene(sides: list[int]) -> bool:
    return len(set(sides)) == 3
