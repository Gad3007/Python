pi = 3.14


def find_farthest_orbit(list_1):
    s = 0
    a1 = 0 
    b1 = 0
    for a, b in list_1:
        if a != b and a * b * pi > s:
            a1 = a
            b1 = b
            s = a1 * b1 * pi
    return a1,b1


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(f'Наибольшая площадь = { find_farthest_orbit(orbits) }')

# from math import pi
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# ellipse = [t for t in orbits if t[0] != t[1]]
# res = max(ellipse, key=lambda t: pi * t[0] * t[1])

# print(res)
