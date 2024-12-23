def main():
    with open("input") as f:
        lines = f.readlines()
        col1, col2 = list(zip(*(line.split() for line in lines)))
        distance = sum(map(lambda cur: abs(int(cur[0]) - int(cur[1])), zip(sorted(col1), sorted(col2))))
        print(distance)


if __name__ == "__main__":
    main()
