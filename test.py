import math
def distance(other_point, current_point):
    vector = (current_point[0] - other_point[0], current_point[1] - other_point[1])
    dis = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    return dis

print(distance((44, 50), (43, 59)))