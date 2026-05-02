from functools import lru_cache
@lru_cache(None)
def count_dyck_words(x_rem, y_rem, z_rem, w_rem, x_used, y_used, z_used, w_used, last_char, s_needed):
    if x_rem == y_rem == z_rem == w_rem == 0:
        return 1 if s_needed == 0 else 0
    if not (x_used >= y_used >= z_used >= w_used):
        return 0
    if s_needed < 0:
        return 0
    total = 0
    if x_rem > 0:
        total += count_dyck_words(x_rem - 1, y_rem, z_rem, w_rem,
                                  x_used + 1, y_used, z_used, w_used,
                                  0, s_needed)
    if y_rem > 0 and x_used >= y_used + 1:
        total += count_dyck_words(x_rem, y_rem - 1, z_rem, w_rem,
                                  x_used, y_used + 1, z_used, w_used,
                                  1, s_needed)
    if z_rem > 0 and y_used >= z_used + 1:
        used = 1 if (last_char == 0 or last_char==1)  else 0  
        total += count_dyck_words(x_rem, y_rem, z_rem - 1, w_rem,
                                  x_used, y_used, z_used + 1, w_used,
                                  2, s_needed - used)
    if w_rem > 0 and z_used >= w_used + 1:
        used = 1 if (last_char == 0 or last_char==1) else 0  
        total += count_dyck_words(x_rem, y_rem, z_rem, w_rem - 1,
                                  x_used, y_used, z_used, w_used + 1,
                                  3, s_needed - used)
    return total
for n in range(0, 10):
    s= ""
    for p in range(1, 2*n+1):
        result = count_paths_with_s_peaks(n, n, n, n, 0, 0, 0, -1, p)
        s = s + str(result)+","
    print(s)
