import random
 
def main():
        # Easier way of declaring the 5 lists
        letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
        letters2 = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
        numbers = "1,2,3,4,5,6,7,8,9,0".split(",")
        sChar = "!,@,#,$,%,^,*,(,)<,>,-,+,?".split(",")
 
        # To pick from all the elements we need a common list
        everything = letters + letters2 + numbers + sChar
        
        # To offer more service we need to know the length of the password.
        nums = int(input("How long would you like the password to be? Enter a number: "))
    
        # We use random.choice on the everything list, and print it out at once
        for i in range(nums):
                print (random.choice(everything), end='')
        print("")
        
        # Do we want to do it again?
        multirun = input("Do you want to generate another password? Enter yes or no: ")
        if multirun.lower() == "yes":
                print("")
                # Recursion is good.
                main()

# Executing the main function
main()
