import random

def RandomArray(N):
    array = []
    while len(array) < N:
        random_num = random.randint(1, N)
        if array.count(random_num) == 0:
            array.append(random_num)
    print(array)
    array.sort()
    return array
N = 30
random4ik = RandomArray(N)
print(random4ik)