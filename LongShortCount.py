def main():
    n=int(input("enter the number for trades you want to input: "))
    lcount=0
    scount=0
    for i in range(n):
        while True:
            inp=input("enter whether trade number "+str(i+1)+" is long or short: ")
            if inp.lower()=="short":
                scount+=1
                break
            elif inp.lower()=="long":
                lcount+=1
                break
            else:
                print("invalid response, try again")

    print("DATA: Long -> ",lcount," Short -> ",scount)
    return None

main()
