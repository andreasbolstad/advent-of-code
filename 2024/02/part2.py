def main():
    with open("input") as f:
        lines = f.readlines()
    safe_count = sum(is_dampened_safe(line) for line in lines)
    print(safe_count)


def is_dampened_safe(line):
    cells = list(map(int, line.split()))
    for i in range(len(cells)):
        if is_safe(cells[:i] + cells[i + 1 :]):
            return True
    return False


def is_safe(cells):
    is_increasing = cells[1] > cells[0]
    for a, b in zip(cells[:-1], cells[1:]):
        d = (b - a) * (1 if is_increasing else -1)
        if not 1 <= d <= 3:
            return False
    return True


if __name__ == "__main__":
    main()
