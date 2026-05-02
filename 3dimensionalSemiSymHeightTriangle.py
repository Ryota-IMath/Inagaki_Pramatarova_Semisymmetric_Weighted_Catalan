from functools import lru_cache
@lru_cache(None)
def ht(t):
    return 2 * t[0] - 2 * t[2]


def altern(t, bd):
    count = 0
    if t == (0, 0, 0):
        return 1
    if t[0] > 0 and t[0] - 1 >= t[1]:
        count += altern((t[0] - 1, t[1], t[2]), bd)
    if t[1] > 0 and t[1] - 1 >= t[2] and ht((t[0], t[1] - 1, t[2])) <= bd:
        count += altern((t[0], t[1] - 1, t[2]), bd)
    if t[2] > 0 and ht((t[0], t[1], t[2] - 1)) <= bd:
        count += altern((t[0], t[1], t[2] - 1), bd)
    return count

for n in range(1, 9):
    for h in range(1, n+1):
        if h == 1:
            print(altern((n, n, n), 2*h))
        if h > 1:
            print(altern((n, n, n), 2*h)-altern((n, n, n), 2*(h-1)))
