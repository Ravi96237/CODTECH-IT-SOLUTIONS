import random
import string

def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
    character_set = ""
    if include_letters:
        character_set += string.ascii_letters
    if include_numbers:
        character_set += string.digits
    if include_symbols:
        character_set += string.punctuation

    if not character_set:
        print("Error: At least one character type (letters, numbers, or symbols) must be included.")
        return None

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def get_valid_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Error: Length must be a positive integer.")
            else:
                return length
        except ValueError:
            print("Error: Please enter a valid number.")

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).lower()
        if response in {'yes', 'no', 'y', 'n'}:
            return response == 'yes' or response == 'y'
        print("Error: Please enter 'yes' or 'no'.")

def main():
    print("Welcome to the Password Generator!")

    length = get_valid_length()

    include_letters = get_yes_no_input("Include letters (yes/no): ")
    include_numbers = get_yes_no_input("Include numbers (yes/no): ")
    include_symbols = get_yes_no_input("Include symbols (yes/no): ")

    password = generate_password(length, include_letters, include_numbers, include_symbols)

    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
