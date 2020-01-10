def computeArea(A,B,C,D,E,F,G,H) :
    intersection_area = 0
    w = min([C, G]) - max([A, E])
    h = min([D, H]) - max([B, F])
    if w > 0 and h > 0 :
        intersection_area=w*h
    area=abs(A-C)*abs(B-D) + abs(E-G)*abs(F-H) - intersection_area
    return area