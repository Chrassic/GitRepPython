#import fibo
#fibo.fib (10)

weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    weight_in_kg = weight*0.45
    print (f"You are {weight_in_kg} kg.")
elif unit.upper() == "K":
    weight_in_lbs = weight/0.45
    print (f"You are {weight_in_lbs} lbs.")
else:
    print ("Wrong input.")
#ytvid: 1:20:49
