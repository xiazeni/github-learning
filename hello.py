def greet(name: str) -> None:
    """Print a greeting message."""
    print(f"Hello, {name}! Welcome to GitHub.")


def main() -> None:
    name = input("请输入你的名字：")
    greet(name)


if __name__ == "__main__":
    main()