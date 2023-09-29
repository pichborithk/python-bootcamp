my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_list = sorted(my_dict)
print(sorted_list)
sorted_tuples = sorted(my_dict.items())
print(sorted_tuples)
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)

my_list = [
    {"name": "a", "age": 3},
    {"name": "b", "age": 4},
    {"name": "c", "age": 1},
    {"name": "d", "age": 5},
    {"name": "e", "age": 2},
]

sorted_age = sorted(my_list, key=lambda dic: dic["age"], reverse=True)
print(sorted_age)
