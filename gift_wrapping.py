#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This module implements gift-wrapping convex hull algorithm.

The module helps to find smallest convex polygon that contains
all the given points.

Examples:

     result = gift_wrapping.convex_hull((0, 0),
                                           (0, 4), (4, 4), (1, 4), (0, 2), (3, 6),
                                           (-3, 6), (-4, 4), (1, 5), (-1, 3))

        self.assertEqual(result, (0, 0), (3, 6),
                         (4, 4), (-3, 6), (-4, 4))


     run unit tests of this module by running :
     $ python -m unittest test.py
"""


def convex_hull(points):
    # result array which gets append over loops
    convex = []

    # return None if there is no point.
    if len(points) < 1:
        return None

    # if there is only one point.
    if len(points) < 2:
        for p in range(1, len(points)):
            convex.append(p)


# Orientation function for finding notation of the points.
# The formula below is come from slope of the points.
def cross(o, a, b):
    return (a[0]-o[0]) * (b[1]-o[1]) - (a[1]-o[1]) * (b[0]-o[0])

    # start from the bottom point to find out points that form the convex
    bottom = bottom_finder(points)
    o = bottom
    convex.append(o)    # first element of convex

    while True:

        a = points[0]

        for b in range(1, len(points)):

            if o == b:
                continue

            if o == a:
                a = b
                continue

        c = cross(o, a, b)
        if c < 0:
            a = b

        o = a
        if o == bottom:
            # our convex ends at start point (bottom)
            break

        convex.append(o)


def bottom_finder(points):
    if len(points) < 1:
        return None

    else:
        b = points[0]
        for p in range(1, len(points)):
            if b[1] < p[1]:
                b = p


