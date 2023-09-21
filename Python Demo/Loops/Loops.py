my_list = ["a", "b", "c", "d", "e", "f"]

for s in my_list:
    print(s, end=" ")


print("")
for index in range(len(my_list)):
    print(index, end=" ")


print("")
for number in range(5):
    print(number, end=" ")
    # 0, 1, 2, 3, 4


print("")
for number in range(1, 10):
    print(number, end=" ")
    # 1, 2, 3, 4, 5, 6, 7, 8, 9


print("")
for number in range(1, 10, 3):
    print(number, end=" ")
    # 1, 4, 7


# While loop
condition = 5
print("")
while condition > 0:
    print(condition, end=" ")
    condition -= 1


# Dictionary Loop
my_dict = {"a": 1, "b": 2, "c": 3}

print("")
for key in my_dict:
    print(key, end=" ")
    # a, b, c


print("")
for key, value in my_dict.items():
    print(key, value)


# Comprehension
new_list_1 = [f"new {item}" for item in my_list]
print(new_list_1)

my_string = "abcde"

new_list_2 = [letter for letter in my_string]
print(new_list_2)

new_list_3 = [number + 1 for number in range(1, 6)]
print(new_list_3)

new_dict_1 = {f"key {item}": item for item in my_list}
print(new_dict_1)

new_dict_2 = {f"new {key}": value + 1 for key, value in my_dict.items()}
print(new_dict_2)

# Conditional Comprehension
new_list_4 = [number for number in new_list_3 if number % 2 == 0]
print(new_list_4)

new_dict_3 = {f"new {key}": value for key, value in my_dict.items() if value % 2 != 0}
print(new_dict_3)
