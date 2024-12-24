import math
import re


def main():
    with open("input") as f:
        text = "".join(f.readlines())
    text = re.sub(r"(?s)(don't\(\).*?do\(\))", "", text)
    text = re.sub(r"(?s)(don't\(\).*?)", "", text)
    matches = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", text)
    return sum([math.prod(map(int, match)) for match in matches])


if __name__ == "__main__":
    print(main())
