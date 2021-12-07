def main():
    squares = []
    # for i in range(1, 101):
    #     if i %3 != 0:
    #         squares.append(i**2)
        
    # for i in squares:
    #     print(i)
    ## este  es un ejemplo de list comprehension pero todo dentro de una linea, esta reasignando el valor de i a cada iteracion
    ## y lo que hace es multiplicar i por i y lo guarda en la lista squares
    ## es similar a un if ternario 
    squares =[i**2 for i in range(1, 101) if i %3 != 0]
    print(squares)


if __name__ == '__main__':
    main()