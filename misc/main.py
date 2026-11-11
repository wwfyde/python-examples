import getpass


def main():
    a = getpass.getpass(prompt="Password: ", echo_char="*")
    print(a)
    print("Hello from misc!")


if __name__ == "__main__":
    main()
