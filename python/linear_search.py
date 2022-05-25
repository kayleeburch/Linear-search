array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)

#release 0
# def linear_search(value_to_find, array_to_search_through):
#     count = -1
#     for i in array_to_search_through:
#         count += 1;
#         if i == value_to_find:
#             return count
    
#     return None

#release 1
def global_linear_search(value_to_find, array_to_search_through):
    occur = []
    count = -1
    for i in array_to_search_through:
        count += 1;
        if i == value_to_find:
            occur.append(count)

    if(len(occur) == 0):
        return None
    
    return occur

