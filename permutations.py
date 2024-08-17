def permutation(x,y,z,n):
    co_ordinates = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
    print(co_ordinates)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # function call
    permutation(x,y,z,n)
