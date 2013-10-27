from math import sqrt
from sys import maxint as MAXINT

#
# Euclidean distance function.
#
def distance(p,q):
    dx = q[0] - p[0]
    dy = q[1] - p[1]
    return sqrt(dx*dx + dy*dy)

#
# Computes a distance for all pairs of points and picks the shortest.
#
# Returns: (p,q),d
#
# Where p and q are points with form (x,y) and d is the distance
# between p and q.
#
def brute_force_closest_pair(points):
    assert(len(points) > 1)
    results = [((points[i],points[j]), distance(points[i],points[j]))
               for i in xrange(len(points))
               for j in xrange(i+1,len(points))]
    results.sort(key=lambda (_,distance): distance)
    return results[0]

#
# One-pass filtering. Splits sequence in O(n).
#
def predicate_split(predicate, sequence):
    truthy,falsey = [],[]
    for item in sequence:
        if predicate(item):
            truthy.append(item)
        else:
            falsey.append(item)
    return truthy,falsey

#
# Wrapper function. Pre-sorts points and calls _closest_pair.
#
def closest_pair(points):
    x_points = sorted(points, key=lambda point: point[0])
    y_points = sorted(points, key=lambda point: point[1])
    return _closest_pair(x_points, y_points)

#
# Recursive divide-and-conquer algorithm. Arguments:
#
# x_points : points sorted by x-coordinate
# y_points : points sorted by y-coordinate
#
# Returns: (p,q),d
#
# Where p,q are points of the form (x,y)
# and d is the distance between p and q.
#
def _closest_pair(x_points, y_points):
    n_total = len(x_points)
    if n_total <= 3: return brute_force_closest_pair(x_points)

    # Choose an x-coordinate that approximately splits group in half.
    line = x_points[n_total/2][0]
    is_left = lambda point: point[0] < line

    # x- and y-sorted subproblems, i.e. to the left and right of line.
    lx_points,rx_points = predicate_split(is_left, x_points)
    ly_points,ry_points = predicate_split(is_left, y_points)
    (pl,ql),dl = _closest_pair(lx_points, ly_points)
    (pr,qr),dr = _closest_pair(rx_points, ry_points)

    # Closest pair that crosses the line.
    (pm,qm),dm = _crossline_pair(y_points, line, min(dl,dr))

    dmin = min(dl,dm,dr)
    if dl == dmin: return (pl,ql),dl
    if dm == dmin: return (pm,qm),dm
    if dr == dmin: return (pr,qr),dr

#
# Subroutine checks for pairs across "line", which may have distance
# less than "dist". Arguments:
#
# y_points : y-sorted points
# line : x-coordinate of dividing line
# dist : minimum distance between points
#
# Returns: (p,q),d
#
# Where p,q are points (x,y) and d is distance
# between p and q. Closest pair within "dist" of "line".
#
def _crossline_pair(y_points, line, dist):
    ym_points = filter(lambda point: abs(point[0]-line) <= dist, y_points)
    n_mid = len(ym_points)

    # For each point check the 7 closest points along line +/- dmin.
    pm,qm,dm = None,None,MAXINT
    for i in xrange(n_mid - 1):
        for j in xrange(i+1, min(n_mid, i+7)):
            dij = distance(ym_points[i], ym_points[j])
            if dij < dm:
                pm = ym_points[i]
                qm = ym_points[j]
                dm = dij

    return (pm,qm),dm
