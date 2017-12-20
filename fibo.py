def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    first_num = 0
    second_num = 1
    for i in range(2, n+1):
        cur_num = first_num + second_num
        first_num = second_num
        second_num = cur_num
    return cur_num


if __name__ == '__main__':
    a = int(input("Enter num:"))
    print(fibo(a))