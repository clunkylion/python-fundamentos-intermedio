def main():
    myList = [1,'hello',True, 4.5]
    myDict = {'firstName':'José','lastName':'Cortés'}
    super_list = [
         {'firstName':'José','lastName':'Cortés'},
          {'firstName':'Esteban','lastName':'Cortés'},
           {'firstName':'Patricia','lastName':'Molina'}
    ]
    super_dict = {
        'naturalNumbs':[1,2,3,4,5,6,7,8,9,10],
        'integersNumbs':[-1,-2,-3,0,1,2,3,4,5,6,7,8,9,10],
        'floatingNumbs':[-1.1,-2.2,-3.3,0.0,1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.0],
    }
    for  key, value in super_dict.items():
        print(key, '-', value)
    for i in super_list:
        print(i.items())    
    
if __name__ == '__main__':
    main()