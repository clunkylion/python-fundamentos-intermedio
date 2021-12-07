def main():
    #myDict = {}
    # for i in range(1,101):
    #     if i % 3 == 0:
    #         myDict[i] = i**3
    #dict comprehension
    myDict = {i:i**3 for i in range(1,101) if i % 3 == 0}
    
    print(myDict)



if __name__ == '__main__':
    main()