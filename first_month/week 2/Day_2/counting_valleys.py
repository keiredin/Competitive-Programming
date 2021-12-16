from typing import Counter


# def countingValleys(steps):
#     # Write your code here
#     count = Counter(steps)
#     print(count)
#     if (count[steps[steps.index('D')]] == count[steps[steps.index('U')]]):
#         return 1
#     else:
#         return 0


def countingValleys(path, steps):
    # Write your code here
    seaLevel = 0
    valley = 0
    for i in range(0,steps):
        if path[i] == "U":
            seaLevel += 1
        elif path[i] == "D":
            seaLevel -= 1

        if seaLevel == 0 and path[i] == "U":
            valley += 1
        
        
    return valley

   

print(countingValleys('DDDUDUUUDDUUUD',14))


