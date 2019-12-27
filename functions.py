from constants import sz


def abs(p):
    if p < 0:
        return p * -1
    return p


def not_zero(p):
    if p == 0:
        return 0
    return 1


def get_xy_by_click(x, y):
    return x // sz, y // sz
