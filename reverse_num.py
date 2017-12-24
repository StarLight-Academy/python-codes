def reverse_num(n):
    rev = 0
    while n != 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev


if __name__ == '__main__':
    a = int(input('Enter no: '))
    print(reverse_num(a))