def main():
    message(5)
def message(times):
    count = 0
    if times > 0:
        count += 1
        print(count,'This is recurtion function.')
        message(times - 1)

main()