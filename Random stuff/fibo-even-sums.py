def main():
    
   print(fibo_sum(4000000))


def fibo_sum(max):
    x=y=1
    z=0
    fibo_sums = 0
    while  z < max :
        if z%2 == 0:
            fibo_sums += z
        z = x + y
        x = y
        y = z
        
        
        print(z)
    return fibo_sums
main()