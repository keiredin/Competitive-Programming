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
                

    return points

print(KClosest([[1,3],[-2,2],[2,-2]],2))



# def KClosest(points,k):
#     distances = []
#     closestPoints = []
#     sortedDistances = []
#     for i in points:
#         distance = math.sqrt( math.pow(i[0],2) + math.pow(i[1], 2))
#         distances.append(distance)
#         sortedDistances.append(distance)
#     sortedDistances.sort()
        
                
                
#     for i in range(k):
#         closestPoints.append(points[distances.index(sortedDistances[i])])
        
#     return sortedDistances

# print(KClosest([[1,2],[2,2],[2,1],[3,1]],2))

# def calculate_distance(point_1, point_2):
#     d = math.sqrt(((point_1[0] - point_2[0]) ** 2) +
#                   ((point_1[1] - point_2[1]) ** 2)
#                   )
#     return d


# def k_closest(points, k):
#     origin = [0, 0]
#     for i in range(k):

#         min_distance = calculate_distance(points[i], origin)
#         min_distance_index = i

#         for j in range(i + 1, len(points)):
#             distance = calculate_distance(points[j], origin)

#             if distance < min_distance:

#                 min_distance = distance
#                 min_distance_index = j
#             points[i], points[min_distance_index] = points[min_distance_index], points[i]
#     return points[:k]


# points = [[0,1], [1,0], [-2, 4]]
# k = 2
# print(k_closest(points, k))
