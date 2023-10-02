# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("usage: meows.py")


import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow", default=1, type=int)
args = parser.parse_args()

# for _ in range(int(args.n)):
# args.n is the integer (we specify the type above) that user type after -n (need to add space)
for _ in range(args.n):
    print("meow")
