def main():
    numbers = [1,2,3,4,5,6,7,8,9]
    total = 0
    for x in numbers:
        total += x
        print(x,'sub_total=', total)
    print('total = ', total)
    print('------------------')

    numbers1 = [1,2,3,4,5,6,7,8,9]
    my_sum = range_sum(numbers1,0,8)
    print(my_sum)
def range_sum(num_list,start,end):
        if start > end:
            return 0
        else:
            return num_list[start] + range_sum(num_list,start + 1,end)
main()