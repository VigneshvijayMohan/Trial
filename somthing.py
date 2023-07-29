def main():
    x = int(input("What is the value of x..?"))
    print("x squared is", square(x))
    
def square(n):
    sq = n * n
    return(sq)
    

if __name__ == '__main__':
    main()