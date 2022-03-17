def main():
    num = int(input('Enter number for the strong: '))
    # calculating the strong of taken number
    fact = factorial(num)

    print('Strong of the number',num,'is:',fact)
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


main()