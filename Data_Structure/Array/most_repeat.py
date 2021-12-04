"""
This algorithm receives an array and returns most_frequent_value
For example: most_repeat([1, 1, 1, 2, 2, 3, 4,5,6]) will 
return [1, 2]
Time Complexity: O(n)
"""
def most_freq(array):
    dict = {}
    
    result = []
    repeat_val = 0

    for i in array:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    repeat_val = max(dict.values())
        
    for i in dict.keys():
        if dict[i] == repeat_val:
            result.append(i)
        else:
            continue
    
    return result

arr = [1,2,3,4,5,4,4,4]
print(most_freq(arr))