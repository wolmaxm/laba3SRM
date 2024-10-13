array1 = [1,2,3,4,5,6,7,8,9]
array2 = [10,11,12,13,14,15,16]

def arrays(arr1,arr2):
    return sorted(arr1 + arr2)

merged = arrays(array1,array2)
print(merged)

def chto(array1,array2):
    array1.extend(array2)
    array1.sort()
chto(array1 , array2)
print(array1)