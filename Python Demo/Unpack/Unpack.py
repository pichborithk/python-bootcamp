# first, last = input("Enter full name: ")

# print(f"Hello {first} {last}")

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


# coins = (100, 50, 25)
coins = [100, 50, 25]

print(total(*coins), "Knuts")

coins_dict = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins_dict), "Knuts")


def positional_print(*args):
    print("Positional:", args)


positional_print(5, 10, 1, 3)
positional_print(5, 10, 1, 3, 500)


def named_print(**kwargs):
    print("Named:", kwargs)


named_print(galleons=100, sickles=50, knuts=25)
named_print(galleons=100, knuts=25)
