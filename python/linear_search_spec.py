from linear_search import global_linear_search

print(global_linear_search(3, [1,2,3,3,6,7,3]) == [2,3,6])
print(global_linear_search(4, [1,2,3]) == None)
print(global_linear_search(13, [13,2,3]) == [0])
print(global_linear_search(0, [0,1,2,3,0]) == [0,4])
print(global_linear_search("a", ["b", "a", "n", "a", "n", "a", "s"]) == [1,3,5])
print(global_linear_search(True, [True, False, True, False]) == [0,2])
print(global_linear_search("?", ["?", ">", ">", "?", "*", 2, True]) == [0,3])
