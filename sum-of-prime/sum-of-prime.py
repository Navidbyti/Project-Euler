def main():
    i = 1
    sop = 2

    while i <= 100:
        j = 2
        #--------------------
        while j < i:
            
            if(i%j == 0):
                break
            elif(j == i - 1 ):
                sop += i
            j += 1
        #------------------------
                
        i += 1



    print(sop)
main()