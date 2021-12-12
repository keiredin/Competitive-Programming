import math


def calcDistance(point):
    return math.sqrt( math.pow(point[0],2) + math.pow(point[1],2) )

def KClosest(points,k):
    n = len(points)
    for i in range(n):
        minValue = points[i]
        for j in range(i+1,n):
            if (calcDistance(points[j]) < calcDistance(points[i])):
                points[i], points[j] = points[j], points[i]
                

    return points[:k]

print(KClosest([[1,3],[-2,2],[2,-2]],2))




