# FileNotFoundError
# with open("a") as file:
#     file.read()

# KeyError
# my_dict = {"a": 1, "b": 2}
# print(my_dict["c"])

# IndexError
# my_list = [1, 2, 3]
# print(my_list[3])

# TypeError
# my_string = "abc"
# print(my_string + 5)

try:
    # something might cause an Error
    file = open("a.txt")
# except:  # do this if there was an Error of any Type
except FileNotFoundError:  # do this only if there was a FileNotFoundError
    file = open("a.text", "w")
    file.write("Something")
# except KeyError as error_message: # can have multiple Exception to handle any type of Error
#     print(error_message)
else:
    # do this if there were no Error
    content = file.read()
    print(content)
finally:
    # do this no matter what happens
    file.close()
    print("File was closed.")

# Raise Custom Exception

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")


# Testing
def squared(n):
    return n * n


def test_squared():
    try:
        assert squared(2) != 4
    except AssertionError:
        print("squared(2) is not equal to 4")
