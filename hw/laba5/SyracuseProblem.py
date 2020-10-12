def check_arg(arg):
    try:
        float(arg)
    except ValueError:
        return False
    return True


def syracuse_problem(n: int):
    if n == 1:
        return n
    elif n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


if __name__ == '__main__':
    n = input()
    while not check_arg(n):
        print('Введите число в верном формате, пожалуйста')
        n = input()
    n = int(float(n))
    sequence = [n]
    while n != 1:
        n = syracuse_problem(n)
        sequence.append(n)
    print(', '.join(map(str, sequence)))
    # with open('output.txt', 'w') as f:  # запись в файл удобнее, чем просто печать
    #     print(', '.join(map(str, sequence)), file=f)
