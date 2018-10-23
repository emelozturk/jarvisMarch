def convex_hull(points):
    convex = []  # result array which gets append over loops

    if len(points) < 1:
        return None

    if len(points) < 2:
        for p in range(1, len(points)):
            convex.append(p)


# orientation function
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # start from the bottom point to find out points that form the convex
    bottom = bottom_finder(points)
    o = bottom
    convex.append(o)  # first element of convex convex_hull

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
            break

        convex.append(o)


def bottom_finder(points):
    if len(points) < 1:
        return None

    else:
        b = points[0]  # start point
        for p in range(1, len(points)):
            if b[1] < p[1]:
                b = p


