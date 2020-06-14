import sys

def one():
    max = 1000
    multiples = []

    for i in range(1, max):
        if (i % 3 == 0 or i % 5 == 0):
            multiples.append(i)
            print(i)

    sum = 0
    for j in multiples:
        sum = sum + j

    print(sum)

def two():
    max = 4000000
    fibonacciSeries = [1, 1]

    key = 1
    sum = 0
    while fibonacciSeries[key] <= max:
        nextNumber = fibonacciSeries[key-1] + fibonacciSeries[key]
        fibonacciSeries.append(nextNumber)

        if nextNumber % 2 == 0:
            sum = sum + nextNumber

        key+=1

    print(fibonacciSeries)
    print(sum)

def main():
    bigNum = 600851475143
    factors = []
    
    

    print(factors)

        
        
if __name__ == '__main__':
    main()