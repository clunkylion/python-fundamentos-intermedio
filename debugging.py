def divisors(num):
    divisorsList = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisorsList.append(i)
    
    return divisorsList




def main():
    num = int(input("Enter a number: "))
    print(divisors(num))
    print('Finally here')
    

if __name__ == '__main__':
    main()