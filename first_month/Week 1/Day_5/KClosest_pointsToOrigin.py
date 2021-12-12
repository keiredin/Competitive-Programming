import math
from typing import List

class Solution:
    def calcDistance(self,point):
        return math.sqrt( math.pow(point[0],2) + math.pow(point[1],2) )
        
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda point:math.sqrt( math.pow(point[0],2) + math.pow(point[1],2)))
        return points[:k]


s = Solution()
print(s.kClosest([[68,97],[34,-84],[60,100],[2,31],[-27,-38],[-73,-74],[-55,-39],[62,91],[62,92],[-57,-67]],5))
print(s.kClosest([[1,3],[-2,2],[2,-2]],2))
print(s.kClosest([[0,1],[1,0],[2,0]],2))



# def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         n = len(points)
#         for i in range(n):
#             minValue = points[i]
#             for j in range(i+1,n):
#                 if (self.calcDistance(points[j]) < self.calcDistance(points[i])):
#                     points[i], points[j] = points[j], points[i]


#         return points[:k]


