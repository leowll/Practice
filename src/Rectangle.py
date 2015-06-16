# -*- coding: utf-8 -*-
__author__ = 'leo'
"""
    package.module
    ~~~~~~~~~~~~~~

    A brief description goes here.

    :copyright: (c) YEAR by AUTHOR.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""


def calc(xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2):
    '''
    Calculate the area of two rectangles
    :param xa1: left top xa
    :param ya1: left top ya
    :param xa2: right bottom xa
    :param ya2: right bottom ya
    :param xb1: left top xb
    :param yb1: left top yb
    :param xb2: right bottom xb
    :param yb2: right bottom yb
    :return: the area
    '''
    overlapped_area = 0
    if is_overlapped(xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2):
        o_xa = max(xa1, xb1)
        o_ya = min(ya1, yb1)

        o_xb = min(xa2, xb2)
        o_yb = max(ya2, yb2)
        overlapped_area = abs(o_xa - o_xb) * abs(o_ya - o_yb)
    return abs(xa1 - xa2) * abs(ya1 - ya2) - overlapped_area * 2


def is_overlapped(xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2):
    '''
    Decide whether 2 rectangles is overlapped
    :param xa1:
    :param ya1:
    :param xa2:
    :param ya2:
    :param xb1:
    :param yb1:
    :param xb2:
    :param yb2:
    :return: true for overlapped
    '''
    x_dist1 = abs(xa1 - xa2)
    x_dist2 = abs(xb1 - xb2)
    y_dist1 = abs(ya1 - ya2)
    y_dist2 = abs(yb1 - yb2)

    x_mid1 = xa1 + x_dist1 / 2
    y_mid1 = ya2 + y_dist1 / 2

    x_mid2 = xb1 + x_dist2 / 2
    y_Mid2 = yb2 + y_dist2 / 2

    x_mid_dist = abs(x_mid1 - x_mid2)
    y_mid_dist = abs(y_mid1 - y_Mid2)

    if x_mid_dist < (x_dist1 + x_dist2) and y_mid_dist < (y_dist1 + y_dist2):
        return True
    return False


if __name__ == '__main__':
    print calc(0, 4, 4, 0, 0, 2, 2, 0)
