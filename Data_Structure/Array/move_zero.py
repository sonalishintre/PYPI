"""
Write an algorithm that takes an array and moves all of the zeros to the end of the list
    move_zeros([ 1, 0, 1, 2, 0, 1, 3])
    output => [ 1, 1, 2, 1, 3, 0, 0]
The time complexity is O(n).
"""


def move_zeros(array):
    result = []
    zeros = 0

    for i in array:
            if i == 0:
                zeros += 1
            else:
                result.append(i)
    
    result.extend([0] * zeros)
    return result


print(move_zeros([ 1, 0, 1, 2, 0, 1, 3,]))