import sys
import time

def simple_progress_bar():
    for i in range(1, 101):

        print("\r", end="")

        # print("进度: {}%: ".format(i), "▓" * (i // 2), end="")
        print(f"进度: {i}%: ", "▓" * (i // 2), end="")

        # 通常，Python 的 print() 函数并不会立即将输出显示在终端上，而是先存储在输出缓冲区中，直到缓冲区满了或遇到换行符时才会刷新到屏幕。
        # sys.stdout.flush() 强制刷新缓冲区的内容，无论缓冲区是否满或遇到换行符。
        sys.stdout.flush()

        time.sleep(0.05)


if __name__ == '__main__':
    simple_progress_bar()