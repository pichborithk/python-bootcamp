# This slice works with both list and tuple

my_list = [0, 1, 2, 3, 4, 5]

print(my_list[1:4])
# 1, 2, 3

print(my_list[3:])
# 3, 4, 5

print(my_list[1:4:2])
# 1, 3

print(my_list[::2])  # print(my_list[0:5:2])
# 0, 2, 4

print(my_list[::-1])
# 5, 4, 3, 2, 1, 0

print(my_list[::-2])
# 5, 3, 1
