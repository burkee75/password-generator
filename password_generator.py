import string
import secrets
import argparse


def generate_password(length, special_chars=None, case=None):
    """Function to build password"""

    if not special_chars and not case:
        password_characters = string.ascii_letters + string.digits

    elif not special_chars:
        password_characters = string.ascii_letters + string.digits
        while True:
            password = "".join(
                secrets.choice(password_characters) for i in range(length)
            )
            if (
                any(character.islower() for character in password)
                and any(character.isupper() for character in password)
                and sum(character.isdigit() for character in password) >= 3
            ):
                break
    elif not case:
        password_characters = string.ascii_letters + string.digits + string.punctuation
    else:
        password_characters = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = "".join(
                secrets.choice(password_characters) for i in range(length)
            )
            if (
                any(character.islower() for character in password)
                and any(character.isupper() for character in password)
                and sum(character.isdigit() for character in password) >= 3
            ):
                break

    password = "".join(secrets.choice(password_characters) for i in range(length))

    return password


def main():
    my_parser = argparse.ArgumentParser(
        prog="password_generator",
        description="generate a password with specified length",
    )

    my_parser.add_argument(
        "--length",
        metavar="length",
        type=int,
        help="Number of characters",
        required=True,
    )
    my_parser.add_argument(
        "--special", action="store_true", help="Use special characters", required=False
    )

    my_parser.add_argument(
        "--case", action="store_true", help="Use different case, ie A a", required=False
    )

    # execute parser
    args = my_parser.parse_args()
    print(generate_password(args.length, args.special))


if __name__ == "__main__":
    main()
