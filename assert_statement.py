def divisors(num):
    divisorsList = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisorsList.append(i)
    
    return divisorsList




def main():
    num = input("Enter a number: ")
    assert num.isnumeric(), 'Number is required'
    print(divisors(int(num)))
    print('Finally here')
    

if __name__ == '__main__':
    main()