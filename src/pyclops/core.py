from math import sqrt

def distance(p,q):
    dx = q[0] - p[0]
    dy = q[1] - p[1]
    return sqrt(dx*dx + dy*dy)

def closest_of_three(p,q,r):
    dpq  = distance(p,q)
    dpr  = distance(p,r)
    dqr  = distance(q,r)
    dmin = min(dpq,dpr,dqr)
    if   dmin == dpq : return (p,q),dpq
    elif dmin == dpr : return (p,r),dpr
    else             : return (q,r),dqr

def closest_pair(points):
    if len(points) == 3: return closest_of_three(*points)
    p = points[0]
    q = points[-1]
    d = distance(p,q)
    return (p,q), d
