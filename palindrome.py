def is_palindrome(n):
    rev = 0
    temp = n
    while temp != 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    return rev == n


if __name__ == '__main__':
    a = int(input('Enter number: '))
    print(is_palindrome(a))