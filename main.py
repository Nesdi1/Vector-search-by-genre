import numpy as np
u1 = np.array(list(map(int, input().split())))
u2 = np.array(list(map(int, input().split())))
u3 = np.array(list(map(int, input().split())))
dist_1_2 = np.linalg.norm(u1-u2)
dist_1_3 = np.linalg.norm(u1-u3)
if dist_1_2 < dist_1_3:
    print("второй человек ближе к первому по жанрам")
else:
    print("третий человек ближе к первому по жанрам")
