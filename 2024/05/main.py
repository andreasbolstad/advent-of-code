from collections import defaultdict

from networkx import DiGraph, topological_sort


def part1():
    with open("input") as f:
        lines = f.read().strip().splitlines()
    split_index = lines.index("")
    rules, updates = lines[:split_index], lines[split_index + 1 :]
    page_to_conditions = defaultdict(list)
    for rule in rules:
        page, condition = rule.split("|")
        page_to_conditions[page].append(condition)
    middle_sum = 0
    for update in updates:
        pages = update.split(",")
        if all(
            not set(pages[:i]) & set(page_to_conditions[page])
            for i, page in enumerate(pages)
        ):
            middle_sum += int(pages[len(pages) // 2])
    print(middle_sum)


def part2():
    with open("input") as f:
        lines = f.read().strip().splitlines()
    split_index = lines.index("")
    rules, updates = lines[:split_index], lines[split_index + 1 :]
    page_to_conditions = defaultdict(list)
    for rule in rules:
        page, condition = rule.split("|")
        page_to_conditions[page].append(condition)
    middle_sum = 0
    for update in updates:
        pages = update.split(",")
        if not all(
            not set(pages[:i]) & set(page_to_conditions[page])
            for i, page in enumerate(pages)
        ):
            edges = [
                (page, condition)
                for page in pages
                for condition in set(page_to_conditions[page]) & set(pages)
            ]
            graph = DiGraph(edges)
            ordered_update = list(topological_sort(graph))
            middle_sum += int(ordered_update[len(ordered_update) // 2])
    print(middle_sum)


if __name__ == "__main__":
    part2()
