def ht(t):
    return 3 * t[0] + t[1] - t[2] - 3*t[3]

def altern(t, bd):
    count = 0
    if t == (0, 0, 0, 0):
        return 1
    if t[0] > 0 and t[0] - 1 >= t[1]:
        count += altern((t[0] - 1, t[1], t[2], t[3]), bd)
    if t[1] > 0 and t[1] - 1 >= t[2] and ht((t[0], t[1] - 1, t[2], t[3])) <= bd:
        count += altern((t[0], t[1] - 1, t[2], t[3]), bd)
    if t[2] > 0 and t[2] - 1 >= t[3] and ht((t[0], t[1], t[2] - 1, t[3])) <= bd:
        count += altern((t[0], t[1], t[2] - 1, t[3]), bd)
    if t[3] > 0 and ht((t[0], t[1], t[2], t[3] - 1)) <= bd:
        count += altern((t[0], t[1], t[2], t[3] -1), bd)
    return count
for n in range(1, 6):
    for h in range(4, 4*n+1):
        if h == 4:
            print(altern((n, n, n, n), h))
        if h > 4:
            print(altern((n, n, n, n), h)-altern((n, n, n, n), h-1))
