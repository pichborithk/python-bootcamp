def main():
    number = input("Amount: ")
    for s in sheep(number):
        print(s)


def sheep(n):
    for i in range(n):
        # we use yield here to iterate return value one by one
        # so that if n is too big the app won't make overload RAM then break app
        yield "A" * i


if __name__ == "__main__":
    main()