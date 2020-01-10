def isRectangleOverlap(rec1,rec2) :
    x11 = rec1[0]
    x12 = rec1[2]
    y11 = rec1[1]
    y12 = rec1[3]
    x21 = rec2[0]
    x22 = rec2[2]
    y21 = rec2[1]
    y22 = rec2[3]
    intersection_area=0
    w=min([x22,x12])-max([x11,x21])
    h = min([y22, y12]) - max([y11, y21])
    if w>0 and h>0 :
        return True
    else :
        return False