import math


def reflect(x1, y1, x2, y2, vx1, vy1, vx2, vy2):
    coords1 = [x1, y1]
    coords2 = [x2, y2]
    velocity1 = [vx1, vy1]
    velocity2 = [vx2, vy2]
    base1 = [[1, 0],
             [1, 0]]
    mod_base1 = [1, 1]
    base2 = [[x1 - x2, y1 - y2],
             [y1 - y2, x2 - x1]]
    mod_base2 = [math.sqrt(base2[0][0] ** 2 + base2[0][1] ** 2), math.sqrt(base2[1][0] ** 2 + base2[1][1] ** 2)]
    def translation(value, base, mod_base):
        value_ = [(value[0] * base[0][0] + value[1] * base[0][1]) / mod_base[0],
                  (value[0] * base[1][0] + value[1] * base[1][1]) / mod_base[1]]
        return value_
    coords1_ = translation(coords1, base2, mod_base2)
    coords2_ = translation(coords2, base2, mod_base2)
    velocity1_ = translation(velocity1, base2, mod_base2)
    velocity2_ = translation(velocity2, base2, mod_base2)
    velocity1_[1] = -velocity1_[1]
    velocity2_[1] = -velocity2_[1]
    velocity1 = translation(velocity1_, base1, mod_base1)
    velocity2 = translation(velocity2_, base1, mod_base1)
    return(velocity1[0], velocity1[1], velocity2[0], velocity2[1])