col_name = ['Plein Air', 'Pratique', 'Numérique', 'Scientifique', 'Persuasif', 'Artisitique', 'Littéraire', 'Musical',
            'Social', 'Urbain']

ref = [0, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 100, 100]

M_raw = [[48, 44, 52, 48, 48, 48, 48, 36, 56, 72],
         [47, 44, 48, 47, 42, 45, 48, 36, 54, 66],
         [41, 40, 36, 41, 31, 41, 40, 32, 40, 52],
         [38, 38, 34, 39, 29, 37, 37, 30, 37, 47],
         [34, 35, 30, 36, 26, 32, 31, 25, 32, 43],
         [32, 34, 29, 33, 25, 30, 29, 24, 30, 41],
         [31, 33, 28, 32, 24, 29, 27, 22, 29, 39],
         [27, 30, 25, 29, 22, 27, 25, 19, 27, 36],
         [25, 28, 23, 27, 20, 25, 22, 17, 25, 34],
         [22, 25, 21, 25, 18, 22, 20, 15, 23, 31],
         [20, 22, 20, 22, 17, 20, 18, 12, 21, 27],
         [19, 21, 19, 21, 15, 19, 16, 11, 19, 25],
         [17, 19, 18, 20, 13, 18, 14, 10, 18, 23],
         [13, 14, 15, 18, 10, 15, 11, 7, 15, 18],
         [10, 10, 12, 15, 9, 13, 9, 5, 12, 14],
         [1, 2, 3, 6, 0, 2, 3, 0, 2, 4]]

F_raw = [[48, 44, 52, 48, 52, 48, 48, 36, 56, 72],
         [47, 39, 43, 46, 43, 48, 47, 36, 56, 67],
         [37, 27, 33, 40, 36, 44, 40, 33, 47, 57],
         [34, 24, 31, 36, 34, 41, 37, 31, 44, 52],
         [30, 20, 28, 33, 31, 36, 33, 27, 40, 48],
         [29, 19, 27, 32, 29, 35, 31, 26, 39, 46],
         [27, 18, 26, 31, 28, 34, 29, 25, 37, 44],
         [25, 16, 24, 28, 26, 31, 27, 23, 34, 41],
         [23, 14, 22, 25, 23, 29, 24, 21, 31, 37],
         [21, 13, 20, 23, 20, 27, 22, 19, 29, 33],
         [19, 11, 18, 20, 17, 24, 20, 16, 26, 27],
         [17, 10, 17, 19, 16, 23, 18, 15, 24, 24],
         [16, 9, 16, 18, 14, 22, 17, 14, 23, 22],
         [12, 7, 13, 15, 10, 19, 14, 11, 19, 16],
         [10, 5, 10, 12, 8, 17, 11, 8, 16, 12],
         [1, 0, 1, 5, 2, 9, 5, 1, 4, 3]]

F = [[F_raw[15 - i][j] for i in range(16)] for j in range(10)]
M = [[M_raw[15 - i][j] for i in range(16)] for j in range(10)]


def get_ref_from_abaque(i: int, lookup: int, gender: int):
    rounder = F[i] if gender == 1 else M[i]
    if lookup in rounder:
        return ref[rounder.index(lookup)]

    closest = min(rounder, key=lambda x: abs(x - lookup))
    closest_id = rounder.index(closest)
    rounder_no_closest = rounder[:]
    rounder_no_closest.pop(closest_id)
    next_closest = min(rounder_no_closest, key=lambda x: abs(x - lookup))
    next_closest_id = rounder.index(next_closest)

    ref1 = ref[closest_id]
    ref2 = ref[next_closest_id]
    round_min = min(closest, next_closest)
    delta = lookup - round_min
    ratio = delta / (abs(closest - next_closest))
    value = ratio * (abs(ref1 - ref2)) + min(ref1, ref2)
    return value
