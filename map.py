def main():
    
    myList = [1,2,3,4,5,6,7,8,9,10]
    newList = list(map(lambda x: x**2, myList))
    print(newList)
    
    
    
if __name__ == '__main__':
    main()