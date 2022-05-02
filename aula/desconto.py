import os
os.system ("cls")

comb=int(input("What type of fuel do you need [1] Gasoline [2] Ethanol: "))
liters=float(input("How many liters do you need: "))

if comb == 1:
    value=liters*6
    if liters <=10: 
        final=value-(value*(0.03))
        print ("\nTotal without the discount:",value,"\n")
        print ("With the discount of 3%, the total will be:",final,"\n")
    if liters>10 and liters<=20:
        print ("\nTotal without the discount:",value,"\n")
        print ("With the discount of 5%, the total will be:",value-(value*0.05),"\n")
    elif liters>20:
        print ("\nTotal without the discount:",value)
        print ("With the discount of 7%, the total will be:",value-(value*0.07),"\n")

elif comb == 2:
    value=liters*5
    if liters <= 10:
        print ("\nTotal without the discount:",value, "\n")
        print ("With the discount of 4%, the total will be:",value-(value*0.04),"\n")
    if liters>10 and liters <=20:
        print ("\nTotal without the discount:",value,"\n")
        print ("With the discount of 6%, the total will be:",value-(value*0.06),"\n")
    elif liters>20:
        print ("\nTotal without the discount:",value,"\n")
        print ("With the discount of 8%, the total will be:",value-(value*0.08),"\n")


