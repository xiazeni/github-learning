def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def main() -> None:
    a = float(input("请输入第一个数字："))
    operator = input("请输入运算符（+ 或 -）：")
    b = float(input("请输入第二个数字："))

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = subtract(a, b)
    else:
        print("暂不支持该运算符")
        return

    print(f"结果：{result}")


if __name__ == "__main__":
    main()