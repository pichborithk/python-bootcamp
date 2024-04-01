from dotenv import load_dotenv

load_dotenv()

from data_manager import DataManager


def main():
    data_manager = DataManager()

    print("Welcome to Flight Club.")
    print("We find the best flights deals and email you.")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    email = input("What is your email?\n")
    confirmation = input("Type your email again.\n")
    if email == confirmation:
        data_manager.add_user_data(
            first_name=first_name, last_name=last_name, email=email
        )


if __name__ == "__main__":
    main()
