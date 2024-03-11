import random

def main():
    print("欢迎来到猜数字游戏！")
    number = random.randint(1, 100)
    attempts = 0
    guess = None

    while guess != number:
        try:
            guess = int(input("请输入一个1到100之间的数字："))
        except ValueError:
            print("输入有误，请输入一个整数。")
            continue

        attempts += 1

        if guess < number:
            print("猜小了！")
        elif guess > number:
            print("猜大了！")
        else:
            print(f"恭喜你，猜对了！数字是{number}。")
            print(f"你一共猜了{attempts}次。")

if __name__ == "__main__":
    main()
