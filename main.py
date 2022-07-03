def main():
    def sum_of_two():
        a = int(input("Enter the first number: "))
        b = int(input("Enter the first number: "))
        c = a + b 
        return c

    while(True):
        c = sum_of_two()
        print('Sum of two number is :',c)

        user_input = input('Do you want calculation (y/[n])? ')
        if user_input != 'y':
            break
    

if __name__ == '__main__':
    main()
