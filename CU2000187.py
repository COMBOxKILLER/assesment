################### blum blum shub random number generator ###################

#we should import time to use it in the seed.
import time;

#formula = xn+1=xn**2(modM).

#we used the time on the machine to make the seed very random.
seed = int(round(time.time()));

#a is a selected prime number.
a = 7

#c is a selected prime number.
c = 157117576973816034098969325683

#the modulus in the rule is equal to the multiplication of the two prime numbers.
m = a * c 

#giving the option to the user of how many random numbers does he want.
howmany = int(input("How many random numbers do you want?: "))

#function to calculate the formula using numbers in a specific range;
#which we used a for loop to get that range from the number the user entered;
#but in every loop we decrease by 1 untill it gets to 0;
#and we print the x before it is equaled to the previous seed.
def random():
    num_base = seed
    for i in range(howmany, 0, -1):
        x = (num_base**2) % m
        print(x)
        num_base = x


random()