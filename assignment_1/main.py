from message_formattor import decorator, decorator2


@decorator
@decorator2
def greet(param: str) -> None:
    print(param)


def main():
    greet("Welcome to my project")
    print("\n")
    greet("Hi there!")


if __name__ == "__main__":
    main()
