#!/usr/bin/env R
def distance(x1,y1,x2,y2):
    """calculate distance between
    coordinates (x1,y1) and (x2,y2)"""
    import math
    d = (x2-x1)**2 + (y2-y1)**2
    d = math.sqrt(d)
    return d
                        
