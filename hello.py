"""
Hello World 模块
一个简单的问候模块，用于演示基本的 Python 模块结构。
"""


def greet(name: str = "World") -> str:
    """生成问候语。

    Args:
        name: 要问候的名字，默认为 "World"。

    Returns:
        问候语字符串。
    """
    return f"Hello, {name}!"


def main():
    """主函数入口。"""
    print(greet())
    print(greet("Python"))


if __name__ == "__main__":
    main()
    print("dsfsdf")
    print("dfsdsfsedfsf")
    print("sdtgfdfgdfgdfgfeggdfg")