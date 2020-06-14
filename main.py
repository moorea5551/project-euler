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
    
    #largest factor has to be half of big num or lower
    if 0 == bigNum % 2:
        startingNum = bigNum // 2
    else:
        startingNum = (bigNum + 1) // 2
    
    for i in range(startingNum, 0, -1):
        if 0 == bigNum % i:
            factors.append(i)
            print('.')
            sys.stdout.flush()
            
    print(factors)

        
        
if __name__ == '__main__':
    main()