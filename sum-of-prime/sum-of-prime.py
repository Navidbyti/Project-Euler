import math

def main():
    i = 1
    sop = 5

    while i < 2000000:
        j = 5
        # --------------------
        while i> j:
            
            if(i % j == 0 ):
                print(i,j)
                print("break")
                break
            elif(j > math.ceil(math.sqrt(i))):
                sop += i
                print(i)
                break
            j += 1
        # ------------------------

        i += 2

    print("final: ",sop)


main()
