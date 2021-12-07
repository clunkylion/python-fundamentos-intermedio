from functools import reduce

def main():
    myList = [1,2,3,4,5,6,7,8,9,10]
    newListReduce = reduce(lambda x,y: x*y, myList)
if __name__ == '__main__':
    main()