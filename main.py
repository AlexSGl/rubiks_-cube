import copy

start_a = [["a1", "a2", "a3", "a4"],
           ["b1", "b2", "b3", "b4"],
           ["c1", "c2", "c3", "c4"],
           ["d1", "d2", "d3", "d4"],
           ["e1", "e2", "e3", "e4"],
           ["f1", "f2", "f3", "f4"]]

def rotate1(arr):
    arr_new = copy.deepcopy(arr)
    arr_new[0][1] = arr[3][1]
    arr_new[0][3] = arr[3][3]
    arr_new[1][1] = arr[0][1]
    arr_new[1][3] = arr[0][3]
    arr_new[2][1] = arr[1][1]
    arr_new[2][3] = arr[1][3]
    arr_new[3][1] = arr[2][1]
    arr_new[3][3] = arr[2][3]
    arr_new[4][0] = arr[4][2]
    arr_new[4][1] = arr[4][0]
    arr_new[4][2] = arr[4][3]
    arr_new[4][3] = arr[4][1]
    return arr_new

def rotate2(arr):
    arr_new = copy.deepcopy(arr)
    arr_new[1][0] = arr[4][1]
    arr_new[1][1] = arr[4][3]
    arr_new[2][0] = arr[2][2]
    arr_new[2][1] = arr[2][0]
    arr_new[2][2] = arr[2][3]
    arr_new[2][3] = arr[2][1]
    arr_new[3][2] = arr[5][0]
    arr_new[3][3] = arr[5][2]
    arr_new[4][1] = arr[3][3]
    arr_new[4][3] = arr[3][2]
    arr_new[5][0] = arr[1][1]
    arr_new[5][2] = arr[1][0]
    return arr_new

def rotate3(arr):
    arr_new = copy.deepcopy(arr)
    arr_new[0][2] = arr[5][2]
    arr_new[0][3] = arr[5][3]
    arr_new[2][0] = arr[4][3]
    arr_new[2][1] = arr[4][2]
    arr_new[3][0] = arr[3][1]
    arr_new[3][1] = arr[3][3]
    arr_new[3][2] = arr[3][0]
    arr_new[3][3] = arr[3][2]
    arr_new[4][2] = arr[0][2]
    arr_new[4][3] = arr[0][3]
    arr_new[5][2] = arr[2][1]
    arr_new[5][3] = arr[2][0]
    return arr_new


kr1 = rotate3(start_a)
kr2 = rotate3(kr1)
kr3 = rotate3(kr2)
kr4 = rotate3(kr3)


print(start_a)
print(kr1)
print(kr2)
print(kr3)
print(kr4)
print(kr4 == start_a)
