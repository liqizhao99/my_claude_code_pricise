"""A simple Hello World module."""


def greet(name: str = "World") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


def main() -> None:
    """Print the default greeting."""
    print(greet())


if __name__ == "__main__":
    main()
