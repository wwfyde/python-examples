def chicken_purchase(chicken: int, money: int) -> tuple:
    for a in range(chicken):
        for b in range(chicken):
            if 5 * a + 3 * b + (chicken - a - b) / 3 == money and (chicken - a - b) % 3 == 0:
                return a, b, 100 - a - b
    return 0, 0, 0


if __name__ == '__main__':
    print(chicken_purchase(100, 100))
