from itertools import product


def maximize_expression(K, M, lists):
    max_value = 0
    for combinations in product(*lists):
        value = 0
        for x in combinations:
            value += x * x
        value = value % M
        if value > max_value:
            max_value = value
    return max_value


if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
