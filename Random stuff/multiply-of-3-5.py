# the sum of all the multiples of 3 or 5
def main():
    domain = 1000
    sum_of_multies = 0
    i = 0
    while i < domain:
        if (i % 3 == 0 or i % 5 == 0):
            sum_of_multies = sum_of_multies + i
        i += 1
    print(sum_of_multies)


main()
