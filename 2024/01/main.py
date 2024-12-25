def part1():
    with open("input") as f:
        lines = f.readlines()
        col1, col2 = list(zip(*(line.split() for line in lines)))
        distance = sum(
            map(
                lambda cur: abs(int(cur[0]) - int(cur[1])),
                zip(sorted(col1), sorted(col2)),
            )
        )
        print(distance)


def part2():
    from collections import Counter

    with open("input") as f:
        lines = f.readlines()
        col1, col2 = zip(*(map(int, line.split()) for line in lines))
        s1 = set(col1)
        s2 = Counter(col2)
        similarity_score = sum([s2[k] * k for k in s1])
        print(similarity_score)


if __name__ == "__main__":
    part2()
