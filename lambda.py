def main():
    
    #palindrome normal function
    def isPalindrome(word):
        return word == word[::-1]
    
    #palindrome lambda function
    ##                  expression argument : login and return // similar a arrow function in js
    isPalindromeLambda = lambda word: word == word[::-1]
if __name__ == '__main__':
    main()