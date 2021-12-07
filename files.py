from os import name


def read():
    numbers = []
    with open('./files/numbers.txt', 'r', encoding='utf-8') as file:
        for number in file:
            numbers.append(int(number))
    print(numbers)
def write():
    names = ['John', 'Bob', 'Alice']
    with open('./files/names.txt', 'w', encoding='utf-8') as file:
        for name in names:
            file.write(name + '\n')

def main():
    write()

if __name__ == '__main__':
    main()