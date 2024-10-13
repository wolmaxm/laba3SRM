def up(array):
    return sorted(array)

def down(array):
    return sorted(array, reverse=True)

array1 = [1,2,3,4,5,6,7,8,9]

sort = up(array1)
sort1 = down(array1)

print(sort)
print(sort1)