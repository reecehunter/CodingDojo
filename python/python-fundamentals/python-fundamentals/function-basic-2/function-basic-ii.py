def countdown(num):
    result = []
    for i in range(num, -1, -1):
        result.append(i)
    return result
# print(countdown(5))

def print_and_return(list):
    print(list[0])
    return list[1]
# print_and_return([10, 20])

def first_plus_length(list):
    sum = list[0] + len(list)
    return sum
# print(first_plus_length([10, 20, 30, 40, 50]))

def values_greater_than_second(list):
    result = []
    if(len(list) < 2):
        return False
    for i in list:
        if(i > 2):
            result.append(i)
    return result
# print(values_greater_than_second([5,2,3,2,1,4]))

def this_length_that_value(size, value):
    result = []
    for i in range(size):
        result.append(value)
    return result
# print(this_length_that_value(4, 7))