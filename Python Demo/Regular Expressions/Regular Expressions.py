import re

email = input("What's your email? ").strip()

# if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
# if re.match(r"\w+@\w+\.edu$", email, re.IGNORECASE):
if re.fullmatch(r"(\w+|\s)@(\w+\.)?\w+\.edu", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


name = input("What's your name? ").strip()

# matches = re.search(r"^(.+), *(.+)$", name)
# if matches:
#     last, first = matches.group()
#     name = f"{first} {last}"

if matches := re.search(r"^(.+), *(.+)$", name):
    last = matches.group(1)
    first = matches.group(2)
    # the group(0) store some other data
    name = f"{first} {last}"

print(f"Hello, {name}")


url = input("URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#     print(f"Username: {matches.group(3)}")

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
