def happy_transform(n):
    orig_n, s = n, 0
    while n:
        n, d = divmod(n, 10)
        s += d ** 2
    print(f'happy_transform: {orig_n} -> {s}')
    return s


def is_happy(n):
    results = []
    last_result = n
    while last_result != 1 and not loop_detected(results):
        last_result = happy_transform(last_result)
        results.append(last_result)
    return last_result == 1  # if not, then we exited loop due to loop_detected fn


def loop_detected(results):
    return len(results) != len(set(results))


if __name__ == '__main__':
    print(is_happy(19))
